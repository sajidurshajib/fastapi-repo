from imp import reload
import uvicorn
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


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1",
                port=8000, reload=True, log_level="info")
