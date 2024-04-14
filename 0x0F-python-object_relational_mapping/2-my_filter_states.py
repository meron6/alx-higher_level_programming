#!/usr/bin/python3
"""
lists records that matches the given state
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

            sq = "SELECT * FROM states WHERE BINARY name='{}'".format(state)

            con = MySQLdb.connect(host=host, port=port,
                                  user=usr, passwd=passwd, db=db)

            cur = con.cursor()

            cur.execute(sq)

            staterecords = cur.fetchall()

            for staterecord in staterecords:
                print("{}".format(staterecord))

        except:
            print("problem with sql query")

        finally:
            cur.close()
            con.close()
