from peewee import SqliteDatabase

DATABASE = 'blog.db'
DEBUG = True
SECRET_KEY = 'poiu4n56098j7c'


class Sqlite:

    connection = None

    def __init__(self):
        self.connection = SqliteDatabase(DATABASE)

    def get_connection(self):
        if self.connection is None:
            self.connection = SqliteDatabase(DATABASE)
        return self.connection
