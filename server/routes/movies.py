from fastapi import APIRouter, Depends, status, HTTPException, File, UploadFile
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from server.models import Movies as MoviesModel, Person as PersonModel
from server.services.implementations.movie_service import MovieService
from server.services.implementations.upload_service import UploadService
from server.services.interfaces.movie_service import AbstractMovieService
from server.services.interfaces.s3_service import S3Service, AWSRegion
from server.schemas.movies import Movies as MoviesSchema, MovieInput
from server.extensions import get_pg_session
from typing import Union
from pydantic import BaseModel

router = APIRouter()


def get_movie_service(db: Session = Depends(get_pg_session)) -> Session:
    return MovieService(db)


def get_upload_service() -> Session:
    return UploadService(AWSRegion.US_EAST_1)


@router.post("/add", response_model=MoviesSchema, status_code=status.HTTP_201_CREATED)
def add_movie(
    movie_data: MovieInput, service: AbstractMovieService = Depends(get_movie_service)
) -> MoviesSchema:
    return service.add_movie(movie_data)


@router.get(
    "/all",
    status_code=status.HTTP_206_PARTIAL_CONTENT,
)
async def list_movies(
    service: AbstractMovieService = Depends(get_movie_service),
):
    return await service.list_movies()


# using ... in file means its required
@router.post("/upload", status_code=status.HTTP_200_OK)
async def upload_file(
    file: UploadFile = File(...), service: S3Service = Depends(get_upload_service)
) -> JSONResponse:
    try: 
        service.upload_file(file)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"status": status.HTTP_200_OK, "msg": "Successful"}
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            content = {'status': status.HTTP_500_INTERNAL_SERVER_ERROR, 'msg': str(e)}    
        )


@router.get("/")
def health_check():
    return {"message": "Working"}
