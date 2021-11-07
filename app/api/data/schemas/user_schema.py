# User Pydantic Schema
#-------------------------------------------------------
# Pydantic Schemas for User Model Class (api/data/models/user_model.py)
#-------------------------------------------------------
# Types of User Schemas:
#   - UserBase
#   - UserCreate
#   - UserUpdate
#   - UserRead
#   - UserList
#   - User
#-------------------------------------------------------

#Python packages
from typing import List
from datetime import datetime
#Pydantic packages
from pydantic import BaseModel
from pydantic import Field,EmailStr
#Local packages
from api.data.models.user_model import User

class UserBase(BaseModel):
    username: str = Field(..., description="User's username")
    email: EmailStr = Field(..., description="User's email")
    active: bool = Field(..., description="User's active status")

class UserCreate(UserBase):
    password: str = Field(..., description="User's password")

class UserRead(UserBase):
    pass

class UserList(BaseModel):
    users: List[UserRead]
    total: int

class User(UserRead):
    id: str = Field(..., description="User's id")
    first_name: str = Field(None, description="User's first name")
    last_name: str = Field(None, description="User's last name")
    bio : str = Field(None, description="User's bio")
    image_url : str = Field(None, description="User's image url")
    created_at : datetime = Field(None, description="User's created'")
    birth_date : datetime = Field(None, description="User's' birth date")
    is_admin : bool = Field(None, description="User's admin status")
    is_active : bool = Field(None, description="User's active status")