from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped

from .base import Base, int_pk

if TYPE_CHECKING:
    pass


class Provider(Base):
    __tablename__ = "providers"

    id: Mapped[int_pk]
    address: Mapped[str]
    phone_number: Mapped[str]
