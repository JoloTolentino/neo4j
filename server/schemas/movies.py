from server.schemas.base import Base, Timestamp
from server.schemas.persons import PersonInput
from server.models import MovieTagEnums
from pydantic import BaseModel, field_validator, field_serializer
from pydantic import SerializationInfo
from typing import Any


class MovieTagInput(BaseModel):
    tag: MovieTagEnums


class MovieInput(BaseModel):
    title: str
    actors: list[PersonInput]
    tags: list[MovieTagInput]  # cant be a string cuz model expects a sa object
    ratings: float

    @field_validator("title")
    @classmethod
    def is_title(cls, val):
        if not isinstance(val, str):
            raise ValueError("title has invalid format")
        return val

    @field_validator("ratings")
    @classmethod
    def only_float_values(cls, values):
        if not isinstance(values, float):
            raise ValueError("ratings must be float values")
        return values


class Movies(MovieInput, Base, Timestamp):
    class Config:
        orm_mode = True
