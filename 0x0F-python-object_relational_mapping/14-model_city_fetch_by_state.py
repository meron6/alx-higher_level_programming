#!/usr/bin/python3
"""
fecth all cities with their state
"""
from model_state import Base, State
from model_city import City
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

            cities = session.query(City.name.label("city_name"),
                                   City.id.label("city_id"),
                                   State.name.label("state_name")) \
                            .join(State, City.state_id == State.id) \
                            .order_by(asc(City.id)) \
                            .all()

            for city in cities:
                print("{}: ({}) {}".format(city.state_name,
                                           city.city_id,
                                           city.city_name))

        except:
            print("something wrong with the query")
