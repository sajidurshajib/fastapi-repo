from typing import List
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
        async def get():
            return [{"id": 1,
                     "title": "Demo",
                     "body": "Demo body"}]

    def post(self):
        @self.router.post('', response_model=self.response_schema)
        async def post(data_in: self.request_schema, db=Depends(get_session)):
            result = await self.repo.create(db, data_in)
            print(result)
            return result

    def get_one(self):
        @self.router.get('/{id}', response_model=self.response_schema)
        async def get(id: int):
            return {"id": 1,
                    "title": "Demo",
                    "body": "Demo body"}

    def put(self):
        @self.router.put('/{id}', response_model=self.response_schema)
        async def put(id: int, update_in: self.request_schema):
            return {"id": 1,
                    "title": "Demo",
                    "body": "Demo body"}

    def delete(self):
        @self.router.delete('/{id}')
        async def delete(id: int):
            return {'msg': 'deleted'}
