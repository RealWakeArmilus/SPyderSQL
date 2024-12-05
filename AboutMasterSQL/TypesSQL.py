from enum import Enum


class SQLite(Enum):
    """
    Выбор тип данных для базы данных SQLite

    :var null: Отсутствие значения.
    :var integer_primary_key_autoincrement: INTEGER PRIMARY KEY AUTOINCREMENT - подходит для нумерации записей в таблице. Должна быть всегда первой и уникальной.
    :var integer: Целое число, которое может быть положительным и отрицательным и в зависимости от своего значения может занимать 1, 2, 3, 4, 6 или 8 байт
    :var real: число с плавающей точкой, занимает 8 байт в памяти
    :var text: строка текста в одинарных кавычках, в кодировке базы данных (UTF-8, UTF-16BE или UTF-16LE)
    :var blob: бинарные данные True/False
    :var numeric: хранит данные всех пяти выше перечисленных типов. (в терминологии SQLite NUMERIC еще называется type affinity)
    """
    null = 'NULL'
    integer_primary_key_autoincrement = 'INTEGER PRIMARY KEY AUTOINCREMENT'
    integer = 'INTEGER DEFAULT 0'
    real = 'REAL DEFAULT 0.0'
    text = "TEXT DEFAULT ''"
    blob = 'BLOB DEFAULT False'
    numeric = 'NUMERIC DEFAULT '''