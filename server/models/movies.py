from sqlalchemy import String, Integer, Float, CheckConstraint
from sqlalchemy import Enum
from sqlalchemy import JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from server.models.base import Base, TimestampMixin
import enum


class MovieTagEnums(enum.Enum):
    horror = "horror"
    love = "love"
    comedy = "comedy"
    action = "action"


class MovieTag(Base):
    # composit key = movie_title + tag
    __tablename__ = "movie_tags"
    movie_title: Mapped[str] = mapped_column(
        ForeignKey("movies.title"), primary_key=True
    )
    tag: Mapped[MovieTagEnums] = mapped_column(Enum(MovieTagEnums), primary_key=True)
    movie: Mapped["Movies"] = relationship(back_populates="tags")


class Movies(TimestampMixin, Base):
    __tablename__ = "movies"
    __table_args__ = (
        CheckConstraint("ratings > 0 AND  ratings<=5.0", name="rating constraints"),
    )
    title: Mapped[str] = mapped_column(unique=True)
    actors: Mapped[list["Person"]] = relationship(
        back_populates="movie"
    )  # we creaet a link with the Person Table # does not show up in the table itself
    tags: Mapped[list[MovieTag]] = relationship(  # < ---- looking for a SA object
        back_populates="movie", cascade="all, delete-orphan"
    )
    ratings: Mapped[float] = mapped_column(Float)
