#!/usr/bin/python3
"""
Script that adds the State object "Louisiana"
to the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create an engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create the database tables if they don't exist yet
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object and add it to the session
    new_state = State(name="Louisiana")
    session.add(new_state)

    # Commit the transaction to save the new State object to the database
    session.commit()

    # Print the new State's id after creation
    print(new_state.id)

    # Close the session
    session.close()
