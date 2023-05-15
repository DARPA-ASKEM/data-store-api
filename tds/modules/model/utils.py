from typing import List

import pandas as pd
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Query, Session

from tds.autogen import orm
from tds.db.relational import engine as pg_engine


def orm_to_params(parameters: List):
    """
    Convert SQL parameter search to dict
    """
    return [
        {
            "id": param.id,
            "name": param.name,
            "type": jsonable_encoder(param.type),
            "default_value": param.default_value,
            "state_variable": param.state_variable,
        }
        for param in parameters
    ]


def model_response(model_from_es, delete_fields=[]) -> dict:
    """
    Function builds model response object from an ElasticSearch model.
    """
    es_response = model_from_es.body
    model = es_response["_source"]
    model["state_id"] = model["id"] = es_response["_id"]
    frameworks = get_frameworks()
    model["framework"] = frameworks[model["model_schema"]]
    model["schema"] = model["model_schema"]

    del model["model_schema"]
    del model["concepts"]

    if delete_fields:
        for field in delete_fields:
            del model[field]

    return model


def model_list_response(model_list_from_es) -> list:
    """
    Function builds model response object from an ElasticSearch model.
    """
    df = pd.DataFrame(model_list_from_es)
    framework_map = get_frameworks()
    # We need to get the fields and then merge back to make the id available.
    models = (
        pd.concat({i: pd.DataFrame(x) for i, x in df.pop("fields").items()})
        .reset_index(level=1, drop=True)
        .join(df)
        .reset_index(drop=True)
    )

    models["framework"] = models["model_schema"].map(lambda x: framework_map[x])
    models.rename(columns={"_id": "id"}, inplace=True)
    models.drop(columns=["_index", "_ignored", "_score"], inplace=True)

    return models.to_json(orient="records")


def get_frameworks() -> dict:
    with Session(pg_engine) as pg_db:
        frameworks = pg_db.query(orm.ModelFramework).all()
        framework_map = {}
        for f in frameworks:
            framework_map[f.schema_url] = f.name
    return framework_map