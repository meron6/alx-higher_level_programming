#!/usr/bin/python3
"""
list first state in table by id
"""
from model_state import Base, State
from sqlalchemy import create_engine
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

            firstState = session.query(State).first()

            if firstState:
                print("{}: {}".format(firstState.id, firstState.name))
            else:
                print("Nothing")

        except:
            print("something wrong with sqlalchemy query")
