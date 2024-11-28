from app.utils.exceptions.invalid_credentials_error import Invalid_credentials_error
from app.utils.exceptions.user_not_found_error import User_not_found_error
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.models.user import User


def authenticate_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    
    if not user:
        raise User_not_found_error(username)
    
    if not verify_password(password, user.password):
        raise Invalid_credentials_error()

    return user


def verify_password(plain_password, hashed_password):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.verify(plain_password, hashed_password)
