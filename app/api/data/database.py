#SQLAlchemy packages
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#SQLite database url
SQLALCHEMY_DATABASE_URL = 'sqlite:///data.db'

#sqlite engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False})

#Session local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base Model
Base = declarative_base()