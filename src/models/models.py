from sqlalchemy import Column, String, Text
from .base_model import BaseModel


class Post(BaseModel):
    __tablename__ = "posts"
    title = Column(String(255), nullable=False)
    body = Column(Text, nullable=False)
