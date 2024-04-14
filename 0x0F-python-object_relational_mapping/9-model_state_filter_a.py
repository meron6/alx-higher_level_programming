#!/usr/bin/python3
"""
list all states with the letter a in their names
"""

from model_state import Base, State
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    if len(sys.argv) == 4:
        try:
            engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                   .format(sys.argv[1], sys.argv[2],
                                           sys.argv[3]), pool_pre_ping=True)
            Session = sessionmaker(bind=engine)

            session = Session()

            astates = session.query(State) \
                             .filter(State.name.ilike('%a%')) \
                             .order_by(asc(State.id)) \
                             .all()

            for state in astates:
                print("{}: {}".format(state.id, state.name))
        except:
            print("something wrong with the query")
