#!/usr/bin/python3
<<<<<<< HEAD
"""
Script that deletes all State objects with a name containing
the letter a from the database
Using module SQLAlchemy
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    # create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    # create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # create a Session
    session = Session()
    Base.metadata.create_all(engine)
    state_del = session.query(State).filter(State.name.like('%a%')).all()
    for delete in state_del:
        session.delete(delete)
    # commit and close session
    session.commit()
    session.close()
=======
# Deletes all State objects with a name containing
# the letter 'a' from the database hbtn_0e_6_usa.
# Usage: ./13-model_state_delete_a.py <mysql username> /
#                                     <mysql password> /
#                                     <database name>
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State):
        if "a" in state.name:
            session.delete(state)
    
    session.commit()
>>>>>>> 4af1a2f9cddcdbd0e8ccc7cb2f6b9ac828f01653
