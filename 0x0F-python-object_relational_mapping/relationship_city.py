#!/usr/bin/python3
"""'City' class definition and an instance.
"""
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from relationship_state import Base


class City(Base):
    """The 'cities' class definition. (SQLAlchemy ORM)

    Attributes:
        id: Column integer (index, primary key)
        name: Column string max 128 (state name)
    """
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True,
                nullable=False, unique=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
