from pydantic import BaseModel
from enum import Enum


class StatusEnums(str, Enum):
    success = "success"
    failure = "failure"


class Transaction_Logs(BaseModel):
    uuid: str
    endpooint: str
    args: list[str]
    status: StatusEnums
