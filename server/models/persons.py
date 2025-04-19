import enum
from sqlalchemy import String,Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from server.models.base import Base, TimestampMixin
# from server.models.movies import Movies
from sqlalchemy import Enum

# foreign key is some key that referes to the primary key of another table


class Roles(enum.Enum):
    actor = "actor"
    director = "director"


class Person(TimestampMixin, Base):
    __tablename__ = 'Persons'
    name: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)
    role: Mapped[Roles] = mapped_column(Enum(Roles), nullable=False)
    movie_id: Mapped[str] = mapped_column(ForeignKey("movies.uuid"))
    movie: Mapped["movies"] = relationship(back_populates="actor")
