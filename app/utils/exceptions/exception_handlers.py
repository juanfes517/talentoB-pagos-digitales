from app.utils.exceptions.insufficient_balance_error import Insufficient_balance_error
from app.utils.exceptions.invalid_credentials_error import Invalid_credentials_error
from app.utils.exceptions.account_not_found_error import Account_not_found_error
from app.utils.exceptions.user_not_found_error import User_not_found_error
from app.utils.exceptions.invalid_field_error import Invalid_field_error
from fastapi.responses import JSONResponse
from app.schemas.response import Response
from fastapi import Request, status
from jose import JWTError


async def insufficient_balance_handler(
    request: Request, exc: Insufficient_balance_error
):
    """
    Maneja errores de saldo insuficiente.
    """

    content = Response(
        status="Failed",
        error={"status_code": status.HTTP_409_CONFLICT, "message": str(exc)},
    ).model_dump()
    return JSONResponse(content=content, status_code=status.HTTP_409_CONFLICT)


async def account_not_found_handler(request: Request, exc: Account_not_found_error):
    """
    Maneja errores de cuenta no encontrada.
    """
    content = Response(
        status="Failed",
        error={"status_code": status.HTTP_404_NOT_FOUND, "message": str(exc)},
    ).model_dump()
    return JSONResponse(content=content, status_code=status.HTTP_404_NOT_FOUND)


async def user_not_found_handler(request: Request, exc: User_not_found_error):
    """
    Maneja errores de usuario no encontrada.
    """
    content = Response(
        status="Failed",
        error={"status_code": status.HTTP_404_NOT_FOUND, "message": str(exc)},
    ).model_dump()
    return JSONResponse(content=content, status_code=status.HTTP_404_NOT_FOUND)


async def invalid_field_error_handler(request: Request, exc: Invalid_field_error):
    """
    Maneja errores de campos no validos.
    """
    content = Response(
        status="Failed",
        error={
            "status_code": status.HTTP_422_UNPROCESSABLE_ENTITY,
            "message": str(exc),
        },
    ).model_dump()
    return JSONResponse(
        content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
    )


async def invalid_credentials_error_handler(
    request: Request, exc: Invalid_credentials_error
):
    """
    Maneja errores de credenciales no validas.
    """
    content = Response(
        status="Failed",
        error={
            "status_code": status.HTTP_401_UNAUTHORIZED,
            "message": str(exc),
        },
    ).model_dump()
    return JSONResponse(content=content, status_code=status.HTTP_401_UNAUTHORIZED)


async def JWTError_handler(request: Request, exc: JWTError):
    """
    Maneja errores relacionados con el token.
    """
    content = Response(
        status="Failed",
        error={
            "status_code": status.HTTP_401_UNAUTHORIZED,
            "message": str(exc),
        },
    ).model_dump()
    return JSONResponse(content=content, status_code=status.HTTP_401_UNAUTHORIZED)
