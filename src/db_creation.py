import asyncio
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from models.models import metadata
from config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

DATABASE_URL_sync = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine_s = create_engine(DATABASE_URL_sync)

DATABASE_URL_ = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine_a = create_async_engine(DATABASE_URL_)



async def create_models():
    async with engine_a.begin() as conn:
        await conn.run_sync(metadata.drop_all)
        await conn.run_sync(metadata.create_all)


# asyncio.run(create_models())

def create_models_sync():
    metadata.drop_all(engine_s)
    metadata.create_all(engine_s)

create_models_sync()


