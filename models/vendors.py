from peewee import CharField, IntegerField
from core.db.db import BaseModel


class Vendors(BaseModel):
    name = CharField(unique=True)
    icon_id = IntegerField()
    is_archive = IntegerField()

    class Meta:
        table_name = 'vendors'
