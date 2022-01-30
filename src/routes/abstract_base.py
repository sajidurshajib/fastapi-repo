from abc import ABC, abstractmethod
from fastapi import APIRouter
from pydantic import BaseModel

from repositories.base import Repo


class ABSRoute(ABC):
    @abstractmethod
    def __init__(
        self,
        prefix: str,
        request_schema: BaseModel,
        response_schema: BaseModel
    ):
        pass

    @abstractmethod
    def initialize_routes(self):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def get_one(self):
        pass

    @abstractmethod
    def post(self):
        pass

    @abstractmethod
    def put(self):
        pass

    @abstractmethod
    def delete(self):
        pass
