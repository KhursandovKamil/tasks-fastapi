from fastapi import HTTPException
from sqlalchemy.sql import select

from src.database import new_session
from src.tasks.models import TaskOrm
from src.tasks.schemas import Task, TaskAdd


class TaskService:
    @classmethod
    async def add_one(cls, data: TaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()
            task = TaskOrm(**task_dict)

            session.add(task)

            await session.flush()
            await session.commit()

            return task.id

    @classmethod
    async def find_all(cls) -> list[Task]:
        async with new_session() as session:
            query = select(TaskOrm)

            result = await session.execute(query)

            task_orms = result.scalars().all()
            tasks = [Task.model_validate(task_orm) for task_orm in task_orms]

            return tasks

    @classmethod
    async def find_by_id(cls, id: int) -> Task:
        async with new_session() as session:
            query = select(TaskOrm).where(TaskOrm.id == id)

            result = await session.execute(query)
            task_orm = result.scalars().first()

            if task_orm:
                return Task.model_validate(task_orm)

            raise HTTPException(status_code=404, detail="The task is not found")
