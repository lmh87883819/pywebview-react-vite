from peewee import *
import datetime

db = SqliteDatabase('database/app.sqlite')


class BaseModel(Model):
    class Meta:
        database = db


class Todo(BaseModel):
    title = CharField()
    content = CharField()


def init_db():

    db.connect()
    db.create_tables([Todo])
