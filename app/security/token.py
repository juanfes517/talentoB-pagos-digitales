from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
from jose import JWTError, jwt
import os

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

load_dotenv()
jwt_secret_key = os.getenv("JWT_SECRET_KEY")
jwt_algorithm = os.getenv("JWT_ALGORITHM")
time_expire = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")


def create_access_token(data: dict):
    expire = datetime.now(timezone.utc) + timedelta(minutes=int(time_expire))
    data.update({"exp": expire})
    encoded_jwt = jwt.encode(data, jwt_secret_key, algorithm=jwt_algorithm)

    return encoded_jwt


def verify_token(token: str):
    payload = jwt.decode(token, jwt_secret_key, algorithms=[jwt_algorithm])
    username: str = payload.get("sub")

    if username is None:
        raise JWTError()

    return username
