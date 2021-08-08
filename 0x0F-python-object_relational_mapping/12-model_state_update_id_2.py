#!/usr/bin/python3
"""Update the State(id 2) object to "New Mexico".

Here we use Session as interface to the database.

Args:
    user (str): mysql username
    pass (str): mysql password
    database (str): mysql database name
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    (session.query(State).get(2)).name = "New Mexico"
    session.commit()
    session.close()
