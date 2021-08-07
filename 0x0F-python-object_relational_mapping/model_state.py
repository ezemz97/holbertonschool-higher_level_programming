#!/usr/bin/python3
"""'State' class definition and an instance.
"""
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """The 'state' class definition. (SQLAlchemy ORM)

    Attributes:
        id: Column integer (index, primary key)
        name: Column string max 128 (state name)
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
