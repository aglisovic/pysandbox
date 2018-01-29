from peewee import ForeignKeyField, TextField, DateTimeField
from blog.models.abstract import AbstractModel
from blog.models.user import UserModel


class MessageModel(AbstractModel):
    user = ForeignKeyField(UserModel)
    content = TextField()
    pub_date = DateTimeField()

    class Meta:
        order_by = ('-pub_date',)
