#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""


if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    # putting the database connection requirements
    HOST = "localhost"
    PORT = 3306
    USER = argv[1]
    PASSWORD = argv[2]
    DATABASE = argv[3]

    # the connections to the database
    db = MySQLdb.connect(host=HOST,
                         port=PORT,
                         user=USER,
                         passwd=PASSWORD,
                         db=DATABASE,
                         charset="utf8")

    # creating the cursor object for interaction in the database
    cursor = db.cursor()

    # executeing the SQL query
    cursor.execute("SELECT * FROM states ORDER BY states.id")

    # getting the rows
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # closing the databsae and cursor connection
    cursor.close()
    db.close()
