#!/usr/bin/python3
"""
Lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
"""

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

    # Query State objects and filter those containing the letter "a"
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))
