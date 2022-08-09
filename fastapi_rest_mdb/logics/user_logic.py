from typing import AsyncGenerator
from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorCollection
from pydantic import BaseModel

class UserModel(BaseModel):

    usermame: str

    
class UserLogic:

    def __init__(self, db: AsyncIOMotorDatabase) -> None:
        self._collection: AsyncIOMotorCollection = db.users

    async def all(self) -> AsyncGenerator[UserModel, None]:
        async for doc in self._collection.find({}):
            yield UserModel(**doc)

    async def new(self, username) -> None:
        model = UserModel(usermame=username)
        self._collection.insert_one(model.dict())