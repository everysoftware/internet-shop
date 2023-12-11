from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped

from .base import Base, created_at, int_pk, updated_at

if TYPE_CHECKING:
    pass


class Good(Base):
    __tablename__ = "goods"

    id: Mapped[int_pk]
    name: Mapped[str]
    presence: Mapped[bool]
    price: Mapped[int]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
