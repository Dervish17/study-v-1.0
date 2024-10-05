import sqlite3 as sq
from prettytable import from_db_cursor


class DataBaseConnection:
    __connection = None

    def __new__(cls, *args, **kwargs):
        if cls.__connection is None:
            cls.__connection = super().__new__(cls)

        return cls.__connection

    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = sq.connect('instance')
        print(f'соединение с БД установлено')

    def close(self):
        print('закрытие соединения с БД')
        self.conn.close()

    def show(self):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT * FROM table1''')
        print('Данные из базы данных:')
        table = from_db_cursor(cursor)
        print(table)

    def write(self):
        cursor = self.conn.cursor()
        insert = [input('Введите пример:')]
        cursor.execute('''INSERT INTO table1 (name_instance) VALUES (?)''', insert)
        self.conn.commit()
        print(f"запись в БД произведена")


db = DataBaseConnection()
db1 = DataBaseConnection()
print(id(db), id(db1))
