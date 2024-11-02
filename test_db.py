import pytest
import sqlite3 as sq


class TestDataBase:

    @pytest.fixture
    def db_connection(self):
        conn = sq.connect(':memory:')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
        conn.commit()
        yield conn
        conn.close()

    def test_add(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")
        db_connection.commit()
        cursor.execute("SELECT * FROM users WHERE name='Alice'")
        result = cursor.fetchone()
        assert result is not None

    def test_change(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO users (name, age) VALUES ('David', 40)")
        db_connection.commit()
        cursor.execute("UPDATE users SET age=41 WHERE name='David'")
        db_connection.commit()
        cursor.execute("SELECT age FROM users WHERE name='David'")
        result = cursor.fetchone()
        assert result[0] == 41

    def test_dell(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO users (name, age) VALUES ('David', 40),"
                       "('John', 25), ('Mary', 30)")
        db_connection.commit()
        cursor.execute("DELETE FROM users WHERE name = 'John'")
        cursor.connection.commit()
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        assert len(result) == 2

    def test_all_values(self, db_connection):
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO users (name, age) VALUES ('David', 40)")
        db_connection.commit()
        cursor.execute("INSERT INTO users (name, age) VALUES ('John', 40)")
        db_connection.commit()
        cursor.execute("INSERT INTO users (name, age) VALUES ('David', 40)")
        db_connection.commit()
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        assert len(result) == 3
