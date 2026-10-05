from fastapi import APIRouter

from src.home.router import home_router
from src.tasks.router import tasks_router

main_router = APIRouter()

main_router.include_router(home_router)
main_router.include_router(tasks_router)
