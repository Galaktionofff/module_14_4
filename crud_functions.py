import sqlite3


connection = sqlite3.connect('banki.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    )
    ''')
    connection.commit()



def get_all_products():
    cursor.execute('SELECT * FROM Products')
    all_ = cursor.fetchall()
    connection.commit()
    return all_

