#Python packages
from datetime import datetime
from typing import Optional
from uuid import UUID
#Pydantic packages
from pydantic import BaseModel
from pydantic import Field
#Local packages
from models.user import User

#Classes for Trino Model
class Trino(BaseModel):
    id: UUID = Field(
        ...,
        title="Trino Id"
        )
    content: str = Field(
        ...,
        title="Trino content",
        min_length=1,
        max_length=256
        )
    create_at: datetime = Field(
        default=datetime.now(),
    )
    update_at: Optional[datetime] = Field(
        default=datetime.now(),
    )
    by: User = Field(
        ...,
        title="User who created the trino"
        )
