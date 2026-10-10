from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

db_engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db"
)

new_session = async_sessionmaker(db_engine, expire_on_commit=False)

class BaseOrm(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

async def create_tables():
    async with db_engine.begin() as conn:
        await conn.run_sync(BaseOrm.metadata.create_all)

async def delete_tables():
    async with db_engine.begin() as conn:
        await conn.run_sync(BaseOrm.metadata.drop_all)
