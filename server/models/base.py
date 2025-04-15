from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, deferred
from datetime import datetime, timezone
from sqlalchemy import String, DateTime


class Base(DeclarativeBase):
    uuid:Mapped[str] = mapped_column(String, primary_key=True)


class TimestampMixin:
    created_at: Mapped[datetime] = deferred(
        mapped_column(
            DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
        )
    )
    last_updated: Mapped[datetime] = deferred(
        mapped_column(
            DateTime(timezone=True), 
            default=lambda: datetime.now(timezone.utc),
            onupdate= lambda: datetime.now(timezone.utc)
        )
    )
