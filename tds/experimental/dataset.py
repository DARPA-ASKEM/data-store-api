"""
Dataset Schema
"""

from json import dumps
from logging import Logger
from typing import List

import strawberry
from sqlalchemy.orm import Session
from strawberry.types import Info

from tds.autogen import orm, schema
from tds.db import list_by_id
from tds.experimental.enum import ValueType
from tds.experimental.helper import sqlalchemy_type

logger = Logger(__name__)


class QualifierSchema(schema.Qualifier):
    class Config:
        orm_mode = True


class FeatureSchema(schema.Feature):
    class Config:
        orm_mode = True


class DatasetSchema(schema.Dataset):
    @classmethod
    def from_orm(cls, body: orm.SimulationPlan) -> "DatasetSchema":
        """
        Handle ORM conversion while coercing `dict` to JSON
        """
        setattr(body, "annotations", dumps(body.annotations))
        return super().from_orm(body)

    class Config:
        orm_mode = True


@sqlalchemy_type(orm.Qualifier)
@strawberry.experimental.pydantic.type(model=QualifierSchema)
class Qualifier:
    id: strawberry.auto
    dataset_id: strawberry.auto
    description: strawberry.auto
    name: strawberry.auto
    value_type: ValueType

    @staticmethod
    def from_pydantic(instance: QualifierSchema) -> "Qualifier":
        data = instance.dict()
        data["value_type"] = ValueType(data["value_type"].name)
        return Qualifier(**data)


@sqlalchemy_type(orm.Feature)
@strawberry.experimental.pydantic.type(model=FeatureSchema)
class Feature:
    id: strawberry.auto
    dataset_id: strawberry.auto
    description: strawberry.auto
    display_name: strawberry.auto
    name: strawberry.auto
    value_type: ValueType

    @strawberry.field
    def qualifiers(self, info: Info) -> List[Qualifier]:
        with Session(info.context["rdb"]) as session:
            fetched_qualifiers: List[orm.QualifierXref] = (
                session.query(orm.QualifierXref)
                .join(orm.Qualifier, orm.QualifierXref.qualifier_id == orm.Qualifier.id)
                .filter(orm.QualifierXref.feature_id == self.id)
                .all()
            )
        return [Qualifier.from_orm(qualifier[1]) for qualifier in fetched_qualifiers]

    @staticmethod
    def from_pydantic(instance: FeatureSchema) -> "Feature":
        data = instance.dict()
        data["value_type"] = ValueType(data["value_type"].name)
        return Feature(**data)


@sqlalchemy_type(orm.Dataset)
@strawberry.experimental.pydantic.type(model=DatasetSchema)
class Dataset:
    id: strawberry.auto
    name: strawberry.auto
    url: strawberry.auto
    description: strawberry.auto
    timestamp: strawberry.auto
    deprecated: strawberry.auto
    sensitivity: strawberry.auto
    quality: strawberry.auto
    temporal_resolution: strawberry.auto
    geospatial_resolution: strawberry.auto
    maintainer: strawberry.auto
    simulation_run: strawberry.auto

    @strawberry.field
    def qualifiers(self, info: Info) -> List[Qualifier]:
        with Session(info.context["rdb"]) as session:
            fetched_qualifiers: List[orm.Qualifier] = (
                session.query(orm.Qualifier)
                .filter(orm.Qualifier.dataset_id == self.id)
                .all()
            )
        return [Qualifier.from_orm(qualifier) for qualifier in fetched_qualifiers]

    @strawberry.field
    def features(self, info: Info) -> List[Feature]:
        with Session(info.context["rdb"]) as session:
            fetched_features: List[orm.Feature] = (
                session.query(orm.Feature)
                .filter(orm.Feature.dataset_id == self.id)
                .all()
            )
        return [Feature.from_orm(feat) for feat in fetched_features]

    @staticmethod
    def from_pydantic(instance: DatasetSchema) -> "Dataset":
        data = instance.dict()
        del data["annotations"]
        return Dataset(**data)


def list_datasets(info: Info) -> List[Dataset]:
    fetched_datasets: List[orm.Dataset] = list_by_id(
        info.context["rdb"].connect(), orm.Dataset, 100, 0
    )
    return [Dataset.from_orm(dataset) for dataset in fetched_datasets]