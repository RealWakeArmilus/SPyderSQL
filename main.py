from MasterSQL import SQLite, TypesSQL


# создание MasterSQL для базы данных SQLite
MasterSQL = SQLite

# Индикатор типа столбца
type_column = TypesSQL.SQLite


name_database = 'database/supremacy.db'

data_id = [12345678, 1641924, 3418749, 9384194, 23971037, 23074102, 2372389, 239873964, 28749364, 2398792]

data_states = {
    1 : {'name_state': 'Франция', 'tg_id': 13523532},
    2 : {'name_state': 'Испания', 'tg_id': 42523532},
    3 : {'name_state': 'Германская Империя', 'tg_id': 75433534},
    4 : {'name_state': 'Нидерландская Новая Гвинея', 'tg_id': 0}
}


# # Создает таблицу, если ее нет
# MasterSQL.create_table(name_database,
#                        'tg_users',
#                        {'tg_id': type_colomn.integer.value},
#                        True)
#
# # Добавляет в таблицу новую колонку
# MasterSQL.alter_table(name_database,
#                       'tg_users',
#                       {'admin': type_colomn.blob.value})
#
# # Заполняет таблицу данными
# for tg_id in data_id:
#     MasterSQL.insert_table(name_database,
#                            'tg_users',
#                            ['tg_id', 'admin'],
#                            (tg_id, False))
#
# # Обновляет данные в выбранных колонках
# MasterSQL.update_table(name_database,
#                        'tg_users',
#                        {'admin': True},
#                        {'tg_id': 23971037})

# Выборка данных из таблицы конкретных столбцов
new_data = MasterSQL.select_table(name_database,
                                  'tg_users',
                                  ['id', 'tg_id'])

print('new_data: ', new_data)

# Выборка данных из таблицы всех столбцов
new_data = MasterSQL.select_table(name_database,
                                  'tg_users')

print('new_data_all_columns: ', new_data)


# # Создает таблицу, если ее нет
# MasterSQL.create_table(name_database,
#                        'states',
#                        {'names' : type_colomn.text.value, 'tg_id' : type_colomn.integer.value},
#                        True)
#
# # Добавляет в таблицу новую колонку
# MasterSQL.alter_table(name_database,
#                       'states',
#                       {'map_id' : type_colomn.integer.value})
#
# # Удаляет таблицу, если она есть
# MasterSQL.drop_table(name_database,
#                      'users')
#
# # Заполняет таблицу данными
# for key, value in data_states.items():
#     MasterSQL.insert_table(name_database,
#                            'states',
#                            ['names', 'tg_id'],
#                            (value['name_state'], value['tg_id']))
#
# # Обновляет данные в выбранных колонках
# MasterSQL.update_table(name_database,
#                        'states',
#                        {'tg_id': 2525252525},
#                        {'names': 'Нидерландская Новая Гвинея'})
