from pydantic import BaseModel
from db.config import Base
from repositories import ABSRepo
from typing import Generic, Type, TypeVar
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.encoders import jsonable_encoder

ModelType = TypeVar("ModelType", bound=Base)
create_schema = TypeVar("create_schema", bound=BaseModel)


class Repo(Generic[ModelType, create_schema], ABSRepo):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def create(self, db: AsyncSession, obj_in: create_schema) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)

        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj
