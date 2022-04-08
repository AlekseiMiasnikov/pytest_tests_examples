from peewee import IntegerField
from core.db.db import BaseModel


class Rights(BaseModel):
    user_id = IntegerField()
    is_admin = IntegerField()

    class Meta:
        table_name = 'rights'
