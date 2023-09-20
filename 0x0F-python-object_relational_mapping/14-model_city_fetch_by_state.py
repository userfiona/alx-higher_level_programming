#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa
Takes three arguments:
    - MySQL username
    - MySQL password
    - Database name
Connects to host localhost and default port (3306)
"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City
    from sys import argv

    # Create an engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create the database tables if they don't exist
    Base.metadata.create_all(engine)

    # Query to fetch City objects along with their associated State objects
    city_states = session.query(State, City).join(City).order_by(City.id)

    # Print the results as described
    for state, city in city_states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()
