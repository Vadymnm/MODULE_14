import sqlite3

connection = (sqlite3.connect('module_14_4.db'))
cursor = connection.cursor()

# ------------  структура таблицы БД:
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT NOT NULL,
price INTEGER
)
''')

Product = ['Apple','Cherry','Srtawberry','Lemon']

def initiate_db():
    for i in range(1, 5):
        price_ = i * 50
        cursor.execute('INSERT INTO Users(title, description, price) VALUES(?, ?, ?)',
                       (f"{Product[i-1]}", f"description{i}", f"{price_}"))


def get_all_products():
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    return users

print('----------------------------')

#initiate_db()


# users = get_all_products()
#
# for user in users:
#     print( f"Название: {user[1]} |", f"Описание: {user[2]} |", f"Цена: {user[3]}")
#
# print('----------------------------')

# connection.commit()
# connection.close()