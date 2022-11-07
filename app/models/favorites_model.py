from sqlalchemy import Column, Integer, String
from app.database.connection import Base


class Favorite(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String)
    value = Column(Integer)
