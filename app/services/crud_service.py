from app.database.connection import async_session
from sqlalchemy.future import select
from sqlalchemy import delete, update


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

    async def create(self, payload: any):
        async with async_session() as session:
            session.add(self.model(**payload.__dict__))
            await session.commit()

    async def delete(self, id: int):
        async with async_session() as session:
            await session.execute(delete(self.model).where(self.model.id == id))
            await session.commit()

    async def update(self, id: int, payload: any):
        async with async_session() as session:
            await session.execute(
                update(self.model).where(self.model.id == id).values(**payload.__dict__)
            )
            await session.commit()
