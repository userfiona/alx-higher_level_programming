#!/usr/bin/python3

"""
A script that lists all State objects from hbtn_0e_6_usa that contain
the letter 'a' from the database.
Username, password, and dbname will be passed as arguments to the script.
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    # Extract command-line arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create an SQLAlchemy engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}', pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and extract states containing the letter 'a'
    states = session.query(State).filter(State.name.ilike('%a%')).order_by(State.id).all()

    # Print the states
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()#!/usr/bin/python3

"""
A script that lists all State objects from hbtn_0e_6_usa that contain
the letter 'a' from the database.
Username, password, and dbname will be passed as arguments to the script.
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    # Extract command-line arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create an SQLAlchemy engine
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}', pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and extract states containing the letter 'a'
    states = session.query(State).filter(State.name.ilike('%a%')).order_by(State.id).all()

    # Print the states
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
