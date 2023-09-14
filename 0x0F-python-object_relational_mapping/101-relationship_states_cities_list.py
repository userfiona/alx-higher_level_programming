#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects
from the database hbtn_0e_101_usa.
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print State and City objects sorted by states.id and cities.id
    states_and_cities = session.query(State).order_by(State.id, City.id).all()

    for state in states_and_cities:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

