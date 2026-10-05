from sqlalchemy.orm import Mapped

from src.database import BaseOrm

class TaskOrm(BaseOrm):
    __tablename__ = "tasks"

    name: Mapped[str]
    description: Mapped[str | None]
