import sqlite3

connection = (sqlite3.connect('module_14_2.db'))
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
cursor.execute('DELETE FROM Users WHERE username = ?', (f"User{6}",))
# ------------  выборка и печать всех записей в БД:
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()
for user in users:
    print(f"Имя: {user[1]} |", f"Почта: {user[2]} |", f"Возраст: {user[3]} |", f"Баланс: {user[4]}")
print('----------------------------')
# --------------------  Вариант AVG - 1:
cursor.execute('SELECT COUNT(*)  FROM Users')
total = cursor.fetchone()[0]
print('total users: ', total)
cursor.execute('SELECT SUM(balance) FROM Users')
sum = cursor.fetchone()[0]
print('total_balance = ', sum)
print('avg_balance1 = ', sum/total)
# ---------------------  Вариант AVG - 2:
print('----------------------------')
cursor.execute("SELECT AVG(balance) FROM Users")
avg_balance = cursor.fetchone()[0]
print('avg_balance2 = ', avg_balance)

connection.commit()
connection.close()
