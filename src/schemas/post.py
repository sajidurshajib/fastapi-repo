from pydantic import BaseModel

class PostIn(BaseModel):
    title: str
    body: str

class PostOut(BaseModel):
    id: int
    title: str
    body: str
