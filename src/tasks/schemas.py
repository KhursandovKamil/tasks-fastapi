from typing import Annotated
from pydantic import BaseModel, ConfigDict, Field

class TaskAdd(BaseModel):
    name: str
    description: str | None = Field(max_length=500, default=None)

class TaskAddResponse(BaseModel):
    ok: bool
    task_id: int = Field(gt=0)

class Task(TaskAdd):
    id: int = Field(gt=0)

    model_config = ConfigDict(from_attributes=True)
