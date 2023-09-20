#!/usr/bin/python3
"""
Script that changes the name of a State object
from the database hbtn_0e_6_usa
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

    # Query the State object with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:
        # Update the name of the State object to "New Mexico"
        state_to_update.name = "New Mexico"

        # Commit the transaction to save the changes
        session.commit()
    else:
        print("State with id 2 not found")

    # Close the session
    session.close()
