#Python packages

#SQLAlchemy packages
from sqlalchemy.orm import Session

#Local packages
from ..schemas import user_schema
from ..models import user_model

def get_user(db: Session, user_id: str):
    return db.query(user_model.User).filter(user_model.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(user_model.User).filter(user_model.User.email == email).first()

def get_user_by_nickname(db: Session, nickname: str):
    return db.query(user_model.User).filter(user_model.User.nickname == nickname).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_model.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: user_schema.UserCreate):
    db_user = user_model.User(
        email=user.email,
        nickname=user.nickname,
        password=user.password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user