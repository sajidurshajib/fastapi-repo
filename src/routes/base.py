from typing import List
from unittest import result
from repositories import Repo
from pydantic import BaseModel
from routes import ABSRoute
from fastapi import APIRouter, Depends
from db.config import get_session


class BaseRoute(ABSRoute):
    def __init__(self, prefix: str, repo: Repo, request_schema: BaseModel, response_schema: BaseModel):

        self.router = APIRouter(prefix=prefix, tags=[
                                "".join(prefix.split('/')).title()])

        self.repo = repo

        self.request_schema = request_schema
        self.response_schema = response_schema
        self.initialize_routes()

    def initialize_routes(self):
        self.get()
        self.post()
        self.get_one()
        self.put()
        self.delete()

    def get(self):
        @self.router.get('', response_model=List[self.response_schema])
        async def get(db=Depends(get_session)):
            read = await self.repo.read(db)
            return read

    def post(self):
        @self.router.post('', response_model=self.response_schema)
        async def post(data_in: self.request_schema, db=Depends(get_session)):
            result = await self.repo.create(db, data_in)
            return result

    def get_one(self):
        @self.router.get('/{id}', response_model=self.response_schema)
        async def get(id: int, db=Depends(get_session)):
            single_result = await self.repo.get_by_id(db, id)
            return single_result

    def put(self):
        @self.router.put('/{id}', response_model=self.response_schema)
        async def put(id: int, update_in: self.request_schema, db=Depends(get_session)):
            update_result = await self.repo.update(db, id, update_in)
            return update_result

    def delete(self):
        @self.router.delete('/{id}')
        async def delete(id: int, db=Depends(get_session)):
            await self.repo.delete(db, id)
            return "Deleted"
