#Python packages
import uuid
#SQLAlchemy packages
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship

#Base model package
from ..database import Base

class Trino(Base):
    __tablename__ = 'trinos'
    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()))
    content = Column(String(250), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)
    #Relationships
    owner = relationship('User', back_populates='trinos')