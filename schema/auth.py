from pydantic import BaseModel


class BaseUser(BaseModel):
    user_name: str


class User(BaseUser):
    id: int

    class Config:
        orm_mode = True
