#!/usr/bin/python3
"""a script that takes in arguments and
dipslaysall vlues in the states table of hbtn_0e_0_usa
where name matches the argument.
safe from MySQL injections!"""


improt sys
iport MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            user=sys.argv[1], passwed=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    stateName = sys.argv[4]
    cur.execute(
            "SELECT * FROM states WHERE name = % ORDER BY id ASC;", (stateName,))

    state = cur.fetchall()
    for state in state:
        print(state)
