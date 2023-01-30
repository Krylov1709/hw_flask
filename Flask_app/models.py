import atexit
from sqlalchemy import Column, String, DateTime, Text, Integer, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime


PG_DSN = 'postgresql://postgres:Rhskjd@localhost:5432/flask_app'
engine = create_engine(PG_DSN)
Base = declarative_base(bind=engine)


class UserModel(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)


class ArticleModel(Base):
    __tablename__ = "article"
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    creation_time = Column(DateTime, default=datetime.now)
    id_user = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship(UserModel, backref="article")


Base.metadata.create_all()
Session = sessionmaker(bind=engine)
atexit.register(engine.dispose)


