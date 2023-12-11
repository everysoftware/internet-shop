from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.schema import ForeignKey

from .base import Base, created_at, int_pk, updated_at

if TYPE_CHECKING:
    pass


class Account(Base):
    __tablename__ = "accounts"

    order_id: Mapped[int_pk] = mapped_column(ForeignKey("orders.id", ondelete="cascade"))
    promocode: Mapped[float]
    benefit: Mapped[str]
    status: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
