from datetime import datetime
from peewee import *

db = SqliteDatabase('history.db')


class ModelBase(Model):
    created_at = DateField(default=datetime.now())

    class Meta():
        database = db


class History(ModelBase):
    name = CharField()
    telegram_id = IntegerField()
    message = TextField()
    response = TextField()
