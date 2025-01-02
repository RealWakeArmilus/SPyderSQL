import asyncio

from SPyderSQL import AsyncSQLite

SPyderSQLite = AsyncSQLite


async def main():

    name_database = 'database/City.db'

    # Инициализация асинхронного SQLite класса с путем к базе данных
    db = SPyderSQLite(name_database)


    # Создание таблицы 'users' с колонками 'name' и 'age' и автоматическим первичным ключом 'id'
    await db.create(
        name_table='users',
        append_columns={'name': 'TEXT', 'age': 'INTEGER', 'admin': 'BLOB', 'count': 'REAL', 'detail': 'NUMERIC'},
        id_primary_key=True
    ).execute()


    # Вставка одной записи в таблицу 'users'
    await db.insert('users', ['name', 'age']).execute(parameters=('Alice', 30))


    # Вставка нескольких записей в таблицу 'users'
    users_to_insert = [
        ('Bob', 25),
        ('Charlie', 35),
        ('Diana', 28)
    ]
    await db.insert('users', ['name', 'age']).executemany(parameters_list=users_to_insert)


    # Выборка всех записей из таблицы 'users'
    users = await db.select('users').execute()
    print("Все пользователи:")
    for user in users:
        print(user)


    # Выполнение запроса SELECT и получение результата с условием WHERE и ограничением LIMIT 1
    user = await db.select('users').where({'id': 1}).limit(1).execute()

    # Проверка и обработка результата
    if user:
        print("Найденный пользователь:")
        print(user[0])  # Поскольку результат - список, берем первый элемент
    else:
        print("Пользователь не найден.")

    # select('users'): Выбирает все столбцы из таблицы users.
    # where({'id': 1}): Добавляет условие, чтобы выбрать только записи, где id равно 1.
    # limit(1): Ограничивает результат одной записью.
    # execute(): Асинхронно выполняет сформированный запрос.


    # Использование метода fetch_one для получения одной записи
    user = await db.select('users').where({'id': 1}).fetch_one()

    if user:
        print("Найденный пользователь:")
        print(user)
    else:
        print("Пользователь не найден.")


    # Обновление возраста пользователя с именем 'Alice'
    await db.update(
        name_table='users',
        data_set={'age': 31},
        conditions={'name': 'Alice'}
    ).execute()


    # Выборка обновленной записи
    updated_user_alice = await db.select('users').where({'name': 'Alice'}).execute()
    print("\nОбновленная запись Alice:")
    print(updated_user_alice)


    # Удаление пользователя 'Bob'
    await db.delete('users', conditions={'name': 'Bob'}).execute()
    # Или
    await db.delete('users').where({'name': 'Alice'}).execute()


    # Выборка всех записей после удаления
    users_after_deletion = await db.select('users').execute()
    print("\nПользователи после удаления Bob:")
    for user in users_after_deletion:
        print(user)

    # Проверка удаления Alice
    deleted_user = await db.select('users').where({'name': 'Alice'}).fetch_one()
    print("\nПользователь Alice после удаления:")
    print(deleted_user)


# Запуск асинхронной функции main
asyncio.run(main())
