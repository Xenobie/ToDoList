import sqlite3

# Подключаемся к базе данных напрямую через sqlite3
conn = sqlite3.connect('todos_db.db')
cursor = conn.cursor()

# Выполняем простой запрос
cursor.execute("SELECT * FROM todos")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()