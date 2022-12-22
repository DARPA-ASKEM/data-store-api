"""
CRUD operations for models
"""

import json
from logging import Logger
from typing import List

from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Query, Session

from tds.autogen import orm, schema
from tds.db import (
    ProvenanceHandler,
    entry_exists,
    list_by_id,
    request_graph_db,
    request_rdb,
)
from tds.lib.models import adjust_model_params, model_opt_relationship_mapping
from tds.operation import create, delete, retrieve, update
from tds.schema.model import (
    Intermediate,
    Model,
    ModelDescription,
    ModelFramework,
    ModelOptPayload,
    ModelParameters,
    orm_to_params,
)
from tds.schema.provenance import Provenance
from tds.settings import settings

logger = Logger(__name__)
router = APIRouter()


@router.post("/frameworks", **create.fastapi_endpoint_config)
def create_framework(
    payload: ModelFramework, rdb: Engine = Depends(request_rdb)
) -> Response:
    """
    Create framework metadata
    """

    with Session(rdb) as session:
        framework_payload = payload.dict()
        framework = orm.ModelFramework(**framework_payload)
        session.add(framework)
        session.commit()
        name: str = framework.name
    logger.info("new framework with %i", name)
    return Response(
        status_code=status.HTTP_201_CREATED,
        headers={
            "content-type": "application/json",
        },
        content=json.dumps({"name": name}),
    )


@router.get("/frameworks/{name}", **retrieve.fastapi_endpoint_config)
def get_framework(name: str, rdb: Engine = Depends(request_rdb)) -> ModelFramework:
    """
    Retrieve framework metadata
    """
    with Session(rdb) as session:
        if (
            session.query(orm.ModelFramework)
            .filter(orm.ModelFramework.name == name)
            .count()
            == 1
        ):
            return ModelFramework.from_orm(session.query(orm.ModelFramework).get(name))
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/frameworks/{name}", **delete.fastapi_endpoint_config)
def delete_framework(name: str, rdb: Engine = Depends(request_rdb)) -> Response:
    """
    Delete framework metadata
    """
    with Session(rdb) as session:
        if (
            session.query(orm.ModelFramework)
            .filter(orm.ModelFramework.name == name)
            .count()
            == 1
        ):
            framework = session.query(orm.ModelFramework).get(name)
            session.delete(framework)
            session.commit()
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )


@router.get("/intermediates/{id}", **retrieve.fastapi_endpoint_config)
def get_intermediate(id: int, rdb: Engine = Depends(request_rdb)) -> Intermediate:
    """
    Retrieve model
    """
    if entry_exists(rdb.connect(), orm.Intermediate, id):
        with Session(rdb) as session:
            intermediate = session.query(orm.Intermediate).get(id)

    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return Intermediate.from_orm(intermediate)


@router.post("/intermediates", **create.fastapi_endpoint_config)
def create_intermediate(
    payload: Intermediate, rdb: Engine = Depends(request_rdb)
) -> Response:
    """
    Create intermediate and return its ID
    """
    with Session(rdb) as session:
        intermediate_payload = payload.dict()
        # pylint: disable-next=unused-variable
        intermediate = orm.Intermediate(**intermediate_payload)
        session.add(intermediate)
        session.commit()
        id: int = intermediate.id

    logger.info("new model created: %i", id)
    return Response(
        status_code=status.HTTP_201_CREATED,
        headers={
            "content-type": "application/json",
        },
        content=json.dumps({"id": id}),
    )


@router.delete("/intermediates/{id}", **delete.fastapi_endpoint_config)
def delete_intermediate(id: int, rdb: Engine = Depends(request_rdb)) -> Response:
    """
    Delete framework metadata
    """
    with Session(rdb) as session:
        if entry_exists(rdb.connect(), orm.Intermediate, id):
            intermediate = session.query(orm.Intermediate).get(id)
            session.delete(intermediate)
            session.commit()
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
    )


@router.get("/descriptions")
def list_model_descriptions(
    page_size: int = 100, page: int = 0, rdb: Engine = Depends(request_rdb)
) -> List[Model]:

    """
    Retrieve all models

    This will return the full list of models, even the previous ones from
    edit history.
    """
    return list_by_id(rdb.connect(), orm.ModelDescription, page_size, page)


