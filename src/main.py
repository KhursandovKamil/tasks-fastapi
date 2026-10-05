from typing import Annotated

from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.database import create_tables, delete_tables
from src.api import main_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("The db is cleaned")

    await create_tables()
    print("The db is ready.")

    yield
    print("Turned off")

app = FastAPI(lifespan = lifespan)

app.include_router(main_router)
