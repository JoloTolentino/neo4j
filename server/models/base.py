from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, deferred
from datetime import datetime, timezone
from sqlalchemy import String, DateTime
from sqlalchemy.orm import declared_attr, Mapped, mapped_column


class Base(DeclarativeBase):
    uuid:Mapped[str] = mapped_column(String, primary_key=True)


class TimestampMixin:
    @declared_attr
    def created_at(cls) -> Mapped[datetime]:
        return mapped_column(
            DateTime(timezone=True),
            default=lambda: datetime.now(timezone.utc)
        )

    @declared_attr
    def updated_at(cls) -> Mapped[datetime]:
        return mapped_column(
            DateTime(timezone=True),
            default=lambda: datetime.now(timezone.utc),
            onupdate=lambda: datetime.now(timezone.utc)
        )