@router.get("/descriptions/{id}", **retrieve.fastapi_endpoint_config)
def get_model_description(
    id: int, rdb: Engine = Depends(request_rdb)
) -> ModelDescription:
    """
    Retrieve model
    """
    if entry_exists(rdb.connect(), orm.ModelDescription, id):
        with Session(rdb) as session:
            model = session.query(orm.ModelDescription).get(id)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return ModelDescription.from_orm(model)


@router.get("/model_parameters/{id}", **retrieve.fastapi_endpoint_config)
def get_model_parameter(id: int, rdb: Engine = Depends(request_rdb)):
    """
    Retrieve model parameter
    """
    with Session(rdb) as session:
        if (
            session.query(orm.ModelParameter)
            .filter(orm.ModelParameter.id == id)
            .count()
            == 1
        ):
            return session.query(orm.ModelParameter).get(id)
        raise HTTPException(status_code=status.HTTP_404_NOT_F)


@router.get("/parameters/{id}", **retrieve.fastapi_endpoint_config)
def get_model_parameters(
    id: int, rdb: Engine = Depends(request_rdb)
) -> ModelParameters:
    """
    Retrieve model
    """
    if entry_exists(rdb.connect(), orm.ModelDescription, id):
        with Session(rdb) as session:
            parameters: Query[orm.ModelParameter] = session.query(
                orm.ModelParameter
            ).filter(orm.ModelParameter.model_id == id)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return orm_to_params(list(parameters))


@router.put("/parameters/{id}", **update.fastapi_endpoint_config)
def update_model_parameters(
    payload: ModelParameters, id: int, rdb: Engine = Depends(request_rdb)
) -> Response:
    """
    Update the parameters for a model
    """
    with Session(rdb) as session:
        adjust_model_params(id, payload, session)
        session.commit()
    return Response(
        status_code=status.HTTP_200_OK,
        headers={
            "content-type": "application/json",
        },
    )


@router.get("/{id}", **retrieve.fastapi_endpoint_config)
def get_model(id: int, rdb: Engine = Depends(request_rdb)) -> Model:
    """
    Retrieve model
    """
    if entry_exists(rdb.connect(), orm.ModelDescription, id):
        with Session(rdb) as session:
            model = session.query(orm.ModelDescription).get(id)
            content = session.query(orm.ModelState).get(model.state_id)
            parameters: List[orm.ModelParameter] = (
                session.query(orm.ModelParameter)
                .filter(orm.ModelParameter.model_id == id)
                .all()
            )

    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return Model.from_orm(model, content, parameters)


@router.post("", **create.fastapi_endpoint_config)
def create_model(
    payload: Model,
    rdb: Engine = Depends(request_rdb),
    graph_db=Depends(request_graph_db),
) -> Response:
    """
    Create model and return its ID
    """
    with Session(rdb) as session:
        model_payload = payload.dict()
        model_payload.pop("concept")  # TODO: Save ontology term

        content = model_payload.pop("content")
        state = orm.ModelState(content=content)
        session.add(state)
        session.commit()
        model_payload["state_id"] = state.id

        parameters = model_payload.pop("parameters")
        model_payload.pop("id")

        model = orm.ModelDescription(**model_payload)
        session.add(model)
        session.commit()
        id: int = model.id
        for param in parameters:
            session.add(
                orm.ModelParameter(
                    model_id=id,
                    name=param["name"],
                    default_value=param["default_value"],
                    type=param["type"],
                    state_variable=param.get("state_variable", False),
                )
            )
        session.commit()
        if settings.NEO4J:
            print("Neo4j is set")
            # payload={"left":model.id,"left_type":"models","right":state.id,"right_type":"states","relationship_type":"BEGINS_AT"}
            provenance_handler = ProvenanceHandler(rdb=rdb, graph_db=graph_db)
            payload = Provenance(
                left=model.id,
                left_type="model",
                right=state.id,
                right_type="model_revision",
                relation_type="BEGINS_AT",
                user_id=model_payload.get("user_id", None),
            )

            provenance_handler.create_entry(payload)
    logger.info("new model created: %i", id)
    return Response(
        status_code=status.HTTP_201_CREATED,
        headers={
            "content-type": "application/json",
        },
        content=json.dumps({"id": id}),
    )


