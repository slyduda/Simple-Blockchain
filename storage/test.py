import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = 'CREATE TABLE users (id INTEGER PRIMARY KEY ASC, username STRING UNIQUE NOT NULL, password STRING NOT NULL)'
cursor.execute(create_table)

connection.commit()
connection.close()