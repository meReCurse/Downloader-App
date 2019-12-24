import os
from .lib.connection import Connection
from .lib.parser import Parser
from .lib.data.database import Sqlite3DataBase
from .lib.data.entities import (
    Book, BookIdentityMap, BookMapper
)
from .lib.file_writer import FileWriter


class Model:
    __slots__ = (
        'connection', 'parser', 'database',
        'entity', 'identity_map', 'mapper',
        'file_writer', '_observers', 'counter')

    def __init__(self, proxy, name):
        self.connection = Connection(proxy)
        self.parser = Parser(self.connection)
        self.database = Sqlite3DataBase(name)
        self.entity = Book
        self.identity_map = BookIdentityMap
        self.mapper = BookMapper()
        self.file_writer = FileWriter()
        self._observers = []
        self.counter = 0
        self.setup_database()
        self.setup_mapper()

    def read_database(self):
        data = self.mapper.select_all()
        self.counter = len(data)
        for el in data:
            self.identity_map.add_book(el)
        self.notify_observers()

    def setup_database(self):
        if not os.path.isfile("library.db"):
            self.database.create_db()
        self.database.connect()

    def setup_mapper(self):
        con = self.database.con
        cur = self.database.cur
        self.mapper.connect(con, cur)

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.model_is_changed()

    def increment_counter(self):
        self.counter += 1
