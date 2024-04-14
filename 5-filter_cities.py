#!/usr/bin/python3
"""
list cities from states
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) == 5:
        try:
            host = "localhost"
            port = 3306
            usr = sys.argv[1]
            passwd = sys.argv[2]
            db = sys.argv[3]
            state = sys.argv[4]

            sq = "SELECT cities.name\
            FROM cities\
            WHERE state_id = \
            (SELECT id\
            FROM states\
            WHERE name=%s)\
            ORDER BY cities.id ASC"

            con = MySQLdb.connect(host=host, port=port, user=usr,
                                  passwd=passwd, db=db)

            cur = con.cursor()

            cur.execute(sq, (state,))

            cities = cur.fetchall()

            for city in cities:
                print("{}".format(city[0]), end="")
                if city != cities[len(cities) - 1]:
                    print(", ", end="")

            print()
        except:
            print("something wrong with sql query")

        finally:

            cur.close()
            con.close()
