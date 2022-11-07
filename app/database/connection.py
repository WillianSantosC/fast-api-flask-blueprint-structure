from os import getenv

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = getenv('DATABASE_URL')

engine = create_async_engine(DATABASE_URL)
async_session = sessionmaker(engine, AsyncSession)

Base = declarative_base()
