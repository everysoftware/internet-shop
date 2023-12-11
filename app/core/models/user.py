from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, created_at, int_pk, updated_at
from ..enums import UserRole

if TYPE_CHECKING:
    pass


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "users"

    id: Mapped[int_pk]
    first_name: Mapped[str]
    last_name: Mapped[str]
    phone_number: Mapped[str]
    address: Mapped[str]
    role: Mapped[UserRole] = mapped_column(default=UserRole.USER)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
