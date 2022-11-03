from sqlalchemy import Column, Integer, String, Text, DateTime

from db_config import Base


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    rubrics = Column(String(250), nullable=False)
    text = Column(Text, nullable=False)
    created_date = Column(DateTime, nullable=False)