@router.post("/opts/{model_operation}", **create.fastapi_endpoint_config)
def model_opt(
    payload: ModelOptPayload,
    model_operation: schema.ModelOperations,
    rdb: Engine = Depends(request_rdb),
    graph_db=Depends(request_graph_db),
) -> Response:
    with Session(rdb) as session:
        payload = payload.dict()
        left_model_id = payload.get("left")
        # query old model and old content
        l_model = session.query(orm.ModelDescription).get(left_model_id)
        l_framework = l_model.framework
        l_description = l_model.description
        l_name = l_model.name
        left_state_id = l_model.state_id

        if payload.get("right", False):
            right_model_id = payload.get("right")
            r_model = session.query(orm.ModelDescription).get(right_model_id)
            right_state_id = r_model.state_id

        if model_operation == "copy":
            l_content = session.query(orm.ModelState).get(left_model_id)
            l_content_dict = l_content.__dict__
            state = orm.ModelState(content=l_content_dict.get("content"))

        elif model_operation == "decompose" or model_operation == "glue":
            state = orm.ModelState(content=payload.get("content"))
        else:
            raise

        session.add(state)
        session.commit()
        new_state_id = state.id

        # add new model
        new_model = orm.ModelDescription(
            name=payload.get("name"),
            description=payload.get("description"),
            framework=payload.get("framework"),
            state_id=new_state_id,
        )
        session.add(new_model)
        session.commit()
        new_model_id = new_model.id

        # add parameters to new model. Default to left model id parameters.
        if payload.get("parameters") is None:
            parameters: List[dict] = (
                session.query(orm.ModelParameter)
                .filter(orm.ModelParameter.model_id == left_model_id)
                .all()
            )
            payload["parameters"] = []
            for parameter in parameters:
                param = parameter.__dict__
                payload["parameters"].append(param)

        # if parameters are set use those for new model
        for param in payload.get("parameters"):
            session.add(
                orm.ModelParameter(
                    model_id=new_model_id,
                    name=param.get("name"),
                    default_value=param.get("default_value"),
                    type=param.get("type"),
                    state_variable=param.get("state_variable"),
                )
            )
        session.commit()

        if settings.NEO4J:
            provenance_handler = ProvenanceHandler(rdb=rdb, graph_db=graph_db)
            prov_payload = Provenance(
                left=new_state_id,
                left_type="model_revision",
                right=left_state_id,
                right_type="model_revision",
                relation_type=model_opt_relationship_mapping[model_operation],
                user_id=payload.get("user_id", None),
            )
            provenance_handler.create_entry(prov_payload)

            if model_operation == "glue":
                prov_payload = Provenance(
                    left=new_state_id,
                    left_type="model_revision",
                    right=right_state_id,
                    right_type="model_revision",
                    relation_type=model_opt_relationship_mapping[model_operation],
                    user_id=payload.get("user_id", None),
                )
                provenance_handler.create_entry(prov_payload)

            # add begins at relationship
            prov_payload = Provenance(
                left=new_model_id,
                left_type="model",
                right=new_state_id,
                right_type="model_revision",
                relation_type="BEGINS_AT",
                user_id=payload.get("user_id", None),
            )
            provenance_handler.create_entry(prov_payload)

    logger.info("new model created: %i", id)
    return Response(
        status_code=status.HTTP_201_CREATED,
        headers={
            "content-type": "application/json",
        },
        content=json.dumps({"id": new_model_id}),
    )


# @router.post("/opts/copy", **create.fastapi_endpoint_config)
# def copy_model(
#     payload: dict,
#     rdb: Engine = Depends(request_rdb),
#     graph_db=Depends(request_graph_db),
# ) -> Response:
#     """
#     Copy model and return new model ID
#     """
#     with Session(rdb) as session:
#         old_model_id = payload.get('left')

#         # query old model and old content
#         model = session.query(orm.ModelDescription).get(old_model_id)
#         framework = model.framework
#         description = model.description
#         name = model.name
#         # set old state id so we have it
#         old_state_id = model.state_id

#         content = session.query(orm.ModelState).get(model.state_id)
#         # take off content id so we can save it again in the database with new id
#         content_payload = content.__dict__
#         state = orm.ModelState(content=content_payload.get("content"))
#         session.add(state)
#         session.commit()

#         new_state_id = state.id
#         model = session.query(orm.ModelDescription).get(old_model_id)

#         new_model = orm.ModelDescription(
#             name=payload.get("name", name),
#             description=payload.get("description", description),
#             framework=framework,
#             state_id=new_state_id,
#         )
#         session.add(new_model)
#         session.commit()
#         new_model_id = new_model.id

