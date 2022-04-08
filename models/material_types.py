from peewee import CharField, IntegerField
from core.db.db import BaseModel


class MaterialTypes(BaseModel):
    name = CharField(unique=True)
    units_measurement_volume_id = IntegerField()

    class Meta:
        table_name = 'material_types'
