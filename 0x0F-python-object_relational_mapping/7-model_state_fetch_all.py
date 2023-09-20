#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""

if __name__ == '__main__':
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    if len(argv) != 4:
        sys.exit('Use: 7-model_state_fetch_all.py <mysql username> '
                 '<mysql password> <database name>')

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/'
                           '{}'.format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    
    # Bind the engine to the Base class
    Base.metadata.bind = engine

    session = Session()

    # Query all State objects and order by State.id in ascending order
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))

    session.close()
