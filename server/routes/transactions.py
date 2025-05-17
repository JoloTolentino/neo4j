
from fastapi import APIRouter,Depends
from server.services.implementations.cache_service import Redis_Service
from server.extensions import get_cache
from server.schemas.redis import RedisStatus



router = APIRouter()


@router.post('/job/{job_id}')
async def register(job_id: str,details:RedisStatus, cache:Redis_Service = Depends(get_cache))->dict: 
    return await cache.update_job(
        job_id = job_id,
        status=  details.state,
        description = details.description,
    )
@router.get('/job/{job_id}')
async def retrieve(job_id:str,cache:Redis_Service = Depends(get_cache))->dict: 
    return await cache.job_status(job_id)