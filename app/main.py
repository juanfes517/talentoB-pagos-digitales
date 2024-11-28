from fastapi import FastAPI
from app.database import engine, Base
from app.routers import bank_account, auth
from app.utils.exceptions import *
from jose import JWTError

app = FastAPI()
app.include_router(bank_account.router)
app.include_router(auth.router)

app.add_exception_handler(Insufficient_balance_error, insufficient_balance_handler)
app.add_exception_handler(Account_not_found_error, account_not_found_handler)
app.add_exception_handler(User_not_found_error, user_not_found_handler)
app.add_exception_handler(Invalid_field_error, invalid_field_error_handler)
app.add_exception_handler(Invalid_credentials_error, invalid_credentials_error_handler)
app.add_exception_handler(JWTError, JWTError_handler)

Base.metadata.create_all(engine)


@app.get("/")
def root():
    return {"message": "API activa"}

