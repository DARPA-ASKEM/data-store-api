from enum import Enum
import datetime
from typing import Optional
from pydantic import BaseModel, Json


class ResourceType(str, Enum):

    dataset = 'dataset'
    extracted_data = 'extracted_data'
    intermediate = 'intermediate'
    model = 'model'
    plan = 'plan'
    publication = 'publication'
    

class RelationType(str, Enum):

    cites = 'cites'
    copiedfrom = 'copiedfrom'
    derivedfrom = 'derivedfrom'
    editedFrom = 'editedFrom'
    gluedFrom = 'gluedFrom'
    stratifiedFrom = 'stratifiedFrom'
    

class TaggableType(str, Enum):

    dataset = 'dataset'
    feature = 'feature'
    model = 'model'
    project = 'project'
    simulation_plan = 'simulation_plan'
    

class FeatureValueType(str, Enum):

    binary = 'binary'
    bool = 'bool'
    float = 'float'
    int = 'int'
    str = 'str'
    

class OntologicalField(str, Enum):

    obj = 'obj'
    unit = 'unit'
    

class IntermediateSource(str, Enum):

    mrepresentationa = 'mrepresentationa'
    skema = 'skema'
    

class IntermediateFormat(str, Enum):

    bilayer = 'bilayer'
    gromet = 'gromet'
    other = 'other'
    sbml = 'sbml'
    

class Role(str, Enum):

    author = 'author'
    contributor = 'contributor'
    maintainer = 'maintainer'
    other = 'other'
    

class ExtractedType(str, Enum):

    equation = 'equation'
    figure = 'figure'
    table = 'table'
    

class Direction(str, Enum):

    input = 'input'
    output = 'output'
    

class QualifierXref(BaseModel):

    id: Optional[int] = None
    qualifier_id: Optional[int] = None
    feature_id: Optional[int] = None


class ModelRuntime(BaseModel):

    id: Optional[int] = None
    timestamp: datetime.datetime = datetime.datetime.now()
    name: str
    left: int
    right: int


class AppliedModel(BaseModel):

    id: Optional[int] = None
    model_id: Optional[int] = None
    plan_id: Optional[int] = None


class SimulationMaterial(BaseModel):

    id: Optional[int] = None
    run_id: Optional[int] = None
    dataset_id: Optional[int] = None
    type: Optional[Direction]


class Dataset(BaseModel):

    id: Optional[int] = None
    name: str
    url: str
    description: str
    timestamp: datetime.datetime = datetime.datetime.now()
    deprecated: Optional[bool]
    sensitivity: Optional[str]
    quality: Optional[str]
    temporal_resolution: Optional[str]
    geospatial_resolution: Optional[str]
    annotations: Optional[Json]
    maintainer: int


class Feature(BaseModel):

    id: Optional[int] = None
    dataset_id: Optional[int] = None
    description: Optional[str]
    display_name: Optional[str]
    name: str
    value_type: FeatureValueType


class Qualifier(BaseModel):

    id: Optional[int] = None
    dataset_id: Optional[int] = None
    description: Optional[str]
    name: str
    value_type: FeatureValueType


class Model(BaseModel):

    id: Optional[int] = None
    name: str
    description: Optional[str]
    framework_id: Optional[int] = None
    timestamp: datetime.datetime = datetime.datetime.now()
    content: Optional[Json]


class SimulationRun(BaseModel):

    id: Optional[int] = None
    simulator_id: Optional[int] = None
    timestamp: datetime.datetime = datetime.datetime.now()
    completed_at: Optional[datetime.datetime]
    success: Optional[bool] = True
    response: Optional[bytes]


class ModelParameter(BaseModel):

    id: Optional[int] = None
    run_id: Optional[int] = None
    name: str
    value: str
    value_type: str


class ExtractedData(BaseModel):

    id: Optional[int] = None
    publication_id: Optional[int] = None
    type: ExtractedType
    data: bytes
    img: bytes


class ProjectAsset(BaseModel):

    id: Optional[int] = None
    project_id: Optional[int] = None
    resource_id: Optional[int] = None
    resource_type: ResourceType
    external_ref: Optional[str]


class Provenance(BaseModel):

    id: Optional[int] = None
    timestamp: datetime.datetime = datetime.datetime.now()
    relation_type: RelationType
    left: int
    left_type: ResourceType
    right: int
    right_type: ResourceType
    user_id: Optional[int]


class Association(BaseModel):

    id: Optional[int] = None
    person_id: Optional[int] = None
    resource_id: Optional[int] = None
    resource_type: Optional[ResourceType]
    role: Optional[Role]


class ModelingFramework(BaseModel):

    id: Optional[int] = None
    version: str
    name: str
    semantics: Json


class Intermediate(BaseModel):

    id: Optional[int] = None
    timestamp: datetime.datetime = datetime.datetime.now()
    source: IntermediateSource
    type: IntermediateFormat
    representation: bytes


class Software(BaseModel):

    id: Optional[int] = None
    timestamp: datetime.datetime = datetime.datetime.now()
    source: str
    storage_uri: str


class SimulationPlan(BaseModel):

    id: Optional[int] = None
    simulator: str
    query: str
    body: Json


class Publication(BaseModel):

    id: Optional[int] = None
    xdd_uri: str


class Project(BaseModel):

    id: Optional[int] = None
    name: str
    description: str
    timestamp: Optional[datetime.datetime] = datetime.datetime.now()
    status: str


class OntologyConcept(BaseModel):

    id: Optional[int] = None
    term_id: str
    type: TaggableType
    obj_id: Optional[int] = None
    status: OntologicalField


class Person(BaseModel):

    id: Optional[int] = None
    name: str
    email: str
    org: Optional[str]
    website: Optional[str]
    is_registered: bool
