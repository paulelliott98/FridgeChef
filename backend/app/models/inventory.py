"""
Each row is one food item associated with a specific user (can have multiple different food items associated with each user id)
"""

from datetime import date

from sqlalchemy import ForeignKey, String, Float, Date
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Inventory(Base):
    __tablename__ = "inventory"

    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    item_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    quantity: Mapped[float] = mapped_column(
        Float,
        nullable=False
    )

    unit: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    expiration_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )