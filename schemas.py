from pydantic import BaseModel, ConfigDict

class TaskAddModel(BaseModel):
    name: str
    description: str | None = None

class TaskAddResponse(BaseModel):
    ok: bool
    task_id: int

class TaskModel(TaskAddModel):
    id: int

    model_config = ConfigDict(from_attributes=True)

