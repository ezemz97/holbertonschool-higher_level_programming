#!/usr/bin/python3
"""List all State objects containing "a" from db (ORM)

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
    for state in session.query(State).order_by(State.id)\
                        .filter(State.name.like("%a%")):
                        # Checker won't like, but it works:
                        # .filter("a" in str(State.name)
        print("{}: {}".format(state.id, state.name))
    session.close()
