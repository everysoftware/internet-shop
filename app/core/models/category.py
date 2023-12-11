from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.schema import ForeignKey

from .base import Base, int_pk

if TYPE_CHECKING:
    pass


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int_pk]
    name: Mapped[str]
