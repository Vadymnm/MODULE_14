import sqlite3

connection = (sqlite3.connect('module_14_1.db'))
cursor = connection.cursor()

# ------------  структура таблицы БД:
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
# ------------  колонка "id" БД:
# cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
#
# # cursor.execute('INSERT INTO Users(username, email, age) VALUES(?, ?, ?)',("newuser", "ex@gmail.com", "28"))

# ------------  строки  таблицы БД:
# for i in range(1,11):
#     age_ = i * 10
#     cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)',
#                    (f"User{i}", f"{i}example@gmail.com", f"{age_}", "1000"))
#
# ------------  изменение баланса каждого второго пользователя:
# for i in range(1,11,2):
#     cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', ('500',f"User{i}"))
# ------------  удаление каждого третьего пользователя:
# for i in range(1,11,3):
#     print(i)
#     cursor.execute('DELETE FROM Users WHERE username = ?', (f"User{i}",))
# ------------  выборка и печать всех записей в БД:
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()
for user in users:
    print(f"Имя: {user[1]} |", f"Почта: {user[2]} |", f"Возраст: {user[3]} |", f"Баланс: {user[4]}")

connection.commit()
connection.close()
