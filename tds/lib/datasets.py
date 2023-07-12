"""
Qualifer specific logic
"""

import json
from logging import Logger

from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Session

from tds.autogen import schema
from tds.modules.dataset.model import QualifierXref

logger = Logger(__file__)


def get_qualifier_xrefs(count: int, rdb: Engine):
    """
    Get a specified number of qualifier xrefs
    """
    with Session(rdb) as session:
        result = (
            session.query(QualifierXref).order_by(QualifierXref.id.asc()).limit(count)
        )
        result = result[::]
        return result


def get_qualifier_xref(id: int, rdb: Engine) -> str:
    """
    Get a specific qualifier xref by ID
    """
    with Session(rdb) as session:
        result = session.query(QualifierXref).get(id)
        return result


def create_qualifier_xref(payload: schema.QualifierXref, rdb: Engine):
    """
    Create a qualifier xref
    """
    with Session(rdb) as session:
        qualifier_xrefp = {}
        try:
            qualifier_xrefp = payload.dict()
        except AttributeError as error:
            logger.error(error)
            qualifier_xrefp = payload
            logger.info("Set qualifier_xref to raw payload.")
        del qualifier_xrefp["id"]
        qualifier_xref = QualifierXref(**qualifier_xrefp)
        exists = (
            session.query(QualifierXref).filter_by(**qualifier_xrefp).first()
            is not None
        )
        if exists:
            return "Qualifier Xref already exists."
        session.add(qualifier_xref)
        session.commit()
        data_id = qualifier_xref.id
        qualifier_xrefp["id"] = data_id
        return json.dumps(qualifier_xrefp)


def update_qualifier_xref(payload: schema.Qualifier, id: int, rdb: Engine) -> str:
    """
    Update a qualifier xref by ID
    """
    with Session(rdb) as session:
        data_payload = payload.dict(exclude_unset=True)
        data_payload["id"] = id
        logger.info(data_payload)

        data_to_update = session.query(QualifierXref).filter(QualifierXref.id == id)
        data_to_update.update(data_payload)
        session.commit()
    return "Updated Qualifier xref"


def delete_qualifier_xref(id: int, rdb: Engine) -> str:
    """
    Delete a qualifier xref by ID
    """
    with Session(rdb) as session:
        session.query(QualifierXref).filter(QualifierXref.id == id).delete()
        session.commit()
