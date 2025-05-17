from pydantic import BaseModel, Field
from enum import Enum


class Status(str, Enum):
    """
    Enumeration of possible task states in Redis.
    """
    pending = "pending"
    complete = "complete"
    fail = "failure"


class RedisStatus(BaseModel):
    """
    Represents the status of a job/task stored in Redis.
    """
    job_id: str = Field(..., description="Unique identifier of the job/task.")
    state: Status = Field(..., description="Current state of the task (pending, complete, or fail).")
    description: str = Field(..., description="Human-readable description of the task status.")



