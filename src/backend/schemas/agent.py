import datetime
from typing import Optional

from pydantic import BaseModel

from backend.database_models.agent import AgentDeployment, AgentModel


class AgentBase(BaseModel):
    user_id: str


class Agent(AgentBase):
    id: str
    created_at: datetime.datetime
    updated_at: datetime.datetime

    version: int
    name: str
    description: Optional[str]
    preamble: Optional[str]
    temperature: float
    # tools: List[Tool]

    model: AgentModel
    deployment: AgentDeployment

    class Config:
        from_attributes = True
        use_enum_values = True


class CreateAgent(BaseModel):
    name: str
    version: Optional[int] = None
    description: Optional[str] = None
    preamble: Optional[str] = None
    temperature: Optional[float] = None
    model: AgentModel
    deployment: AgentDeployment

    class Config:
        from_attributes = True
        use_enum_values = True


class UpdateAgent(BaseModel):
    name: Optional[str] = None
    version: Optional[int] = None
    description: Optional[str] = None
    preamble: Optional[str] = None
    temperature: Optional[float] = None
    model: Optional[AgentModel] = None
    deployment: Optional[AgentDeployment] = None
    # tools: Optional[List[Tool]] = None

    class Config:
        from_attributes = True
        use_enum_values = True


class DeleteAgent(BaseModel):
    pass
