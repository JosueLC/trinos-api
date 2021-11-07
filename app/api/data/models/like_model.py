# Like model
# ------------------------------------------------
# SQLAlchemy model for the likes table
# ------------------------------------------------
# Like table structure:
#   tweet_id: unique id of the tweet : uuid
#   user_id: unique id of the user : uuid
#   created_at: date and time of the like : datetime
#   updated_at: date and time of the like : datetime
#
#   Primary key: tweet_id, user_id
#
#   Foreign keys:
#       tweet_id: tweet.id
#       user_id: user.id
# ------------------------------------------------

#Python packages

#SQLAlchemy packages
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
#Local packages
from ..database import Base

class Like(Base):
    __tablename__ = 'likes'
    tweet_id = Column(String(36), ForeignKey('tweets.id'), primary_key=True)
    user_id = Column(String(36), ForeignKey('users.id'), primary_key=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    