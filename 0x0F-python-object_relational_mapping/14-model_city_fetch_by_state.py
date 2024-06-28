#!/usr/bin/python3
"""
script that prints all city objects from the database hbtn_0e_14_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":

    USR = argv[1]
    PASS = argv[2]
    DB = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(USR, PASS, DB))

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City, State).join(State).order_by(City.id).all()
    for city, state in result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
