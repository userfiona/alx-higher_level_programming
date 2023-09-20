#!/usr/bin/python3
<<<<<<< HEAD
"""Prints the State object with the name passed
as argument from the database hbtn_0e_6_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == '__main__':
    URL = 'mysql+mysqldb://{}:{}@localhost/{}'
    s1, s2, s3 = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(URL.format(s1, s2, s3), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    status = 0
    states = session.query(State).filter(State.name == sys.argv[4])
    for state in states:
        status += 1
        print(state.id)
    if (status == 0):
        print('Not found')
=======

"""
A script that prints the State object with the name passed as an argument
from hbtn_0e_6_usa
Username, password, dbname, and name to search will be passed as arguments to the script.
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)

    # Create a session
    session = Session()

    # Extract the State object with the given name
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    # Print state.id or "Not found" if not found
    if state is None:
        print("Not found")
    else:
        print(state.id)

    session.close()
>>>>>>> 4af1a2f9cddcdbd0e8ccc7cb2f6b9ac828f01653
