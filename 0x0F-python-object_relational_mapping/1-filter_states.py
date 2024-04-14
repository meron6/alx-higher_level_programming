#!/usr/bin/python3
"""
lists states that starts with capital letter "N"
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

            sql_query = "SELECT * FROM states ORDER BY id ASC"

            con = MySQLdb.connect(host=host, port=port,
                                  user=usr, passwd=passwd, db=db)

            cur = con.cursor()

            cur.execute(sql_query)

            nstates = cur.fetchall()

            for nstate in nstates:
                if nstate[1][0] == 'N':
                    print("{}".format(nstate))

        except:
            print("error reading mysql query")

        finally:

            cur.close()
            con.close()
