#!/usr/bin/python3
"""
list all matched states
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) == 5:
        try:
            host = 'localhost'
            port = 3306
            usr = sys.argv[1]
            passwd = sys.argv[2]
            db = sys.argv[3]
            state = sys.argv[4]

            sq = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"

            con = MySQLdb.connect(host=host, port=port, user=usr,
                                  passwd=passwd, db=db)

            cur = con.cursor()

            cur.execute(sq, (state,))

            staterecords = cur.fetchall()

            for st in staterecords:
                print("{}".format(st))

        except:
            print("something wrong with the sql query")

        finally:

            cur.close()
            con.close()
