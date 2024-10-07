import sqlite3

connection = (sqlite3.connect('module_14_5.db'))
cursor = connection.cursor()

# ------------  структура таблицы БД:
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER NOT NULL,
balance INTEGER NOT NULL
)
''')


def get_all_users():
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    return users


def add_user(username, email, age):
    cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)',
                   (username, email, age, "1000"))
    print('Новый пользователь добавлен')
    connection.commit()


def is_included(username):
    print(username)
    info = cursor.execute("SELECT * FROM Users WHERE username=?", (username,))
#    print(info)
    new_user = info.fetchone()
    print('new user (is included):', new_user)
    return new_user


print('----------------------------')

#  *****  ТО,  ЧТО  ИСПОЛЬЗУЕТСЯ  ТОЛЬКО  ОДИН  РАЗ !!!!  ****
# def initiate_db():
#     for i in range(1, 2):
#         age = i * 10
#         cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)',
#                        (f"User{i}", f"{i}example@gmail.com", f"{age}", "1000"))

#
# initiate_db()
# add_user('Vasya', 'vasya@gmail.com', 33)
# new_user = is_included('Petya1')
# print(new_user)
#
# if new_user == None:
#     add_user('Petya1', 'petya@gmail.com', 25)
#
# users = get_all_users()
# for user in users:
#     print(f"username: {user[1]} |", f"email: {user[2]} |", f"age: {user[3]}", f"balance: {user[4]}")
# #
# print('----------------------------')

# connection.commit()
# connection.close()
