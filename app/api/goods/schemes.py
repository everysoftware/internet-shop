import datetime

from fastapi_users import schemas
from pydantic import BaseModel


class GoodRead(BaseModel):
    id: int
    name: str
    presence: bool
    price: int
    created_at: datetime.datetime
    updated_at: datetime.datetime


class GoodCreate(BaseModel):
    name: str
    presence: bool
    price: int


class GoodUpdate(BaseModel):
    name: str | None = None
    presence: bool | None = None
    price: int | None = None
