from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)

    @property
    def serialize(self):
        return {
            'title': self.title,
            'content': self.content
        }


engine = create_engine('')
Base.metadata.create_all(engine)
