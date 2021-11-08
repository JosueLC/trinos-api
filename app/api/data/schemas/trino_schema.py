# Trino Pydantic Schema
#-------------------------------------------------------
# Pydantic Schemas for Trino Model Class (api/data/models/trino_model.py)
#-------------------------------------------------------
# Types of Trino Schemas:
#   - TrinoBase
#   - TrinoCreate
#   - TrinoUpdate
#   - TrinoRead
#   - TrinoList
#   - Trino
#-------------------------------------------------------

#Python packages
from typing import List, Optional
from datetime import datetime

from sqlalchemy.sql.expression import desc
#Pydantic packages
from pydantic import BaseModel
from pydantic import Field
#Local packages
from api.data.models.trino_model import Trino

class TrinoBase(BaseModel):
    content: str = Field(..., description="Trino content")
    author: str = Field(..., description="Author ID")

class TrinoCreate(TrinoBase):
    pass

class Trino(TrinoBase):
    id: str = Field(..., description="Trino ID")
    hashtags: List[str] = Field(None, description="Hashtags of the trino")
    urls: List[str] = Field(None, description="URLs from trino's content")
    created_at: datetime = Field(None, description="Trino created")
    updated_at: datetime = Field(None, description="Trino updated")
    likes: List[str] = Field(None, description="Users that liked this trino")
    retrinos: List[str] = Field(None, description="Users that shared this trino")

    class Config:
        orm_mode = True