from datetime import datetime

from pydantic import BaseModel


class PostBase(BaseModel):
    rubrics: list[str]
    text: str
    created_date: datetime


class PostInDB(PostBase):
    id: int
    rubrics: list[str]
    text: str
    created_date: datetime

    class Config:
        orm_mode = True
