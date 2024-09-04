from ninja import Schema
from datetime import datetime
from pydantic import EmailStr

class DayHomeProviderListSchema(Schema):
    id: int
    first_name: str
    last_name: str
    location: str
    email: EmailStr

class DayHomeProviderDetailSchema(Schema):
    id: int
    first_name: str
    last_name: str
    location: str
    created_at: datetime
    updated_at: datetime
    email: EmailStr