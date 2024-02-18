#!/usr/bin/python3


import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")

    cur = conn.cursor()
    text = """SELECT * FROM states WHERE name="{}" ORDER BY states.id ASC"""
    text = text.format(argv[4])
    cur.execute(text)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
