#!/usr/bin/python3
"""
script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""

from sys import argv
from relationship_state import State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    USR, PASS, DB = argv[1], argv[2], argv[3]
    engine = create_engine(f'mysql+mysqldb://{USR}:{PASS}@localhost:3306/{DB}')
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")
    session.close()
