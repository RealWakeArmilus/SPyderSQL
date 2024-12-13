from SPyderSQL import SQLite, TypesSQLite

# создание SPyderSQL для базы данных SQLite
SPyderSQL = SQLite


name_database = 'database/supremacy.db'

data_id = [12345678, 1641924, 3418749, 9384194, 23971037, 23074102, 2372389, 239873964, 28749364, 2398792]

data_states = {
    1 : {'name_state': 'Франция', 'tg_id': 13523532},
    2 : {'name_state': 'Испания', 'tg_id': 42523532},
    3 : {'name_state': 'Германская Империя', 'tg_id': 75433534},
    4 : {'name_state': 'Нидерландская Новая Гвинея', 'tg_id': 0}
}


# # Создает таблицу, если ее нет
# SPyderSQL.create_table(name_database,
#                        'tg_users',
#                        {'tg_id': TypesSQLite.integer.value},
#                        True)
#
# # Добавляет в таблицу новую колонку
# SPyderSQL.alter_table(name_database,
#                       'tg_users',
#                       {'admin': TypesSQLite.blob.value})
#
# # Заполняет таблицу данными
# for tg_id in data_id:
#     SPyderSQL.insert_table(name_database,
#                            'tg_users',
#                            ['tg_id', 'admin'],
#                            (tg_id, False))
#
# # Обновляет данные в выбранных колонках
# SPyderSQL.update_table(name_database,
#                        'tg_users',
#                        {'admin': True},
#                        {'tg_id': 23971037})

# Выборка данных из таблицы конкретных столбцов
new_data = SPyderSQL.select_table(name_database,
                                  'tg_users',
                                  ['id', 'tg_id'])

print('new_data: ', new_data)

# Выборка данных из таблицы всех столбцов
new_data = SPyderSQL.select_table(name_database,
                                  'tg_users')

print('new_data_all_columns: ', new_data)

# Вывод названий всех столбцов таблицы
names_columns = SPyderSQL.pragma_table(name_database,
                                      'tg_users')

print('names_columns: ', names_columns)


# # Создает таблицу, если ее нет
# SPyderSQL.create_table(name_database,
#                        'states',
#                        {'names' : TypesSQLite.text.value, 'tg_id' : TypesSQLite.integer.value},
#                        True)
#
# # Добавляет в таблицу новую колонку
# SPyderSQL.alter_table(name_database,
#                       'states',
#                       {'map_id' : TypesSQLite.integer.value})
#
# # Удаляет таблицу, если она есть
# SPyderSQL.drop_table(name_database,
#                      'users')
#
# # Заполняет таблицу данными
# for key, value in data_states.items():
#     SPyderSQL.insert_table(name_database,
#                            'states',
#                            ['names', 'tg_id'],
#                            (value['name_state'], value['tg_id']))
#
# # Обновляет данные в выбранных колонках
# SPyderSQL.update_table(name_database,
#                        'states',
#                        {'tg_id': 2525252525},
#                        {'names': 'Нидерландская Новая Гвинея'})
