#!/usr/bin/python3
"""Script that creates the State “California” with the City “San Francisco”
   from the database hbtn_0e_100_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Create the SQLAlchemy engine using the provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a session factory
    Session = sessionmaker(bind=engine)

    # Create a session object
    session = Session()

    # Create California state
    california = State(name="California")
    # Create San Francisco city
    san_francisco = City(name="San Francisco", state=california)
    # Add the city to the state's cities
    california.cities.append(san_francisco)

    # Add the state to the session
    session.add(california)

    # Commit the session to persist the changes
    session.commit()

    # Close the session
    session.close()
