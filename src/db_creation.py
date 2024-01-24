import asyncio
from models.models import metadata
from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER
from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL_ = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine_ = create_async_engine(DATABASE_URL_)


async def create_models():
    async with engine_.begin() as conn:
        await conn.run_sync(metadata.drop_all)
        await conn.run_sync(metadata.create_all)


asyncio.run(create_models())
