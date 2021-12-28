import mysql.connector
#TODO update requirements.txt


def connect():
        return mysql.connector.connect(
            # TODO use ENV
            host="",
            user="",
            password="",
            database=""
        )


db = connect()


def run(query):
    global db
    if not db or not db.is_connected():
        db = connect()
    cursor = db.cursor()
    print("running query:")
    print(query)
    cursor.execute(query)
    rv = cursor.fetchall()
    db.commit()
    return rv

