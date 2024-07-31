#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all cities of
that state, using the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb
if __name__ == "__main__":

    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306,
        host="localhost")

    icursor = db.cursor()
    icursor.execute(
        "SELECT cities.name FROM cities\
        INNER JOIN states ON cities.state_id = states.id\
        WHERE states.name = %s \
        ORDER BY cities.id ASC", (argv[4], ))

    cities = icursor.fetchall()

    id = 0
    for city in cities:
        if id != 0:
            print(", ", end="")
        print("%s" % city, end="")
        id += 1
    print("")

    icursor.close()
    db.close()
