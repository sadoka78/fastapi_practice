from sqlalchemy import Column , Integer, String,DateTime,ForeignKey
from sqlalchemy.orm import declarative_base,relationship
from datetime import datetime


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True, index = True)
    username =Column(String, unique=True,index=True,nullable=False)
    hashed_password= Column(String, nullable=False)
    role = Column(String, default="user")
    notes=relationship('Note',back_populates='owner',cascade="all, delete-orphan")
from sqlalchemy.sql import func

class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship('User', back_populates='notes')
