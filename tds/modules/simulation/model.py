"""
TDS Simulation Data Model Definition.
"""
from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from tds.autogen.enums import SimulationEngine, SimulationStatus, SimulationType
from tds.db.base import TdsModel
from tds.settings import settings


class Simulation(TdsModel):
    """
    Simulation Data Model
    """

    id: str
    name: Optional[str]
    description: Optional[str]

    _index = "simulation"
    engine: SimulationEngine
    type: SimulationType
    status: Optional[SimulationStatus] = Field(default="queued")
    reason: Optional[str]
    execution_payload: dict
    start_time: Optional[datetime]
    completed_time: Optional[datetime]
    workflow_id: str
    user_id: Optional[int]
    project_id: Optional[int]
    result_files: Optional[List[str]] = []

    def save(self):
        """
        Method saves the object to ElasticSearch.
        """
        res = super().save()
        # self._extract_concepts()
        if settings.NEO4J_ENABLED:
            self._establish_provenance()
        return res

    def _extract_concepts(self, simulation_id):
        pass

    def _establish_provenance(self):
        pass

    class Config:
        """
        Simulation Data Model Swagger Example
        """

        schema_extra = {
            "example": {
                "id": "str",
                "execution_payload": {},
                "result_files": [],
                "type": "ensemble|simulation|calibration",
                "status": "queued|running|complete|error|cancelled|failed",
                "reason": "Only filled if simulation failed.",
                "start_time": "timestamp",
                "completed_time": "timestamp",
                "engine": "ciemss|julia",
                "workflow_id": "str",
                "user_id": "int",
                "project_id": "int",
            }
        }
