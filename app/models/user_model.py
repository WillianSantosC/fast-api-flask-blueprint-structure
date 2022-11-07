from sqlalchemy import Column, Integer, String
from app.database.connection import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
