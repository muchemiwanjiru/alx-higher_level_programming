#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb
if __name__ == "__main__":

    HOST = "localhost"
    PORT = 3306
    PASS = argv[2]
    USER = argv[1]
    DB = argv[3]

    db = MySQLdb.connect(host=HOST,
                        port=PORT,
                        passwd=PASS,
                        user=USER,
                        charset="utf8",
                        db=DB)
    
    cursor = db.cursor()
    query = " ".join(["SELECT c.id, c.name, st.name",
                    "FROM cities c, states st",
                    "WHERE c.state_id = st.id",
                    "ORDER BY c.id"])
    
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
