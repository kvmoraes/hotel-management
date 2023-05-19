import sqlite3
import os

def create_database():
    db = sqlite3.connect('management.db')
    cursor = db.cursor()

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS HOTEL(client int, floor int, room int, \
        single bed int, couple bed int, local string, PRIMARY KEY(client))'
    )

def delete_database():
    os.remove('./management.db')

if __name__ == "__main__" :
    delete_database()
    create_database()