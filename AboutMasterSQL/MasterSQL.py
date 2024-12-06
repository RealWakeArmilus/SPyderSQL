from SQLRequests import SQLRequests
import sqlite3 as sq


# экземпляр класса по созданию SQL-запросов
sql_builder = SQLRequests()


# CREATE запрос
def create_table(name_database: str, name_table: str, columns: dict, id_primary_key: bool = False):
    """
    Запрос для создания таблицы, если таковой нет.

    :param name_database: Название базы данных.
    :param name_table: Название таблицы.
    :param columns: Словарь столбцов таблицы. Ключи - названия столбцов, значения - их типы.
    :param id_primary_key: Добавить ли в начале таблицы уникальный id, для идентификации каждой записи. По умолчанию False - не добавлять, True - добавить
    """
    database = sq.connect(name_database)
    database.execute(sql_builder.create(name_table, columns, id_primary_key).build())
    database.commit()


# ALTER запрос
def alter_table(name_database: str, name_table: str, add_column: dict):
    """
    Запрос для добавления ОДНОЙ колонки в таблицу

    Примечание: В add_column должно быть максимум 1 пара значений

    :param name_database: Название базы данных.
    :param name_table: Название таблицы.
    :param add_column: Словарь должен содержать элементы одного нового столбца для созданной таблицы. Ключи - название столбца, значения - их типы.
    """
    database = sq.connect(name_database)
    database.execute(sql_builder.alter(name_table, add_column).build())
    database.commit()


# DROP запрос
def drop_table(name_database: str, name_table: str):
    """
    Запрос для удаления таблицы из базы данных

    :param name_database: Название базы данных.
    :param name_table: Название таблицы.
    """
    database = sq.connect(name_database)
    database.execute(sql_builder.drop(name_table).build())
    database.commit()


# INSERT запрос
def insert_table(name_database: str, name_table: str, names_columns: list, values_columns: tuple):
    """
    Запрос для заполнения таблицы новыми данными.

    Примечание: В values_columns должно быть минимум 2 значения

    :param name_database: Название базы данных.
    :param name_table: Название таблицы.
    :param names_columns: Список названий колонок таблиц.
    :param values_columns: Кортеж данных, которые заполняются в колонки таблиц.
    """
    database = sq.connect(name_database)
    database.execute(sql_builder.insert(name_table, names_columns).build(), values_columns)
    database.commit()


# UPDATE запрос
def update_table(name_database: str, name_table: str, data_set: dict, data_where: dict = None):
    """
    Запрос для изменения содержания конкретной или группы записей, схожих по определенному признаку

    :param name_database: Название базы данных.
    :param name_table: Название таблицы.
    :param data_set: Словарь для установки нового значения. Key - название колонки, Value - новое значение.
    :param data_where: Словарь по которому будет осуществляться поиск. Key - название колонки, Value - поисковое значение.
    """
    database = sq.connect(name_database)
    database.execute(sql_builder.update(name_table, data_set, data_where).build())
    database.commit()




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

