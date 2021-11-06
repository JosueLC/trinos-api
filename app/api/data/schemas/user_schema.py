#Python packages
from typing import List, Optional
from datetime import datetime
#Pydantic packages
from pydantic import BaseModel
#Local packages
from .trino_schema import Trino

class UserBase(BaseModel):
    email: str
    nickname: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: str
    created_at: datetime
    first_name: str
    last_name: str
    trinos: List[Trino] = []

    class Config:
        orm_mode = True