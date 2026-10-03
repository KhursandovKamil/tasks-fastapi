from typing import Annotated

from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("The db is cleaned")

    await create_tables()
    print("The db is ready.")

    yield
    print("Turned off")

app = FastAPI(lifespan = lifespan)

app.include_router(tasks_router)
