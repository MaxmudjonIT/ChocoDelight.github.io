import sqlite3

db_connect = sqlite3.connect('DateBase.sqlite3')
db_cursor = db_connect.cursor()

def RegistrationUser():
    db_cursor.execute(
        """CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            user_id INTEGER UNIQUE, 
            name TEXT,
            phone TEXT
        )""")
    db_connect.commit()

RegistrationUser()