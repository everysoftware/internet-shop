from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.schema import ForeignKey

from .base import Base, int_pk

if TYPE_CHECKING:
    pass


class GoodCart(Base):
    __tablename__ = "good_cart"

    good_id: Mapped[int_pk] = mapped_column(ForeignKey("goods.id", ondelete="cascade"))
    cart_id: Mapped[int_pk] = mapped_column(ForeignKey("carts.order_id", ondelete="cascade"))
