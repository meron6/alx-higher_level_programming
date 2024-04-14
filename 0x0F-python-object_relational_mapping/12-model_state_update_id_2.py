#!/usr/bin/python3
"""
change state name
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
            Base.metadata.create_all(engine)

            Session = sessionmaker(bind=engine)
            session = Session()

            session.query(State) \
                   .filter(State.id == 2) \
                   .update({'name': 'New Mexico'}, synchronize_session=False)
            session.commit()

        except:
            print("something wrong with the query")

        finally:
            session.close()
