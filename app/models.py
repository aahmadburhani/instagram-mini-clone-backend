from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base


class User(Base):
    __tablename__ = "app_users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    image_url = Column(String)
    caption = Column(Text)
    user_id = Column(Integer, ForeignKey("app_users.id"))

class Follow(Base):
    # stores follower-following relationship
    # used to generate user feed

    __tablename__ = "follows"

    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer)
    following_id = Column(Integer)

class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    post_id = Column(Integer)

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    text = Column(Text)
    user_id = Column(Integer)
    post_id = Column(Integer)
