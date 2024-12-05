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


    def create(self, name_table: str, colomns: dict, id_primary_key: bool = False):
        """
        Создает SQL-запрос для создания таблицы, если она не существует, и возвращает его.

        :param name_table: Название создаваемой таблицы.
        :param colomns: Словарь столбцов таблицы. Ключи - названия столбцов, значения - их типы.
        :param id_primary_key: Добавить ли в начале таблицы уникальный id, для идентификации каждой записи. По умолчанию False - не добавлять, True - добавить
        :return: Экземпляр класса SQLRequests.
        """
        columns = ''

        if id_primary_key:

            columns = 'id INTEGER PRIMARY KEY AUTOINCREMENT, '

        columns = makeup_columns(
            colomns,
            columns)

        # Создание SQL-запроса
        self.query = ("CREATE TABLE IF NOT EXISTS {name_table} "
                      "({columns})".format
                      (name_table=name_table, columns=columns))

        return self


    def alter(self, name_table: str, add_colomn: dict):
        """
        Создает SQL-запрос для изменения таблицы. Добавляет новые колонки.

        :param name_table: Название таблицы.
        :param add_colomn: Словарь должен содержать элементы одного нового столбца для созданной таблицы. Ключи - название столбца, значения - их типы.
        :return: Экземпляр класса SQLRequests.
        """
        column = makeup_columns(
            add_colomn)

        # Создание SQL-запроса
        self.query = ("ALTER TABLE {name_table} "
                      "ADD {column}".format
                      (name_table=name_table, column=column))

        return self


    def drop(self, name_table: str):
        """
        Создает SQL-запрос для удаления существующей таблицы.

        :param name_table: Название таблицы, которую нужно удалить.
        :return: Экземпляр класса SQLRequests.
        """
        # Создание SQL-запроса
        self.query = ("DROP TABLE IF EXISTS {name_table}".format
                      (name_table=name_table))

        return self


    def insert(self, name_table: str, names_colomns: list):
        """
        Создает INSERT запрос. Для заполнения уже созданной таблицы новыми данными.

        :param name_table: Название таблицы.
        :param names_colomns: Названия колонок таблиц.
        :return: Экземпляр класса SQLRequests.
        """
        # Выписывание названий колонок
        names_colomns = ", ".join(names_colomns)

        # Подсчет колонок, с которыми будут взаимодействовать
        count_colomns : int = len(names_colomns) + 1

        values_colomns = []

        for _ in 0, count_colomns:
            values_colomns.append('?')

        # Переход списка знаков "?" в формат str
        values_colomns = ', '.join(values_colomns)

        # Создание SQL-запроса
        self.query = ("INSERT INTO {name_table} ({name_columns}) VALUES ({value_colomns})".format
                      (name_table=name_table, name_columns=names_colomns, value_colomns=values_colomns))

        return self


    def select(self, name_table: str, columns: list):
        """
        Создает базовый SELECT запрос.

        :param name_table: Название таблицы.
        :param columns: Список колонок для выборки или строка "*".
        :return: Экземпляр класса SQLRequests.
        """
        columns = ", ".join(columns)

        # Создание SQL-запроса
        self.query = ("SELECT {columns} "
                      "FROM {name_table}".format
                      (columns=columns,
                       name_table=name_table))

        return self


    def where(self, conditions: dict):
        """
        Добавляет WHERE условия в запрос.

        :param conditions: Строка или словарь условий.
        :return: Экземпляр класса SQLRequests.
        """
        cond = " AND ".join("{key} = {value}".format(key=key, value=value) if isinstance(value, (int, bool))
            else "{key} = '{value}'".format(key=key, value=value)
            for key, value in conditions.items()
        )

        self.query += (" WHERE {cond}".format
                       (cond=cond))

        return self


    def limit(self, count: int):
        """
        Добавляет LIMIT в запрос.

        :param count: Количество строк для ограничения выборки.
        :return: Экземпляр класса SQLRequests.
        """
        self.query += (" LIMIT {count}".format
                       (count=count))

        return self


    def order_by(self, columns: list, order: str = "ASC"):
        """
        Добавляет ORDER BY в запрос.

        :param columns: Колонка или список колонок для сортировки.
        :param order: Порядок сортировки, "ASC" или "DESC".
        :return: Экземпляр класса SQLRequests.
        """
        columns = ", ".join(columns)

        self.query += (" ORDER BY {columns} {order}".format
                       (columns=columns, order=order))

        return self


    def update(self, name_table: str, data_set: dict, conditions=None):
        """
        Создает UPDATE запрос. Для обновления данных конкретной записи или записей.

        :param name_table: Название таблицы.
        :param data_set: Словарь данных для обновления.
        :param conditions: Условия для обновления.
        :return: Экземпляр класса SQLRequests.
        """
        updates = ", ".join("{key} = '{value}'".format(key=key, value=value)
                            for key, value in data_set.items())

        self.query = "UPDATE {name_table} SET {updates}".format(name_table=name_table, updates=updates)

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

