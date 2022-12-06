"""
CRUD operations for concepts and related tables in the DB
"""

import json
from logging import Logger
from typing import List, Optional
from urllib.parse import quote_plus

from fastapi import APIRouter, Depends, Query, Response, status
from sqlalchemy import func
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Session

from tds.autogen import orm, schema
from tds.db import request_rdb
from tds.lib.concepts import fetch_from_dkg, mark_concept_active

logger = Logger(__file__)
router = APIRouter()


@router.get("")
def search_concept(curie: str, rdb: Engine = Depends(request_rdb)):
    """
    Searches within TDS for artifacts with this concept term associated with them
    """
    results = []
    with Session(rdb) as session:
        result_list = (
            session.query(orm.OntologyConcept)
            .filter(orm.OntologyConcept.curie == curie)
            .all()
        )

    for result in result_list:
        result.__dict__.pop("id")
        results.append(result)
    return results


@router.get("/definitions")
def search_concept_definitions(term: str, limit: int = 100, offset: int = 0):
    """
    Wraps search functionality from the DKG.
    """
    params = f"/search?q={term}&limit={limit}&offset={offset}"
    return fetch_from_dkg(params)


@router.get("/definitions/{curie}")
def get_concept_definition(curie: str):
    """
    Wraps fetch functionality from the DKG.
    """
    params = f"/entity/{quote_plus(curie)}"
    return fetch_from_dkg(params)


def get_taggable_orm(taggable_type: schema.TaggableType):
    """
    Maps resource type to ORM
    """
    enum_to_orm = {
        schema.TaggableType.features: orm.Feature,
        schema.TaggableType.qualifiers: orm.Qualifier,
        schema.TaggableType.datasets: orm.Dataset,
        schema.TaggableType.simulation_plans: orm.SimulationPlan,
        schema.TaggableType.models: orm.Model,
        schema.TaggableType.model_parameters: orm.ModelParameter,
        schema.TaggableType.projects: orm.Project,
        schema.TaggableType.publications: orm.Publication,
        schema.TaggableType.simulation_runs: orm.SimulationRun,
        schema.TaggableType.intermediates: orm.Intermediate,
        schema.TaggableType.simulation_parameters: orm.SimulationParameter,
    }
    return enum_to_orm[taggable_type]


