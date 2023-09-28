from os import getenv

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = f"postgresql+asyncpg://{getenv('PG_USER')}:{getenv('PG_PASS')}@{getenv('DB_HOST')}:{getenv('DB_PORT')}/{getenv('PG_DB')}"

engine = create_async_engine(DATABASE_URL)
async_session = sessionmaker(engine, class_=AsyncSession)  # type: ignore

Base = declarative_base()
