from SQLRequests import SQLRequests
from TypesSQL import SQLite
import sqlite3 as sq


sql_builder = SQLRequests()


# Подключение к базе данных (создаст файл, если его нет)
database = sq.connect('supremacy.db')
# Создание курсора
cursor = database.cursor()


# CREATE запрос
def create_table(name_table: str, arguments: dict, id_primary_key: bool = False):
    """
    Запрос для создания таблицы, если таковой нет.

    :param name_table: Название таблицы.
    :param arguments: Словарь аргументов столбцов таблицы. Ключи - названия столбцов, значения - их типы.
    :param id_primary_key: Добавить ли в начале таблицы уникальный id, для идентификации каждой записи. По умолчанию False - не добавлять, True - добавить
    """
    database.execute(sql_builder.create(name_table, arguments, id_primary_key).build())
    database.commit()


# ALTER запрос
def alter_table(name_table: str, argument: dict):
    """
    Запрос для добавления ОДНОЙ колонки в таблицу

    :param name_table: Название таблицы.
    :param argument: Словарь должен содержать элементы одного нового столбца для созданной таблицы. Ключи - название столбца, значения - их типы.
    """
    database.execute(sql_builder.alter(name_table, argument).build())
    database.commit()


# DROP запрос
def drop_table(name_table: str):
    """
    Запрос для удаления таблицы из базы данных

    :param name_table: Название таблицы.
    """
    database.execute(sql_builder.drop(name_table).build())
    database.commit()


# INSERT запрос
def insert_table(name_table: str, names_colomns: list, values_colomns: tuple):
    """
    Запрос для заполнения таблицы новыми данными.

    :param name_table: Название таблицы.
    :param names_colomns: Список названий колонок таблиц.
    :param values_colomns: Кортеж данных, которые заполняются в колонки таблиц.
    """
    database.execute(sql_builder.insert(name_table, names_colomns).build(), values_colomns)
    database.commit()


# UPDATE запрос
def update_set_where_table(name_table: str, data_set: dict, data_where: dict = None):
    """
    Запрос для изменения содержания конкретной или группы записей, схожих по определенному признаку (пример: одинаковый возраст)

    :param name_table: Название таблицы.
    :param data_set: Словарь для установки нового значения. Key - название колонки, Value - новое значение.
    :param data_where: Словарь по которому будет осуществляться поиск. Key - название колонки, Value - поисковое значение.
    """
    database.execute(sql_builder.update(name_table, data_set, data_where).build())
    database.commit()


data = {
    1 : {'name_state': 'Франция', 'tg_id': 13523532},
    2 : {'name_state': 'Испания', 'tg_id': 42523532},
    3 : {'name_state': 'Германская Империя', 'tg_id': 75433534},
    4 : {'name_state': 'Нидерландская Новая Гвинея', 'tg_id': 0}
}



# create_table('states',
#              {'names' : SQLite.text.value, 'tg_id' : SQLite.integer.value},
#              True)

# alter_table('states',
#             {'map_id' : SQLite.integer.value})

# drop_table('users')

# for key, value in data.items():
#     insert_table('states',
#                  ['names', 'tg_id'],
#                  (value['name_state'], value['tg_id']))

update_set_where_table('states',
                       {'tg_id': 2525252525},
                       {'names': 'Нидерландская Новая Гвинея'})



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