@router.get("/facets")
def search_concept_using_facets(
    types: List[schema.TaggableType] = Query(default=None),
    curies: Optional[List[str]] = Query(default=None),
    is_simulation: bool = Query(default=False),
    rdb: Engine = Depends(request_rdb),
) -> Response:
    """
    Search along type and curie facets
    """
    with Session(rdb) as session:
        default_search_body = {
            "types": {
                type: session.query(get_taggable_orm(type)).count() for type in types
            },
            "curies": session.query(
                func.count(orm.OntologyConcept.curie),
                orm.OntologyConcept.curie,
                orm.ActiveConcept.name,
            )
            .join(
                orm.ActiveConcept,
                orm.OntologyConcept.curie == orm.ActiveConcept.curie,
                isouter=True,
            )
            .filter(orm.OntologyConcept.type != "datasets")
            .group_by(orm.OntologyConcept.curie, orm.ActiveConcept.name),
            "results": session.query(orm.OntologyConcept, orm.ActiveConcept.name)
            .join(
                orm.ActiveConcept,
                orm.OntologyConcept.curie == orm.ActiveConcept.curie,
                isouter=True,
            )
            .filter(orm.OntologyConcept.type != "datasets"),
        }
        dataset_search_body = {
            "types": session.query(orm.Dataset)
            .filter(orm.Dataset.simulation_run == is_simulation)
            .count(),
            "curies": session.query(
                func.count(orm.OntologyConcept.curie),
                orm.OntologyConcept.curie,
                orm.ActiveConcept.name,
            )
            .join(
                orm.ActiveConcept,
                orm.OntologyConcept.curie == orm.ActiveConcept.curie,
                isouter=True,
            )
            .filter(orm.OntologyConcept.type == "datasets")
            .join(
                orm.Dataset,
                orm.OntologyConcept.object_id == orm.Dataset.id,
            )
            .filter(orm.Dataset.simulation_run == is_simulation)
            .group_by(orm.OntologyConcept.curie, orm.ActiveConcept.name),
            "results": session.query(orm.OntologyConcept, orm.ActiveConcept.name)
            .join(
                orm.ActiveConcept,
                orm.OntologyConcept.curie == orm.ActiveConcept.curie,
                isouter=True,
            )
            .filter(orm.OntologyConcept.type == "datasets")
            .join(
                orm.Dataset,
                orm.OntologyConcept.object_id == orm.Dataset.id,
            )
            .filter(orm.Dataset.simulation_run == is_simulation),
        }

        search_body = {"facets": {"types": {}, "concepts": {}}, "results": []}
        for key in default_search_body:
            if key == "types":
                continue
            if types is not None:
                default_search_body[key] = default_search_body[key].filter(
                    orm.OntologyConcept.type.in_(types)
                )
            if curies is not None:
                default_search_body[key] = default_search_body[key].filter(
                    orm.OntologyConcept.curie.in_(curies)
                )

        search_body["facets"]["types"].update(default_search_body["types"])
        search_body["facets"]["concepts"].update(
            {
                hit[1]: {"count": hit[0], "name": hit[2]}
                for hit in default_search_body["curies"]
            }
        )
        search_body["results"].extend(
            [
                {
                    "type": entry.type,
                    "id": entry.object_id,
                    "curie": entry.curie,
                    "name": name,
                }
                for entry, name in default_search_body["results"]
            ]
        )
        for key in dataset_search_body:
            if curies is not None:
                default_search_body[key] = default_search_body[key].filter(
                    orm.OntologyConcept.curie.in_(curies)
                )

        if "datasets" in types:
            search_body["facets"]["types"]["datasets"] = dataset_search_body["types"]
            search_body["facets"]["concepts"].update(
                {
                    hit[1]: {"count": hit[0], "name": hit[2]}
                    for hit in dataset_search_body["curies"]
                }
            )
            search_body["results"].extend(
                [
                    {
                        "type": entry.type,
                        "id": entry.object_id,
                        "curie": entry.curie,
                        "name": name,
                    }
                    for entry, name in dataset_search_body["results"]
                ]
            )

        return Response(
            status_code=status.HTTP_200_OK,
            headers={
                "content-type": "application/json",
            },
            content=json.dumps(search_body),
        )


@router.get("/{id}")
def get_concept(id: int, rdb: Engine = Depends(request_rdb)) -> str:
    """
    Get a specific concept by ID
    """
    with Session(rdb) as session:
        result = session.query(orm.OntologyConcept).get(id)
        return result


@router.post("")
def create_concept(payload: schema.OntologyConcept, rdb: Engine = Depends(request_rdb)):
    """
    Create a concept
    """
    with Session(rdb) as session:
        concept_dict = payload.dict()
        concept = orm.OntologyConcept(**concept_dict)
        mark_concept_active(session, concept.curie)
        session.add(concept)
        session.commit()
        return Response(
            status_code=status.HTTP_201_CREATED,
            headers={
                "content-type": "application/json",
            },
            content=json.dumps({"id": concept.id}),
        )


@router.patch("/{id}")
def update_concept(
    payload: schema.OntologyConcept, id: int, rdb: Engine = Depends(request_rdb)
) -> str:
    """
    Update a concept by ID
    """
    with Session(rdb) as session:
        data_payload = payload.dict(exclude_unset=True)
        data_payload["id"] = id
        mark_concept_active(session, data_payload["curie"])
        logger.info(data_payload)

        data_to_update = session.query(orm.OntologyConcept).filter(
            orm.OntologyConcept.id == id
        )
        data_to_update.update(data_payload)
        session.commit()
    return "Updated Concept"


@router.delete("/{id}")
def delete_concept(id: int, rdb: Engine = Depends(request_rdb)):
    """
    Delete a concept by ID
    """
    with Session(rdb) as session:
        session.query(orm.OntologyConcept).filter(orm.OntologyConcept.id == id).delete()
        session.commit()
