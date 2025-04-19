from typing import List

from sqlalchemy import CheckConstraint, DateTime, Double, Enum, ForeignKeyConstraint, Integer, PrimaryKeyConstraint, String, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import datetime

class Base(DeclarativeBase):
    pass


class Movies(Base):
    __tablename__ = 'movies'
    __table_args__ = (
        CheckConstraint('ratings > 0::double precision AND ratings <= 5.0::double precision', name='rating constraints'),
        PrimaryKeyConstraint('uuid', name='movies_pkey'),
        UniqueConstraint('title', name='movies_title_key')
    )

    title: Mapped[str] = mapped_column(String)
    ratings: Mapped[float] = mapped_column(Double(53))
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    uuid: Mapped[str] = mapped_column(String, primary_key=True)

    Persons: Mapped[List['Persons']] = relationship('Persons', back_populates='movie')
    movie_tags: Mapped[List['MovieTags']] = relationship('MovieTags', back_populates='movies')


class Persons(Base):
    __tablename__ = 'Persons'
    __table_args__ = (
        ForeignKeyConstraint(['movie_id'], ['movies.uuid'], name='Persons_movie_id_fkey'),
        PrimaryKeyConstraint('uuid', name='Persons_pkey')
    )

    name: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)
    role: Mapped[str] = mapped_column(Enum('actor', 'director', name='roles'))
    movie_id: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    uuid: Mapped[str] = mapped_column(String, primary_key=True)

    movie: Mapped['Movies'] = relationship('Movies', back_populates='Persons')


class MovieTags(Base):
    __tablename__ = 'movie_tags'
    __table_args__ = (
        ForeignKeyConstraint(['movie_title'], ['movies.title'], name='movie_tags_movie_title_fkey'),
        PrimaryKeyConstraint('movie_title', 'tag', 'uuid', name='movie_tags_pkey')
    )

    movie_title: Mapped[str] = mapped_column(String, primary_key=True)
    tag: Mapped[str] = mapped_column(Enum('horror', 'love', 'comedy', 'action', name='movietagenums'), primary_key=True)
    uuid: Mapped[str] = mapped_column(String, primary_key=True)

    movies: Mapped['Movies'] = relationship('Movies', back_populates='movie_tags')
