from logging import Logger
from typing import List, Optional
from fastapi import APIRouter, Depends, Request
from fastapi_rest_mdb.logics.user_logic import UserLogic, UserModel
from pydantic import BaseModel

router = APIRouter(prefix="/users")


def _get_user_logic(request: Request) -> UserLogic:
    return UserLogic(request.app.state.db)


def _get_logger(request: Request) -> Logger:
    return request.app.state.logger


class UserResponse(BaseModel):

    username: str


class UserRequest(BaseModel):

    username: str
    is_admin: Optional[bool]


@router.get("/", tags=["users"], response_model=List[UserResponse])
async def read_users(
    user_logic: UserLogic = Depends(_get_user_logic),
    logger: Logger = Depends(_get_logger),
):
    async for model in user_logic.all():
        logger.info(model)
    resp = [model.dict() async for model in user_logic.all()]
    logger.info(resp)
    return resp


@router.post("/", tags=["users"])
async def new_user(
    user_request: UserRequest,
    user_logic: UserLogic = Depends(_get_user_logic),
    logger: Logger = Depends(_get_logger),
):
    logger.info(user_request.dict())
    await user_logic.new(UserModel(**user_request.dict()))
    return {}


@router.get("/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}


@router.get("/id/{username}", tags=["users"])
async def read_id_user(username: int):
    return {"username": username}
