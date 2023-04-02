from datetime import datetime
from peewee import *

db = SqliteDatabase('db_for_tgbot.db')


class ModelBase(Model):
    created_at = DateField(default=datetime.now())

    class Meta():
        database = db


class History(ModelBase):
    location = TextField()
    message = TextField()
