# User model
# ----------------------------------------------------------------
# SQLAlchemy model for the User table
# ----------------------------------------------------------------
# User table structure:
#   id: unique user id : uuid
#   username: unique username : string
#   password: hashed password : string
#   email: unique email : string
#   first_name: first name : string
#   last_name: last name : string
#   created_at: date of creation : datetime
#   bio: user bio : string
#   image_url: user image url : string
#   birth_date: user birth date : datetime
#   is_admin: boolean : boolean
#   is_active: boolean : boolean
#   
#   One-to-many relationship with Trinos table
#   One-to-many relationship with Likes table

#Python packages
from typing import List, Optional
from uuid import uuid4
#SQLAlchemy packages
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, Text, Date
from sqlalchemy.orm import relationship
#Local packages
from ..database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(String(36), primary_key=True, default=str(uuid4()))
    username = Column(String(20), unique=True, nullable=False)
    password = Column(String(60), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    created_at = Column(DateTime, nullable=False)
    bio = Column(Text, nullable=True)
    image_url = Column(String(100), nullable=True)
    birth_date = Column(Date, nullable=True)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    trinos = relationship('Trino', backref='user', lazy=True)
    likes = relationship('Like', backref='user', lazy=True)