#         parameters: List[orm.ModelParameter] = (
#             session.query(orm.ModelParameter)
#             .filter(orm.ModelParameter.model_id == old_model_id)
#             .all()
#         )

#         # set the parameters as the same for copied model
#         for param in parameters:
#             session.add(
#                 orm.ModelParameter(
#                     model_id=new_model_id,
#                     name=param.name,
#                     default_value=param.default_value,
#                     type=param.type,
#                     state_variable=param.state_variable,
#                 )
#             )
#         session.commit()

#         if settings.NEO4J:
#             provenance_handler = ProvenanceHandler(rdb=rdb, graph_db=graph_db)
#             prov_payload = Provenance(
#                 left=new_state_id,
#                 left_type="model_revision",
#                 right=old_state_id,
#                 right_type="model_revision",
#                 relation_type="COPIED_FROM",
#                 user_id=payload.get("user_id", None),
#             )
#             provenance_handler.create_entry(prov_payload)

#             prov_payload = Provenance(
#                 left=new_model_id,
#                 left_type="model",
#                 right=new_state_id,
#                 right_type="model_revision",
#                 relation_type="BEGINS_AT",
#                 user_id=payload.get("user_id", None),
#             )
#             provenance_handler.create_entry(prov_payload)

#     logger.info("new model created: %i", id)
#     return Response(
#         status_code=status.HTTP_201_CREATED,
#         headers={
#             "content-type": "application/json",
#         },
#         content=json.dumps({"id": new_model_id}),
#     )


# @router.post("/opts/decompose", **create.fastapi_endpoint_config)
# def decompose_model(
#     payload: dict,
#     rdb: Engine = Depends(request_rdb),
#     graph_db=Depends(request_graph_db),
# ) -> Response:
#     """
#     Decompose model and return new model ID
#     """
#     with Session(rdb) as session:
#         old_model_id = payload.get('left')

#         # query old model info and old content id
#         model = session.query(orm.ModelDescription).get(old_model_id)
#         framework = model.framework
#         description = model.description
#         name = model.name
#         old_state_id = model.state_id

#         # create new content node for new model
#         state = orm.ModelState(content=payload.get('content'))
#         session.add(state)
#         session.commit()

#         new_state_id = state.id

#         new_model = orm.ModelDescription(
#             name=payload.get("name", name),
#             description=payload.get("description", description),
#             framework=payload.get("framework", framework),
#             state_id=new_state_id,
#         )
#         session.add(new_model)
#         session.commit()
#         new_model_id = new_model.id

#         # if parameters are not set assume they use the same as the old model? maybe not a good idea
#         parameters: List[orm.ModelParameter] = (
#             session.query(orm.ModelParameter)
#             .filter(orm.ModelParameter.model_id == old_model_id)
#             .all()
#         )

#         # set the parameters as the same for copied model
#         for param in payload.get("parameters", parameters):
#             session.add(
#                 orm.ModelParameter(
#                     model_id=new_model_id,
#                     name=param.name,
#                     default_value=param.default_value,
#                     type=param.type,
#                     state_variable=param.state_variable,
#                 )
#             )
#         session.commit()

#         if settings.NEO4J:
#             provenance_handler = ProvenanceHandler(rdb=rdb, graph_db=graph_db)
#             prov_payload = Provenance(
#                 left=old_state_id,
#                 left_type="model_revision",
#                 right=new_state_id,
#                 right_type="model_revision",
#                 relation_type="DECOMPOSED_FROM",
#                 user_id=payload.get("user_id", None),
#             )
#             provenance_handler.create_entry(prov_payload)

#             prov_payload = Provenance(
#                 left=new_model_id,
#                 left_type="model",
#                 right=new_state_id,
#                 right_type="model_revision",
#                 relation_type="BEGINS_AT",
#                 user_id=payload.get("user_id", None),
#             )
#             provenance_handler.create_entry(prov_payload)

#     logger.info("new model created: %i", id)
#     return Response(
#         status_code=status.HTTP_201_CREATED,
#         headers={
#             "content-type": "application/json",
#         },
#         content=json.dumps({"id": new_model_id}),
#     )

