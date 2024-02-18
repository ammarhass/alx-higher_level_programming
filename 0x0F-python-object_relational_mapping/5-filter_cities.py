#!/usr/bin/python3

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute(f"""SELECT cities.name FROM cities
                JOIN states ON states.id=cities.state_id
                WHERE states.name='{argv[4]}'
                ORDER BY cities.id ASC""")
    rows = cur.fetchall()
    print(", ".join(map(lambda i: i[0], rows)))
    cur.close()
    conn.close()
