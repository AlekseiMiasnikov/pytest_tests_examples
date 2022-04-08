from peewee import CharField, IntegerField
from core.db.db import BaseModel


class Users(BaseModel):
    login = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()
    created_at = IntegerField()
    last_login_at = IntegerField()
    token = CharField()

    class Meta:
        table_name = 'users'
