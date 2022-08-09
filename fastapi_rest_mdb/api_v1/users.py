from fastapi import APIRouter, Depends
from fastapi_rest_mdb.app.db import get_db

from fastapi_rest_mdb.logics.user_logic import UserLogic

from motor.motor_asyncio import AsyncIOMotorDatabase

router = APIRouter(prefix="/users")


def _get_user_logic(db: AsyncIOMotorDatabase = Depends(get_db)) -> UserLogic:
    return UserLogic(db)


@router.get("/", tags=["users"])
async def read_users(user_logic: UserLogic = Depends(_get_user_logic)):
    return [model.dict() async for model in user_logic.all()]


@router.post("/", tags=["users"])
async def new_user(username: str, user_logic: UserLogic = Depends(_get_user_logic)):
    await user_logic.new(username)
    return {}


@router.get("/me", tags=["users"])
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}
