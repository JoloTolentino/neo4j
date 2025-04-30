import enum
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from server.models.base import Base, TimestampMixin
from sqlalchemy.dialects.postgresql import ENUM as PGEnum
from sqlalchemy import Enum


# foreign key is some key that referes to the primary key of another table


class movie_roles(enum.Enum):
    actor = "actor"
    director = "director"


class Person(TimestampMixin, Base):
    __tablename__ = "persons"
    name: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)
    role: Mapped[movie_roles] = mapped_column(
        Enum(movie_roles, name="movie_roles", create_type=False), nullable=False
    )
    movie_id: Mapped[str] = mapped_column(ForeignKey("movies.uuid"))
    movie: Mapped["Movies"] = relationship(back_populates="actors")
    # always remeber it has to be the classname in Mapped
