#Tweet model
#-------------------------------------------------------
# SQLAlchemy model for the Tweets table
#-------------------------------------------------------
# Tweet table structure:
#   id: unique id for each tweet : uuid
#   text: text of the tweet
#   user_id: id of the user who posted the tweet
#   created_at: date and time of the tweet
#   updated_at: date and time of the last update
#   likes: list of users who liked the tweet
#   retweets: list of users who retweeted the tweet
#   replies: list of users who replied to the tweet
#   hashtags: list of hashtags used in the tweet
#   urls: list of urls used in the tweet
#   mentions: list of users mentioned in the tweet
#   media: list of media used in the tweet
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

class Tweet(Base):
    __tablename__ = 'tweets'
    id = Column(String(36), primary_key=True, default=str(uuid4()))
    text = Column(String(280))
    user_id = Column(String(36), ForeignKey('users.id'))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    hashtags = Column(JSON)
    urls = Column(JSON)
    mentions = Column(JSON)
    media = Column(JSON)
    likes = relationship('Like', back_populates='tweet')
    retweets = relationship('Retweet', back_populates='tweet')
    replies = relationship('Reply', back_populates='tweet')
    