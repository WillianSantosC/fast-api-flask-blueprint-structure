from typing import Any, List

from sqlalchemy import delete, insert, update
from sqlalchemy.future import select

from app.database.connection import async_session


class CrudService:
    def __init__(self, model) -> None:
        self.model = model

    async def find_all(self):
        async with async_session() as session:
            result = await session.execute(select(self.model))
            return result.scalars().all()

    async def find_one(self, id: int):
        async with async_session() as session:
            result = await session.execute(
                select(self.model).where(self.model.id == id)
            )
            return result.scalar()

    async def create(self, payload: Any):
        async with async_session() as session:
            session.add(self.model(**payload))
            await session.commit()

    async def bulk_create(self, payload: List[object]):
        async with async_session() as session:
            await session.execute(insert(self.model).values(payload))
            await session.commit()

    async def update(self, id: int, payload: Any):
        async with async_session() as session:
            await session.execute(
                update(self.model).where(self.model.id == id).values(**payload)
            )
            await session.commit()

    async def bulk_update(self, payload: List[object]):
        async with async_session() as session:
            await session.execute(update(self.model), payload)
            await session.commit()

    async def delete(self, id: int):
        async with async_session() as session:
            await session.execute(delete(self.model).where(self.model.id == id))
            await session.commit()

    async def delete_all(self):
        async with async_session() as session:
            await session.execute(delete(self.model))
            await session.commit()