# @router.post("/opts/glue", **create.fastapi_endpoint_config)
# def glue_models(
#     payload: dict,
#     id: int,
#     rdb: Engine = Depends(request_rdb),
#     graph_db=Depends(request_graph_db),
# ) -> Response:
#     """
#     Decompose model and return new model ID
#     """
#     with Session(rdb) as session:
#         left_id = payload.get('left')
#         right_id = payload.get('right')

#         # query left model info and old content id
#         model = session.query(orm.ModelDescription).get(left_id)
#         left_state_id = model.state_id

#         # query right model info and right content id
#         r_model = session.query(orm.ModelDescription).get(right_id)
#         right_state_id = r_model.state_id

#         # create new content node for new model
#         state = orm.ModelState(content=payload.get('content'))
#         session.add(state)
#         session.commit()

#         new_state_id = state.id

#         new_model = orm.ModelDescription(
#             name=payload.get("name"),
#             description=payload.get("description"),
#             framework=payload.get("framework"),
#             state_id=new_state_id,
#         )
#         session.add(new_model)
#         session.commit()
#         new_model_id = new_model.id

#         # if parameters are not set assume they use the same as the old model? maybe not a good idea
#         parameters: List[orm.ModelParameter] = (
#             session.query(orm.ModelParameter)
#             .filter(orm.ModelParameter.model_id == left_id)
#             .all()
#         )

#         # set the parameters as the same for copied model
#         for param in payload.get("parameters", parameters):
#             session.add(
#                 orm.ModelParameter(
#                     model_id=new_model_id,
#                     name=param.name,
#                     default_value=param.default_value,
#                     type=param.type,
#                     state_variable=param.state_variable,
#                 )
#             )
#         session.commit()

#         if settings.NEO4J:
#             provenance_handler = ProvenanceHandler(rdb=rdb, graph_db=graph_db)
#             prov_payload = Provenance(
#                 left=left_state_id,
#                 left_type="model_revision",
#                 right=new_state_id,
#                 right_type="model_revision",
#                 relation_type="GLUED_FROM",
#                 user_id=payload.get("user_id", None),
#             )
#             provenance_handler.create_entry(prov_payload)
#             prov_payload = Provenance(
#                 left=right_state_id,
#                 left_type="model_revision",
#                 right=new_state_id,
#                 right_type="model_revision",
#                 relation_type="GLUED_FROM",
#                 user_id=payload.get("user_id", None),
#             )
#             provenance_handler.create_entry(prov_payload)


#             prov_payload = Provenance(
#                 left=new_model_id,
#                 left_type="model",
#                 right=new_state_id,
#                 right_type="model_revision",
#                 relation_type="BEGINS_AT",
#                 user_id=payload.get("user_id", None),
#             )
#             provenance_handler.create_entry(prov_payload)

#     logger.info("new model created: %i", id)
#     return Response(
#         status_code=status.HTTP_201_CREATED,
#         headers={
#             "content-type": "application/json",
#         },
#         content=json.dumps({"id": new_model_id}),
#     )


@router.post("/{id}", **update.fastapi_endpoint_config)
def update_model(
    payload: Model,
    id: int,
    rdb: Engine = Depends(request_rdb),
    graph_db=Depends(request_graph_db),
) -> Response:
    """
    Update model content
    """
    # TODO: reinclude `provenance_handler = ProvenanceHandler(rdb, graph_db)`
    if entry_exists(rdb.connect(), orm.ModelDescription, id):
        model_payload = payload.dict()
        content = model_payload.pop("content")
        model_payload.pop("parameters")
        with Session(rdb) as session:
            state = orm.ModelState(content=content)
            session.add(state)
            session.commit()

            model = session.query(orm.ModelDescription).get(id)

            old_state = model.state_id

            model.state_id = state.id
            model.name = model_payload["name"]
            model.description = model_payload["description"]
            model.framework = model_payload["framework"]
            model.state_id = state.id
            session.commit()
            if settings.NEO4J:
                provenance_handler = ProvenanceHandler(rdb=rdb, graph_db=graph_db)

                payload = Provenance(
                    left=state.id,
                    left_type="model_revision",
                    right=old_state,
                    right_type="model_revision",
                    relation_type="EDITED_FROM",
                    user_id=model_payload.get("user_id", None),
                )
                provenance_handler.create_entry(payload)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return Response(
        status_code=status.HTTP_200_OK,
        headers={
            "content-type": "application/json",
        },
        content=json.dumps({"id": id}),
    )
