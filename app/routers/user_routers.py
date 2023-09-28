from typing import List

from fastapi import APIRouter

from app.schemas.user_schemas import ErrorOutput, StandardOutput, UserListOutput
from app.views.user_view import UserView

user_router = APIRouter(prefix="/user")

user_router.get(
    "/list",
    response_model=List[UserListOutput],
    responses={400: {"model": ErrorOutput}},
)(UserView.list_user)

user_router.post(
    "/create",
    response_model=StandardOutput,
    responses={400: {"model": ErrorOutput}},
)(UserView.user_create)

user_router.post(
    "/favorite/add",
    response_model=StandardOutput,
    responses={400: {"model": ErrorOutput}},
)(UserView.add_favorite)

user_router.delete(
    "/delete/{id}",
    response_model=StandardOutput,
    responses={400: {"model": ErrorOutput}},
)(UserView.user_delete)

user_router.delete(
    "/delete/favorite/{id}",
    response_model=StandardOutput,
    responses={400: {"model": ErrorOutput}},
)(UserView.remove_favorite)
