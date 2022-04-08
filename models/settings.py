from peewee import IntegerField, CharField
from core.db.db import BaseModel


class Settings(BaseModel):
    name = CharField()
    active = IntegerField()

    class Meta:
        table_name = 'settings'
