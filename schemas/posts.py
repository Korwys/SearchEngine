from datetime import datetime

from pydantic import BaseModel


class PostBase(BaseModel):
    rubrics: list[str]
    text: str
    created_date: datetime


class PostCreate(PostBase):
    rubrics: list[str]
    text: str
    created_date: datetime


class PostUpdate(PostCreate):
    rubrics: list[str] | None
    text: str | None
    created_date: datetime | None


class PostInDB(PostBase):
    id: int
    rubrics: list[str]
    text: str
    created_date: datetime

    class Config:
        orm_mode = True
