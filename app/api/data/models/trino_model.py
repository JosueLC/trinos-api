#Trino model
#-------------------------------------------------------
# SQLAlchemy model for the Trinos table
#-------------------------------------------------------
# Trino table structure:
#   id: unique id for each Trino : uuid
#   text: text of the Trino
#   user_id: id of the user who posted the Trino
#   created_at: date and time of the Trino
#   updated_at: date and time of the last update
#   likes: list of users who liked the Trino
#   reTrinos: list of users who reTrinoed the Trino
#   replies: list of users who replied to the Trino
#   hashtags: list of hashtags used in the Trino
#   urls: list of urls used in the Trino
#   mentions: list of users mentioned in the Trino
#   media: list of media used in the Trino
#
#   Relationships:
#       Many-to-one relationship with the User table
#       One-to-many relationship with the Like table

#Python packages
from typing import List, Optional
from uuid import uuid4
#SQLAlchemy packages
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, Text, JSON, Float
from sqlalchemy.orm import relationship
#Local packages
from ..database import Base

class Trino(Base):
    __tablename__ = 'Trinos'
    id = Column(String(36), primary_key=True, default=str(uuid4()))
    text = Column(String(280))
    user_id = Column(String(36), ForeignKey('users.id'))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    hashtags = Column(JSON)
    urls = Column(JSON)
    mentions = Column(JSON)
    media = Column(JSON)
    likes = relationship('Like', back_populates='Trino')
    retrinos = relationship('Retrino', back_populates='Trino')
    replies = relationship('Reply', back_populates='Trino')
    