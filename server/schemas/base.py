from uuid import UUID
from pydantic import BaseModel
from datetime import datetime


class Base(BaseModel):
    uuid: UUID


class Timestamp(BaseModel):
    created_at: datetime
    updated_at: datetime
