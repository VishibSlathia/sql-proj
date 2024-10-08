from sqlalchemy.orm import Session
from . import models
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(db: Session, username: str, email: str, password: str):
    hashed_password = generate_password_hash(password)
    db_user = models.User(username=username, email=email, password_hash=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user or not check_password_hash(user.password_hash, password):
        return None
    return user

def get_user_query_history(db: Session, user_id: int, limit: int = 10):
    return db.query(models.QueryHistory).filter(models.QueryHistory.user_id == user_id).order_by(models.QueryHistory.created_at.desc()).limit(limit).all()