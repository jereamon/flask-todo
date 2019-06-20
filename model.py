from peewee import Model, CharField, DateTimeField, ForeignKeyField
import os

from playhouse.db_url import connect

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))


class User(Model):
    name = CharField(unique=True, max_length=256)
    password = CharField(max_length=256)
    class Meta:
        database = db


class Task(Model):
    name = CharField(max_length=30)
    performed = DateTimeField(null=True)
    performed_by = ForeignKeyField(model=User, null=True)
    class Meta:
        database = db
