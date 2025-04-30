from abc import ABC, abstractmethod


class AbstractMovieService(ABC):
    @abstractmethod
    def add_movie(self, data: dict):
        pass

    @abstractmethod
    def list_movies(self):
        pass
