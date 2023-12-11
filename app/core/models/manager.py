from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped

from .base import Base, int_pk

if TYPE_CHECKING:
    pass


class Manager(Base):
    __tablename__ = "managers"

    id: Mapped[int_pk]
    first_name: Mapped[str]
    last_name: Mapped[str]
    patronymic: Mapped[str]
    phone_number: Mapped[str]
