#!/usr/bin/python3
<<<<<<< HEAD
"""Script prints first `State` object from database
Takes three arguments
    mysql username
    mysql password
    database name
Connects to host localhost and default port (3306)
"""
if __name__ == "__main__":
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sys import argv
    Session = sessionmaker()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    instance = session.query(State).first()
    if instance:
        print("{}: {}".format(instance.id, instance.name))
=======

"""
List all states
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).order_by(State.id).first()
    if state:
        print("{}: {}".format(state.id, state.name))
>>>>>>> 4af1a2f9cddcdbd0e8ccc7cb2f6b9ac828f01653
    else:
        print("Nothing")
    session.close()
