from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.schema import ForeignKey

from .base import Base, created_at, int_pk, updated_at

if TYPE_CHECKING:
    pass


class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int_pk]
    manager_id: Mapped[int] = mapped_column(ForeignKey("managers.id", ondelete="cascade"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="cascade"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
