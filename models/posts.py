from sqlalchemy import Column, Integer, String, Text, DateTime, ARRAY

from models.db_config import Base


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    rubrics = Column(ARRAY(String), nullable=False)
    text = Column(Text, nullable=False)
    created_date = Column(DateTime, nullable=False)
