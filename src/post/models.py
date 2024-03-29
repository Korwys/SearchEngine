from sqlalchemy import Column, Integer,Text, DateTime, ARRAY

from config.db_config import Base


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True, index=True)
    rubrics = Column(ARRAY(Text()), nullable=False)
    text = Column(Text, nullable=False)
    created_date = Column(DateTime, nullable=False)
