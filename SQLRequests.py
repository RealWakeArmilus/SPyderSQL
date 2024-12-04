import logger
from my_exception import IsinstanceError


def makeup_columns(arguments: dict, columns: str = '') -> str:
    """
    Создание макета столбцов для таблиц базы данных

    :param arguments: Словарь аргументов столбцов таблицы. Ключи - названия столбцов, значения - их типы.
    :param columns: Уже существующие колонки
    :return: отформатированные столбцы в типе данных str
    """
    columns += ", ".join(
       ["{column_name} {column_type}".format
        (column_name=column_name, column_type=column_type)
        for column_name, column_type in arguments.items()])

    return columns



class SQLRequests:


    def __init__(self):

        self.query = ""


    def __str__(self):

        return self.query


    def create(self, name_table: str, arguments: dict, id_primary_key: bool = False) -> str:
        """
        Создает SQL-запрос для создания таблицы, если она не существует, и возвращает его.

        :param name_table: Название создаваемой таблицы.
        :param arguments: Словарь аргументов столбцов таблицы. Ключи - названия столбцов, значения - их типы.
        :param id_primary_key: Добавить ли в начале таблицы уникальный id, для идентификации каждой записи. По умолчанию False - не добавлять, True - добавить
        :return: SQL-запрос типа данных str.
        """
        columns = ''

        if id_primary_key:

            columns = 'id INTEGER PRIMARY KEY AUTOINCREMENT, '

        columns = makeup_columns(
            arguments,
            columns)

        # Создание SQL-запроса
        self.query = ("CREATE TABLE IF NOT EXISTS {name_table} "
                      "({columns})".format
                      (name_table=name_table, columns=columns))

        return self.query


    def alter(self, name_table: str, add_arguments: dict) -> str:
        """
        Создает SQL-запрос для изменения таблицы. Добавляет новые колонки.

        :param name_table: Название таблицы.
        :param add_arguments: Словарь аргументов новых столбцов для созданной таблицы. Ключи - названия столбцов, значения - их типы.
        :return: SQL-запрос типа данных str.
        """
        columns = makeup_columns(
            add_arguments)

        # Создание SQL-запроса
        self.query = ("ALTER TABLE {name_table} "
                      "ADD {columns}".format
                      (name_table=name_table, columns=columns))

        return self.query


    def drop(self, name_table: str) -> str:
        """
        Создает SQL-запрос для удаления существующей таблицы.

        :param name_table: Название таблицы, которую нужно удалить.
        :return: SQL-запрос типа данных str.
        """
        # Создание SQL-запроса
        self.query = ("DROP TABLE {name_table}".format
                      (name_table=name_table))

        return self.query


    def select(self, name_table: str, columns: list):
        """
        Создает базовый SELECT запрос.

        :param name_table: Название таблицы.
        :param columns: Список колонок для выборки или строка "*".
        :return: SQL-запрос типа данных str.
        """
        columns = ", ".join(columns)

        # Создание SQL-запроса
        self.query = ("SELECT {columns} "
                      "FROM {table}".format
                      (columns=columns,
                       table=name_table))

        return self.query


    def where(self, conditions):
        """
        Добавляет WHERE условия в запрос.

        :param conditions: Строка или словарь условий.
        :return: SQL-запрос типа данных str.
        """
        if isinstance(conditions, dict):
            cond = " AND ".join(f"{k} = '{v}'" for k, v in conditions.items())
        else:
            cond = conditions
        self.query += f" WHERE {cond}"
        return self.query


    def order_by(self, columns, order="ASC"):
        """
        Добавляет ORDER BY в запрос.

        :param columns: Колонка или список колонок для сортировки.
        :param order: Порядок сортировки, "ASC" или "DESC".
        :return: Экземпляр класса SQLRequests.
        """
        if isinstance(columns, (list, tuple)):
            columns = ", ".join(columns)
        self.query += f" ORDER BY {columns} {order}"
        return self


    def limit(self, count):
        """
        Добавляет LIMIT в запрос.

        :param count: Количество строк для ограничения выборки.
        :return: Экземпляр класса SQLRequests.
        """
        self.query += f" LIMIT {count}"
        return self


    def insert(self, table, data):
        """
        Создает INSERT запрос.

        :param table: Название таблицы.
        :param data: Словарь данных для вставки.
        :return: Экземпляр класса SQLRequests.
        """
        columns = ", ".join(data.keys())
        values = ", ".join(f"'{v}'" for v in data.values())
        self.query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        return self


    def update(self, table, data, conditions=None):
        """
        Создает UPDATE запрос.

        :param table: Название таблицы.
        :param data: Словарь данных для обновления.
        :param conditions: Условия для обновления.
        :return: Экземпляр класса SQLRequests.
        """
        updates = ", ".join(f"{k} = '{v}'" for k, v in data.items())
        self.query = f"UPDATE {table} SET {updates}"
        if conditions:
            self.where(conditions)
        return self


    def delete(self, table, conditions=None):
        """
        Создает DELETE запрос.

        :param table: Название таблицы.
        :param conditions: Условия для удаления.
        :return: Экземпляр класса SQLRequests.
        """
        self.query = f"DELETE FROM {table}"
        if conditions:
            self.where(conditions)
        return self


    def reset(self):
        """
        Сбрасывает текущий запрос.
        """
        self.query = ""
        return self


    def build(self):
        """
        Возвращает финальный SQL запрос.

        :return: Строка SQL-запроса.
        """
        query = self.query
        self.reset()
        return query


