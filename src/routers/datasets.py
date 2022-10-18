"""
router.datasets - crud operations for datasets and related tables in the DB
"""

import json
from db import ENGINE
from pydantic import BaseModel
from fastapi import APIRouter
from generated import schema, orm
from logging import Logger
from sqlalchemy.orm import Session
from typing import List

logger = Logger(__file__)
router = APIRouter()


@router.get("/datasets")
def get_datasets(count: int) -> str:
    with Session(ENGINE) as session:
        result = (
            session.query(orm.Datasets).order_by(orm.Datasets.id.desc()).limit(count)
        )
        logger.info(f"Pre manip result: {result}")
        result = result[::-1]
        logger.info(f"Latest output: {result}")
        return result


@router.get("/datasets/{id}")
def get_datasets(id: int) -> str:
    with Session(ENGINE) as session:
        result = session.query(orm.Datasets).get(id)
        logger.info(f"Latest output: {result}")
        return result


class CreateDatasetRequest(BaseModel):
    dataset: schema.Datasets
    features: List[schema.Features]


@router.post("/datasets")
def create_dataset(payload: CreateDatasetRequest) -> str:
    with Session(ENGINE) as session:
        datasetp = payload.dataset.dict()
        del datasetp["id"]
        dataset = orm.Datasets(**datasetp)
        session.add(dataset)
        session.commit()
        for f in payload.features:
            feat = f.dict()
            del feat["id"]
            feat["dataset_id"] = dataset.id
            feature = orm.Features(**feat)
            session.add(feature)
        session.commit()
    return "Created dataset"


@router.patch("/datasets/update/{id}")
def update_dataset(payload: schema.Datasets, id: int) -> str:
    with Session(ENGINE) as session:
        data_payload = payload.dict(
            exclude_unset=True
        )  # Exclude unset not working, throws 422 if schema.Datasets in malformed.
        data_payload["id"] = id
        logger.info(data_payload)

        data_to_update = session.query(orm.Datasets).filter(orm.Datasets.id == id)
        data_to_update.update(data_payload)
        session.commit()
    return "Updated dataset"


# Not working because of lack of cascade settings in ORM? Features foreign key blocks the delete.
@router.post("/datasets/delete/{id}")
def delete_dataset(id: int) -> str:
    with Session(ENGINE) as session:
        session.query(orm.Datasets).filter(orm.Datasets.id == id).delete()
        session.commit()
