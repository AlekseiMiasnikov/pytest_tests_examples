from peewee import CharField, IntegerField
from core.db.db import BaseModel


class Materials(BaseModel):
    name = CharField(unique=True)
    type_id = IntegerField()

    class Meta:
        table_name = 'materials'
