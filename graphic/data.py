import sqlite3

# Подключение к базе данных mord.db
mord_db = sqlite3.connect('mord.db')
mord_cursor = mord_db.cursor()

# Подключение к базе данных db.sqlite3
sqlite3_db = sqlite3.connect('db.sqlite3')
sqlite3_cursor = sqlite3_db.cursor()

# Выбор данных из таблицы morbidity
mord_cursor.execute('SELECT * FROM morbidity')
data_to_transfer = mord_cursor.fetchall()

# Вставка данных в таблицу main_data в db.sqlite3
for row in data_to_transfer:
    # Генерируем SQL-запрос для вставки данных в таблицу main_data
    insert_query = 'INSERT INTO main_data VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    sqlite3_cursor.execute(insert_query, row)

# Сохраняем изменения в базе данных db.sqlite3
sqlite3_db.commit()

# Закрываем соединения с базами данных
mord_db.close()
sqlite3_db.close()
