#!/usr/bin/python3
"""Adds the State object “Louisiana” to the database.

Here we use Session as interface to the database.

Args:
    user (str): mysql username
    pass (str): mysql password
    database (str): mysql database name
"""
import sys
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from relationship_state import State, Base
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = Session(engine)

    insert = State(name='California', cities=[City(name='San Francisco')])
    session.add(insert)
    session.commit()
    session.close()
