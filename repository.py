from sqlalchemy.sql import select

from database import new_session, TaskOrm
from schemas import TaskAddModel, TaskModel

class TaskRepository:
    @classmethod
    async def add_one(cls, data: TaskAddModel) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()
            task = TaskOrm(**task_dict)

            session.add(task)

            await session.flush()
            await session.commit()

            return task.id

    @classmethod
    async def find_all(cls) -> list[TaskModel]:
        async with new_session() as session:
            query = select(TaskOrm)

            result = await session.execute(query)

            task_models = result.scalars().all()
            tasks_schemas = [TaskModel.model_validate(task_orm) for task_orm in task_models]

            return tasks_schemas
