from sqlalchemy import delete, update
from sqlalchemy.future import select
from pydantic import BaseModel
from db.config import Base
from repositories import ABSRepo
from typing import Generic, Type, TypeVar, Union
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

    async def read(self, db: AsyncSession) -> ModelType:
        query = select(self.model)
        result = await db.execute(query)
        c = result.scalars()
        return list(c)

    async def update(self, db: AsyncSession, id: int, update_in: create_schema) -> ModelType:
        query = update(self.model).where(self.model.id == id).values(
            **update_in.dict(exclude_unset=True))
        result = await db.execute(query)
        await db.commit()
        data = None
        if result.rowcount:
            data = await self.get_by_id(db, id)
        return data

    async def delete(self, db: AsyncSession, id: Union[str, int]) -> ModelType:
        query = delete(self.model).where(self.model.id == id)
        result = await db.execute(query)
        await db.commit()
        return result

    async def get_by_id(self, db: AsyncSession, id: int) -> ModelType:
        query = select(self.model).filter_by(id=id).limit(1)
        result = await db.execute(query)
        c = result.scalars().first()
        return c
