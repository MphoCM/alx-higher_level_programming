#!/usr/bin/python3
"""
Write a script lists all State objects
that contain the letter a from database hbtn_0e_6_usa"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import MetData
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]),
            pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sesh = Session()
    state = sesh.query(State).filter(
            State.name.contains('a')).order_by(State.id).all()
    for place in state:
        print("{}: {}".format(place.id, place.name))
    sesh.close()
