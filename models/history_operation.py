from peewee import CharField, IntegerField, FloatField
from core.db.db import BaseModel


class HistoryOperation(BaseModel):
    vendor_id = IntegerField()
    material_id = IntegerField()
    object_id = IntegerField()
    volume = FloatField()
    price = FloatField()
    total = FloatField()
    file_id = IntegerField()
    comment = CharField(unique=True)
    created_at = IntegerField()
    updated_at = IntegerField()
    is_debt = IntegerField()
    confirmed_data = IntegerField()

    class Meta:
        table_name = 'history_operation'
