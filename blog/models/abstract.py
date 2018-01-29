from peewee import Model
from blog.util.database import Sqlite


class AbstractModel(Model):

    class Meta:
        database = Sqlite().get_connection()
