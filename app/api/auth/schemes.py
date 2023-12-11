import datetime

from fastapi_users import schemas

from app.core.enums import UserRole


class UserRead(schemas.BaseUser[int]):
    first_name: str
    last_name: str
    address: str
    phone_number: str
    role: UserRole
    created_at: datetime.datetime
    updated_at: datetime.datetime


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    last_name: str
    address: str
    phone_number: str


class UserUpdate(schemas.BaseUserUpdate):
    first_name: str | None
    last_name: str | None
    address: str | None
    phone_number: str | None
