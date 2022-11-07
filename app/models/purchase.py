from sqlalchemy import Column, Integer
from app.database.connection import Base
from .mixins import Timestamp


class Purchase(Timestamp, Base):
    __tablename__ = "purchase"

    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Integer)
