from server.models.persons import movie_roles
from server.schemas.base import Base, Timestamp
from pydantic import BaseModel


class PersonInput(BaseModel):
    name: str
    age: int
    role: movie_roles


class Person(PersonInput, Base, Timestamp):
    class Config:
        orm_mode = True
