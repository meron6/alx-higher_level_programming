#!/usr/bin/python3
"""Fetch all State objects from the database hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            sys.argv[1], sys.argv[2], sys.argv[3]))

    # Bind engine to Base class metadata
    Base.metadata.bind = engine

    # Create a session maker instance
    DBSession = sessionmaker(bind=engine)

    # Create session
    session = DBSession()

    # Query all State objects and sort them by id
    states = session.query(State).order_by(State.id).all()

    # Print the results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
