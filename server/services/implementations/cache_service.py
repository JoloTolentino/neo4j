import redis.asyncio as redis
import json
from typing import Optional
from server.schemas.redis import RedisStatus, Status
from server.services.interfaces.cache_service import Redis_Cache


class Redis_Service(Redis_Cache):
    def __init__(self, url: Optional[str] = "redis://localhost:6379/0"):
        self._url = url
        self._client = redis.Redis.from_url(self._url, decode_responses=True)

    async def update_job(self, job_id: str, status: Status, description: Optional[str]) -> dict:
        data = RedisStatus(job_id=job_id,state=status, description=description)
        data = data.model_dump_json()
        await self._client.set(job_id, data)
        return data

    async def job_status(self, job_id: str) -> dict:
        data = await self._client.get(job_id)
        if data is None:
            return {
                'msg': "invalid job id"
            }
        return json.loads(data)
