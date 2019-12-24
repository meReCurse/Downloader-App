import sqlite3
from abc import ABCMeta, abstractmethod


class AbstractDataBase(metaclass=ABCMeta):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def create_db(self):
        pass


class Sqlite3DataBase(AbstractDataBase):
    __slot__ = 'name', 'con', 'cur'

    def __init__(self, name):
        self.name = name
        self.con = None
        self.cur = None

    def connect(self):
        self.con = sqlite3.connect(self.name)
        self.cur = self.con.cursor()

    def close(self):
        self.cur.close()

    def create_db(self):
        con = sqlite3.connect(self.name)
        cur = con.cursor()
        try:
            cur.executescript("""\
                CREATE TABLE library (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    author TEXT,
                    url TEXT
                );
            """)
        except sqlite3.DatabaseError as err:
            print(err)
        finally:
            cur.close()


if __name__ == "__main__":
    base = Sqlite3DataBase('lib.db')
    base.create_db()
