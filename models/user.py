#Python packages
from typing import Optional
from uuid import UUID
from datetime import date
#Pydantic packages
from pydantic import BaseModel
from pydantic import Field,EmailStr

#Classes for User
class UserBase(BaseModel):
    id: UUID = Field(
        ...,
        title="User ID"
        )
    username: str = Field(
        ...,
        title="Username"
        )
    email: EmailStr = Field(
        ...,
        title="Email"
        )
class UserLogin(UserBase):
    password: str = Field(
        ...,
        title="Password",
        min_length=8,
        max_length=64
        )
class User(UserBase):
    first_name: str = Field(
        ...,
        title="First Name",
        max_length=50,
        min_length=2
        )
    last_name: str = Field(
        ...,
        title="Last Name",
        max_length=50,
        min_length=2
        )
    birth_date: Optional[date] = Field(
        default=None,
        title="Birth Date"
        )
