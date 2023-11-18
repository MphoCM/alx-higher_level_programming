#!/usr/bin/python3
"""
Write a script lists all State objects
that contain the letter a from database hbtn_0e_6_usa"""


import sys
from model_state import Base, State
from sqlalchemy import create-engine
from sqlalchemy.orm import sessionmaker

# should not be executed when imported
if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    a_states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    for state in a_states:
        print("{}: {}".format(state.id, state.name))
