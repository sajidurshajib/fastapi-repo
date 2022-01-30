from fastapi import APIRouter


catagory_route = APIRouter(prefix='/catagory', tags=['Catagory'])

@catagory_route.get('')
async def all():
    return {'msg': 'All catagories'}

@catagory_route.post('')
async def insert():
    return {'msg':'Insert a catagory'}