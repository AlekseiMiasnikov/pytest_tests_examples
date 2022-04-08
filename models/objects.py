from peewee import CharField, IntegerField
from core.db.db import BaseModel


class Objects(BaseModel):
    name = CharField(unique=True)
    is_archive = IntegerField()

    class Meta:
        table_name = 'objects'
