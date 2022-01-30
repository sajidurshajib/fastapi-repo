from routes import BaseRoute
from schemas import PostOut, PostIn
from repositories import PostRepo

post_route = BaseRoute(
    prefix='/post', repo=PostRepo, request_schema=PostIn, response_schema=PostOut)
