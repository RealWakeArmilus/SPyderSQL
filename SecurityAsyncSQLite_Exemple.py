import asyncio
from SPyderSQL import SecurityAsyncSQLite
from SPyderSQL import sanitize_table_name
from SPyderSQL import sanitize_column_names

SQLite = SecurityAsyncSQLite

async def main():

    db = SQLite("database.db")
    await db.connect()  # Подключение к БД

    # Создание таблицы (безопасное выполнение)
    await db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

    # Вставка данных
    await db.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
    await db.execute_many("INSERT INTO users (name) VALUES (?)", [("Bob",), ("Charlie",)])

    # Получение одной строки
    user = await db.fetchone("SELECT * FROM users WHERE name = ?", ("Alice",))
    print(dict(user))  # {'id': 1, 'name': 'Alice'}

    # Получение всех данных (⚠️ использовать с осторожностью, если данных очень много!)
    all_users = await db.fetchall("SELECT * FROM users")
    print([dict(u) for u in all_users])

    # Потоковое получение данных (экономия памяти)
    async for user in db.fetch_stream("SELECT * FROM users"):
        print(dict(user))  # Выведет по одной строке за раз

    await db.close()  # Закрытие соединения



asyncio.run(main())



async def employer_exemple():

    db = SQLite("company.db")
    await db.connect()


    # ✅ создания таблицы с множеством столбцов

    name_table = sanitize_table_name('employees')

    created_column_names = (
        'name TEXT NOT NULL,'
        'age INTEGER,'
        'department TEXT,'
        'salary REAL,'
        'hire_date TEXT DEFAULT CURRENT_TIMESTAMP'
    )

    await db.execute(f"""
        CREATE TABLE IF NOT EXISTS {name_table} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            {created_column_names}
        )
    """)

    await db.close()


    # ✅ Как добавить данные в таблицу?
    # Теперь можешь вставлять данные с помощью метода execute():

    name_table = sanitize_table_name('employees')

    column_names = sanitize_column_names(['name, age, department, salary'])
    values = ("Alice", 30, "Engineering", 75000.50)

    placeholders = ", ".join(["?" for _ in column_names])

    await db.execute(f"""
        INSERT INTO {name_table} ({", ".join(column_names)})
        VALUES ({placeholders})
    """, values)

    await db.close()


    # ✅ Как вставлять сразу много строк? (оптимизировано)
    # Чтобы быстро добавить несколько сотрудников сразу, используй execute_many():

    name_table = sanitize_table_name('employees')

    column_names = sanitize_column_names(['name, age, department, salary'])

    values_employees = [
        ("Bob", 28, "HR", 50000),
        ("Charlie", 35, "Marketing", 62000),
        ("Diana", 40, "Finance", 90000),
    ]

    placeholders = ", ".join(["?" for _ in column_names])

    await db.execute_many(f"""
            INSERT INTO {name_table} ({", ".join(column_names)})
            VALUES ({placeholders})
        """, values_employees)

    await db.close()


    # ✅ Как получить данные из таблицы?
    # 📌 Получить всех сотрудников:

    name_table = sanitize_table_name('employees')

    employees = await db.fetchall(f"SELECT * FROM {name_table}")

    await db.close()
    all_employees = [dict(emp) for emp in employees]

    print(all_employees)

    await db.close()


    # ✅ Как получить данные из таблицы?
    # 📌 Получить всех сотрудников:

    name_table = sanitize_table_name('employees')

    alone_where = ('Alice', )

    employee = await db.fetchone(f"SELECT * FROM {name_table} WHERE name = ?", alone_where)

    await db.close()
    employee_by_name = dict(employee) if employee else None

    print(employee_by_name)

    await db.close()


    # ✅ Как обновить данные в таблице?

    name_table = sanitize_table_name('employees')

    columns_to_update = ["salary"]
    update_values = (80000, 1)

    set_clause = ", ".join(f"{col} = ?" for col in columns_to_update)
    where_clause = "id = ?"

    await db.execute(f"""
            UPDATE {name_table} SET {set_clause} WHERE {where_clause}
        """, update_values)

    await db.close()


    # ✅ Как удалить данные из таблицы?

    name_table = sanitize_table_name('employees')

    alone_where = (2,)

    where_clause = "id = ?"

    await db.execute(f"DELETE FROM {name_table} WHERE {where_clause}", alone_where)

    await db.close()



asyncio.run(employer_exemple())


# 🎯 Вывод
# ✔ Создаёшь таблицу с множеством колонок через execute().
# ✔ Вставляешь данные через execute() или execute_many().
# ✔ Читаешь данные через fetchone() или fetchall().
# ✔ Используешь update и delete для модификации записей.
#
# 🔥 Теперь AsyncSQLite можно использовать для сложных баз данных! 🚀



# from fastapi import FastAPI
#
# async def fast_api_main():
#
#     app = FastAPI()
#     db = SQLite("database.db")
#
#     @app.on_event("startup")
#     async def startup():
#         await db.connect()
#         await db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
#
#     @app.on_event("shutdown")
#     async def shutdown():
#         await db.close()
#
#     @app.post("/users/")
#     async def create_user(name: str):
#         await db.execute("INSERT INTO users (name) VALUES (?)", (name,))
#         return {"message": "User added"}
#
#     @app.get("/users/")
#     async def get_users():
#         users = await db.fetchall("SELECT * FROM users")
#         return [dict(user) for user in users]



# asyncio.run(fast_api_main())

