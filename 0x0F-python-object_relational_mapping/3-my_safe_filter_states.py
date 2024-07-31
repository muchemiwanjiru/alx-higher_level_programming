#!/usr/bin/python3
"""
script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. But this time,
it is safe from MySQL injections!
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    USER = argv[1]
    PASS = argv[2]
    DB = argv[3]
    PORT = 3306
    HOST = 'localhost'

    db = MySQLdb.connect(host=HOST, port=PORT, user=USER, passwd=PASS, db=DB)
    cursor = db.cursor()
    cursor.execute('SELECT * from states WHERE name = %s ORDER BY states.id', (argv[4], ))

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
