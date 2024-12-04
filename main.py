from SQLRequests import SQLRequests
from TypesSQL import SQLite
import sqlite3 as sq


sql_builder = SQLRequests()


# Подключение к базе данных (создаст файл, если его нет)
database = sq.connect('data_jam.db')
# Создание курсора
cursor = database.cursor()


# # CREATE запрос
# create_command = (sql_builder.create('users', {'login' : SQLite.text.value, 'password' : SQLite.integer.value, 'admin' : SQLite.blob.value}))
#
# print(create_command)
#
# db.execute(create_command)
# db.commit()
#
#
# # ALTER запрос
# alter_command = (sql_builder
#                  .alter('users',
#                         {'ban' : SQLite.blob.value}))
#
# db.execute(alter_command)
# db.commit()

# CREATE запрос
def create_table(name_table: str, arguments: dict):
    database.execute(sql_builder.create(name_table, arguments))
    database.commit()


# ALTER запрос
def alter_table(name_table: str, arguments: dict):
    database.execute(sql_builder.alter(name_table,arguments))
    database.commit()


create_table('users', {'login' : SQLite.text.value, 'password' : SQLite.integer.value, 'admin' : SQLite.blob.value})
alter_table('users', {'ban' : SQLite.blob.value})


# # SELECT запрос
# query1 = (sql_builder
#           .select("users", {"id": "name"})
#           .where({"status": "active", "age": "30"})
#           .order_by("name", "ASC")
#           .limit(10)
#           .build())
# print(query1)
# # Вывод: SELECT id, name FROM users WHERE status = 'active' AND age = '30' ORDER BY name ASC LIMIT 10
#
# # INSERT запрос
# query2 = sql_builder.insert("users", {"name": "John Doe", "age": 30, "status": "active"}).build()
# print(query2)
# # Вывод: INSERT INTO users (name, age, status) VALUES ('John Doe', '30', 'active')
#
# # UPDATE запрос
# query3 = (sql_builder
#           .update("users", {"name": "Jane Doe"}, {"id": 1})
#           .build())
# print(query3)
# # Вывод: UPDATE users SET name = 'Jane Doe' WHERE id = '1'
#
# # DELETE запрос
# query4 = sql_builder.delete("users", {"status": "inactive"}).build()
# print(query4)
# # Вывод: DELETE FROM users WHERE status = 'inactive'

