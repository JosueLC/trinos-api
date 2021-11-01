#Python packages
from typing import List, Optional
from datetime import datetime
#Pydantic packages
from pydantic import BaseModel
#Local packages
from .user_schema import UserBase

class TrinoBase(BaseModel):
    content: str

class TrinoCreate(TrinoBase):
    pass

class Trino(TrinoBase):
    id: str
    owner: UserBase
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True