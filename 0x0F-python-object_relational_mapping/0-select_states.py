#!/usr/bin/python3
"""
list all states from mysql database
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) == 4:
        try:
            host = "localhost"
            port = 3306
            username = sys.argv[1]
            password = sys.argv[2]
            db = sys.argv[3]

            con = MySQLdb.connect(host=host, port=port,
                                  user=username, passwd=password, db=db)

            cur = con.cursor()

            sql_query = "SELECT * FROM states ORDER BY id ASC"

            cur.execute(sql_query)

            states = cur.fetchall()

            for state in states:
                print("{}".format(state))

        except:
            print("Error reading data from MySQL table")

        finally:
            cur.close()
            con.close()
