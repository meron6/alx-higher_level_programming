#!/usr/bin/python3
"""
Creates the State "California" with the City "San Francisco" from the database hbtn_0e_100_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>".format(sys.argv[0]))
        sys.exit(1)

    # Create connection to MySQL database
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, password, db_name))

    # Create tables
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object for California
    california = State(name="California")

    # Create a new City object for San Francisco
    san_francisco = City(name="San Francisco")

    # Add the City object to the State object's cities relationship
    california.cities.append(san_francisco)

    # Add the State object to the session
    session.add(california)

    # Commit the changes to the database
    session.commit()

    # Close session
    session.close()
