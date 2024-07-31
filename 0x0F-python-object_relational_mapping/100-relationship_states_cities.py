#!/usr/bin/python3
"""
script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa:
"""

from sys import argv
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    USR = argv[1]
    PASS = argv[2]
    DB = argv[3]
    engine = create_engine(f'mysql+mysqldb://{USR}:{PASS}@localhost:3306/{DB}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    newState = State(name="California")
    newCity = City(name="San Francisco", state=newState)
    session.add(newState)
    session.add(newCity)
    session.commit()
    session.close()
