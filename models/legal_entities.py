from peewee import CharField, IntegerField
from core.db.db import BaseModel


class LegalEntities(BaseModel):
    legal_entities_type_id = IntegerField()
    name = CharField(unique=True)
    created_at = IntegerField()
    updated_at = IntegerField()
    is_archive = IntegerField()

    class Meta:
        table_name = 'legal_entities'
