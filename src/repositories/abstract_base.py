from abc import ABC, abstractmethod
from typing import Type, TypeVar
from pydantic import BaseModel
from db.config import Base
from sqlalchemy.ext.asyncio import AsyncSession

ModelType = TypeVar("ModelType", bound=Base)
create_schema = TypeVar("create_schema", bound=BaseModel)


class ABSRepo(ABC):
    @abstractmethod
    def __init__(self, model: Type[ModelType]):
        pass

    @abstractmethod
    def create(self, db: AsyncSession, obj_in: create_schema) -> ModelType:
        pass
