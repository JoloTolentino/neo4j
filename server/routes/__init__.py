from fastapi import APIRouter
from .movies import router as movie_routes


router = APIRouter()
router.include_router(movie_routes, prefix="/movies", tags=["Movies"])
