#!/usr/bin/python3
"""
list all cities from db
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) == 4:
        try:
            host = "localhost"
            port = 3306
            usr = sys.argv[1]
            passwd = sys.argv[2]
            db = sys.argv[3]

            sq = "SELECT cities.id, cities.name, states.name \
            FROM cities\
            INNER JOIN states\
            ON cities.state_id = states.id\
            ORDER BY cities.id ASC"

            con = MySQLdb.connect(host=host, port=port, user=usr,
                                  passwd=passwd, db=db)

            cur = con.cursor()

            cur.execute(sq)

            cities = cur.fetchall()

            for city in cities:
                print("{}".format(city))

        except:
            print("something wrong with sql query")

        finally:

            cur.close()
            con.close()
