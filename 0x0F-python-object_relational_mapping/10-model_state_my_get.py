#!/usr/bin/python3
"""
list the id of the state if exists
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    if len(sys.argv) == 5:
        try:
            engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                                   .format(sys.argv[1], sys.argv[2],
                                           sys.argv[3]), pool_pre_ping=True)

            state = sys.argv[4]

            Session = sessionmaker(bind=engine)

            session = Session()

            state_id = session.query(State.id) \
                              .filter(State.name == state) \
                              .all()

            if state_id:
                print(state_id[0][0])
            else:
                print("Not found")

        except:
            print("something wrong with the query")
