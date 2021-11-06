#Python packages
import uuid
#SQLAlchemy packages
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship

#Base model package
from ..database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(String(36), primary_key=True,default=lambda:str(uuid.uuid4()))  
    nickname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    created_at = Column(DateTime, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)

    #Relationships
    trinos = relationship('Trino', back_populates='owner')
