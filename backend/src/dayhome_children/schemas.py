from ninja import Schema
from datetime import datetime
from dayhome_provider.schemas import DayHomeProviderDetailSchema

class DayHomeChildrenListSchema(Schema):
    id: int
    first_name: str
    last_name: str
    provider_id: DayHomeProviderDetailSchema

class DayHomeChildrenDetailSchema(Schema):
    id: int
    first_name: str
    last_name: str
    provider_id: DayHomeProviderDetailSchema
    created_at: datetime
    updated_at: datetime