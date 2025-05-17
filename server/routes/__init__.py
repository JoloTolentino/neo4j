from fastapi import APIRouter
from .movies import router as movie_routes
from .transactions import router as cache_service


router = APIRouter()
router.include_router(movie_routes, prefix="/movies", tags=["Movies"])
router.include_router(cache_service, prefix="/status",tags=['Status'])