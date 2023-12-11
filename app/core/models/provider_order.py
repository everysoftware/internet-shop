from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.schema import ForeignKey

from .base import Base, created_at, int_pk, updated_at

if TYPE_CHECKING:
    pass


class ProviderOrder(Base):
    __tablename__ = "provider_orders"

    id: Mapped[int_pk]
    manager_id: Mapped[int_pk] = mapped_column(ForeignKey("managers.id", ondelete="cascade"))
    provider_id: Mapped[int_pk] = mapped_column(ForeignKey("providers.id", ondelete="cascade"))
    status: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
