from typing import AsyncGenerator, Optional
from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorCollection
from pydantic import BaseModel


class UserModel(BaseModel):

    username: str
    is_admin: Optional[bool] = False


class UserLogic:
    def __init__(self, db: AsyncIOMotorDatabase) -> None:
        self._collection: AsyncIOMotorCollection = db.users

    async def all(self) -> AsyncGenerator[UserModel, None]:
        async for doc in self._collection.find({}):
            yield UserModel(**doc)

    async def new(self, user_model: UserModel) -> None:
        await self._collection.insert_one(user_model.dict())
