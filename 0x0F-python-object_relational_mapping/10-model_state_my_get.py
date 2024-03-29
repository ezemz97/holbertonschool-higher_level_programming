#!/usr/bin/python3
"""Search for a specific state from db (ORM)

Here we use Session as interface to the database.

Args:
    user (str): mysql username
    pass (str): mysql password
    database (str): mysql database name
    statename (str): state name to search
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
    query = session.query(State).order_by(State.id)\
                   .filter(State.name == sys.argv[4]).all()
    if query:
        for state in query:
            print("{}".format(state.id))
            # print(row.name)
    else:
        print("Not found")
    session.close()
