from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from server.models import Movies as MoviesModel, Person as PersonModel
from server.services.implementations.movie_service import MovieService
from server.services.interfaces.movie_service import AbstractMovieService
from server.schemas.movies import Movies as MoviesSchema, MovieInput
from server.extensions import get_pg_session

router = APIRouter()


def get_movie_service(db: Session = Depends(get_pg_session)) -> Session:
    return MovieService(db)


@router.post("/add", response_model=MoviesSchema, status_code=status.HTTP_201_CREATED)
def add_movie(
    movie_data: MovieInput, service: AbstractMovieService = Depends(get_movie_service)
) -> MoviesSchema:
    return service.add_movie(movie_data)


@router.get(
    "/all",
    response_model=list[MoviesSchema],
    status_code=status.HTTP_206_PARTIAL_CONTENT,
)
def list_movies(
    service: AbstractMovieService = Depends(get_movie_service),
) -> list[MoviesSchema]:
    return service.list_movies()


@router.get("/")
def health_check():
    return {"message": "Working"}
