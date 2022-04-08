from peewee import IntegerField, FloatField
from core.db.db import BaseModel


class Payments(BaseModel):
    vendor_id = IntegerField()
    legal_entity_id = IntegerField()
    amount = FloatField()
    created_at = IntegerField()
    updated_at = IntegerField()

    class Meta:
        table_name = 'payments'
