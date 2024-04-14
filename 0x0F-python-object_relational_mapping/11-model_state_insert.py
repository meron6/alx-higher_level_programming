#!/usr/bin/python3
"""
adds a state to the database
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

            louisiana = State("Louisiana")

            session.add(louisiana)

            session.commit()

            louisiana_id = session.query(State.id) \
                                  .filter(State.name == "Louisiana") \
                                  .all()

            if louisiana_id:
                print("{}".format(louisiana_id[0][0]))

        except:
            print("something wrong with the query")

        finally:
            session.close()
