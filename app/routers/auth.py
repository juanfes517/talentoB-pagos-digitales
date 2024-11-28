from fastapi.security import OAuth2PasswordRequestForm
from app.security.token import create_access_token
from app.crud.user import authenticate_user
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from typing import Annotated

router = APIRouter(prefix="/auth", tags=["login"])


@router.post("/login")
def login(
    login_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db),
):
    user = authenticate_user(
        db=db, username=login_data.username, password=login_data.password
    )

    access_token = create_access_token(
        data={
            "sub": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
        }
    )

    return {"access_token": access_token, "token_type": "bearer"}

