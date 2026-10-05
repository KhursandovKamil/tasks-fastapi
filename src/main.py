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

app = FastAPI(
    lifespan = lifespan,
    description="Welcome to Tasks API documentation! Here you will able to discover all of the ways you can interact with the Tasks API.",
    root_path="/api/v1",
    docs_url=None,
    openapi_url="/docs/openapi.json",
    redoc_url="/docs",
)

app.include_router(main_router)
