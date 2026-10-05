from typing import Annotated
from fastapi import APIRouter, Body

from src.tasks.service import TaskService
from src.tasks.schemas import TaskAdd, Task, TaskAddResponse

tasks_router = APIRouter(
    prefix = "/tasks",
    tags = ["Tasks"]
)

@tasks_router.post("")
async def add_task(
    task: Annotated[TaskAdd, Body()],
) -> TaskAddResponse:
    task_id = await TaskService.add_one(task)

    return TaskAddResponse(
        ok = True,
        task_id = task_id,
    )

@tasks_router.get("")
async def get_all_tasks() -> list[Task]:
    tasks = await TaskService.find_all()
    
    return tasks

@tasks_router.get("/{id}")
async def get_task_by_id(id: int) -> Task:
    task = await TaskService.find_by_id(id)
    
    return task
