import MasterSQL
import TypesSQL


# Индикатор типа колонки
type_indicator = TypesSQL.SQLite


data = {
    1 : {'name_state': 'Франция', 'tg_id': 13523532},
    2 : {'name_state': 'Испания', 'tg_id': 42523532},
    3 : {'name_state': 'Германская Империя', 'tg_id': 75433534},
    4 : {'name_state': 'Нидерландская Новая Гвинея', 'tg_id': 0}
}


# Создает таблицу, если ее нет
MasterSQL.create_table('supremacy.db',
                       'states',
                       {'names' : type_indicator.text.value, 'tg_id' : type_indicator.integer.value},
                       True)

# Добавляет в таблицу новую колонку
MasterSQL.alter_table('supremacy.db',
                      'states',
                      {'map_id' : type_indicator.integer.value})

# Удаляет таблицу, если она есть
MasterSQL.drop_table('supremacy.db',
                     'users')

# Заполняет таблицу данными
for key, value in data.items():
    MasterSQL.insert_table('supremacy.db',
                           'states',
                           ['names', 'tg_id'],
                           (value['name_state'], value['tg_id']))

# Обновляет данные в выбранных колонках
MasterSQL.update_set_where_table('supremacy.db',
                                 'states',
                                 {'tg_id': 2525252525},
                                 {'names': 'Нидерландская Новая Гвинея'})