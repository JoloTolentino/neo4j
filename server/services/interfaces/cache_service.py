from abc import ABC, abstractmethod
from server.schemas.redis import RedisStatus,Status
from typing import Optional



class Redis_Cache(ABC):
    @abstractmethod
    def update_job(self,job_id:str,status:Status, description:Optional[str]) -> RedisStatus:
        '''Updates the status of the job'''
        pass # pragma: no cover

    @abstractmethod
    def job_status(self, job_id:str) -> RedisStatus:
        '''Gets the current status of a job'''
        pass # pragma: no cover


    