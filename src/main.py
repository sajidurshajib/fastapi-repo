from fastapi import FastAPI
from routes import (
    post_route,
    catagory_route
)


app = FastAPI()


@app.get('/')
async def index():
    return {"msg": "Hello FastAPI"}


app.include_router(catagory_route)
app.include_router(post_route.router)
