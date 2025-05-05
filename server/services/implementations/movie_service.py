from server.services.interfaces.movie_service import AbstractMovieService
from server.models import Movies as MoviesModel, Person, MovieTag, MovieTagEnums
from server.models.persons import movie_roles
from server.schemas.persons import PersonInput
from server.schemas.movies import Movies as MoviesSchema, MovieInput
from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from server.extensions import get_service
from uuid import uuid4
import pandas as pd
import pdb
import datetime


class MovieService(AbstractMovieService):
    def __init__(self, db) -> None:
        self.db = db

    def _create_time(self) -> datetime:
        return datetime.datetime.now()

    def _title_exists(self, title: str) -> bool:
        return (
            True
            if (self.db.query(MoviesModel).filter(MoviesModel.title == title).first())
            else False
        )

    def _create_actors(
        self, actor_inputs: list[PersonInput], movie_uuid: str
    ) -> list[Person]:
        return [
            Person(
                uuid=uuid4().hex,
                name=actor.name,
                age=actor.age,
                role=movie_roles(actor.role),
                movie_id=movie_uuid,
            )
            for actor in actor_inputs
        ]

    def _create_tags(self, tag_inputs, movie_title: str) -> list[MovieTag]:
        return [
            MovieTag(
                uuid=uuid4().hex,
                movie_title=movie_title,
                tag=MovieTagEnums(tag.tag),
            )
            for tag in tag_inputs
        ]

    def add_movie(self, movie: MovieInput) -> MoviesSchema:
        try:

            if self._title_exists(movie.title):
                raise ValueError("Movie Exists")

            movie_uuid = uuid4().hex
            ts = self._create_time()
            db_movie = MoviesModel(
                title=movie.title,
                ratings=movie.ratings,
                uuid=movie_uuid,
                actors=self._create_actors(movie.actors, movie_uuid),
                tags=self._create_tags(movie.tags, movie.title),
                created_at=ts,
                updated_at=ts,
            )
            self.db.add(db_movie)
            self.db.commit()
            self.db.refresh(db_movie)

            return MoviesSchema.model_validate(db_movie, from_attributes=True)

        except ValueError as ve:
            print("Validation error:\n", ve)
            raise HTTPException(status_code=400, detail=str(ve))

        except SQLAlchemyError:
            self.db.rollback()
            raise HTTPException(status_code=500, detail="Database error occurred")

        except Exception as e:
            self.db.rollback()
            raise HTTPException(
                status_code=500, detail=f"Unexpected error occurred {e}"
            )

    async def list_movies(self):
        result = await self.db.execute(select(MoviesModel))        
        return result.scalars().all() 


    async def download_movies(self):
        query = self.list_movies()
        df = await pd.read_sql(query, self.db.bind)

    def download_list(self):
        pass
