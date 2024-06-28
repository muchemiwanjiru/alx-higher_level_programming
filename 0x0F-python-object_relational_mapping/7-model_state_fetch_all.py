#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # getting the user, pswd & databs from cmd-line args
    USR = argv[1]
    DB = argv[3]
    PASS = argv[2]

    # creating the connection to the MySQL database
    mysql_engine = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(mysql_engine.format(USR, PASS, DB))

    # creating the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # querying the state objects using the session
    states = session.query(State).order_by(State.id)
    for state in states:
        print("{}: {}".format(state.id, state.name))
