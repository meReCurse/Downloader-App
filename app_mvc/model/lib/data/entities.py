import sqlite3


class BookIdentityMap:
    book_map = {}

    @classmethod
    def add_book(cls, book):
        if book.id not in cls.book_map.keys():
            cls.book_map[book.id] = book

    @classmethod
    def get_book(cls, key):
        if key in cls.book_map.keys():
            return cls.book_map[key]
        else:
            return None

    @classmethod
    def get_books(cls):
        return cls.book_map.values()


class Book:
    __slot__ = "id", "title", "author", "url"

    def __init__(self, id, title, author, url):
        self.id = id
        self.title = title
        self.author = " ".join(author.split(","))
        self.url = url

    def __repr__(self):
        return f"Book(name={self.title}, author={self.author})"

    def __str__(self):
        return f"Book(name={self.title}, author={self.author})"

    def get_attrs(self):
        li = []
        for attr in dir(self):
            if not attr.startswith('__') and \
             not callable(getattr(self, attr)):
                li.append(attr)
        return li


class BookMapper:
    __slot__ = 'connection', 'cursor'

    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self, connection, cursor):
        self.connection = connection
        self.cursor = cursor

    def select_all(self):
        statement = f"SELECT * FROM library"
        self.cursor.execute(statement)
        data = []
        result = self.cursor.fetchall()
        for el in result:
            data.append(Book(*el))
        return data

    def find_by_id(self, id):
        statement = f"SELECT * FROM library WHERE ID=?"
        self.cursor.execute(statement, (id,))
        result = self.cursor.fetchone()
        if result:
            return Book(*result)
        else:
            raise sqlite3.DatabaseError

    def insert(self, book):
        statement = f"INSERT INTO library (title, author, url) VALUES (?, ?, ?)"
        self.cursor.execute(
            statement,
            (book.title, book.author, book.url))
        try:
            self.connection.commit()
        except Exception:
            raise sqlite3.DatabaseError

    def update(self, book):
        statement = f"UPDATE library SET title=?, author=?, url=? WHERE id=?"
        self.cursor.execute(
            statement,
            (book.title, book.author, book.url, book.id))
        try:
            self.connection.commit()
        except Exception:
            raise sqlite3.DatabaseError

    def delete(self, book):
        statement = f"DELETE FROM library WHERE id=?"
        self.cursor.execute(
            statement,
            (book.id))
        try:
            self.connection.commit()
        except Exception:
            raise sqlite3.DatabaseError
