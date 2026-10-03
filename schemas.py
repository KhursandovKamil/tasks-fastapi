from pydantic import BaseModel

class TaskAddModel(BaseModel):
    name: str
    description: str | None

class TaskAddResponse(BaseModel):
    ok: bool
    task_id: int

class TaskModel(TaskAddModel):
    id: int

