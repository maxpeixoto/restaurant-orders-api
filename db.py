import mysql.connector
import os


def connect():
        return mysql.connector.connect(
            host=os.environ['RDS_HOSTNAME'],
            user=os.environ['RDS_USERNAME'],
            password=os.environ['RDS_PASSWORD'],
            database=os.environ['RDS_DB_NAME']
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

