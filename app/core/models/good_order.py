from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.schema import ForeignKey

from .base import Base, int_pk

if TYPE_CHECKING:
    pass


class GoodOrder(Base):
    __tablename__ = "good_order"

    good_id: Mapped[int_pk] = mapped_column(ForeignKey("goods.id", ondelete="cascade"))
    order_id: Mapped[int_pk] = mapped_column(ForeignKey("orders.id", ondelete="cascade"))
