from peewee import CharField, DateTimeField, ForeignKeyField
from hashlib import md5
from blog.models.abstract import AbstractModel


class UserModel(AbstractModel):
    username = CharField(unique=True)
    password = CharField()
    email = CharField()
    join_date = DateTimeField()

    class Meta:
        order_by = ('username',)

    def following(self):
        return UserModel.select().join(
            RelationshipModel, on=RelationshipModel.to_user
        ).where(RelationshipModel.from_user == self)

    def followers(self):
        return UserModel.select().join(
            RelationshipModel, on=RelationshipModel.from_user
        ).where(RelationshipModel.to_user == self)

    def is_following(self, user):
        return RelationshipModel.select().where(
            (RelationshipModel.from_user == self) &
            (RelationshipModel.to_user == user)
        ).count() > 0

    def gravatar_url(self, size=80):
        return 'http://www.gravatar.com/avatar/%s?d=identicon&s=%d' % (md5(self.email.strip().lower().encode('utf-8')).hexdigest(), size)


class RelationshipModel(AbstractModel):
    from_user = ForeignKeyField(UserModel, related_name='relationship')
    to_user = ForeignKeyField(UserModel, related_name='related_to')

    class Meta:
        indexes = (
            (('from_user', 'to_user'), True),
        )
