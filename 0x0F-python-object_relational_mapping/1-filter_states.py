#!/usr/bin/python3
"""
script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa:
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    # the database connection requirements
    HOST = "localhost"
    PORT = 3306
    USER = argv[1]
    PASS = argv[2]
    DB = argv[3]

    # the database connection establishments
    db = MySQLdb.connect(host=HOST,
                         port=PORT,
                         user=USER,
                         passwd=PASS,
                         db=DB,
                         charset="utf8")

    # creating the cursor object
    cursor = db.cursor()

    # constructing the query to select teh states starting with 'N'
    query = " ".join(["SELECT * FROM states",
                      "WHERE name LIKE BINARY 'N%'"
                      "ORDER BY states.id"])

    # executing the sql querry
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
