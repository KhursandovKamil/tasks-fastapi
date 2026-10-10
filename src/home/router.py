from fastapi import APIRouter

from src.home.service import HomeService

home_router = APIRouter(
    prefix = "",
    tags = ["Home"]
)

@home_router.get("/")
async def home() -> str:
    return HomeService.it_works()
