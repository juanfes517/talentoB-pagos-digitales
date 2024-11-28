from app.crud.bank_account import process_payment
from app.schemas.payment import PaymentRequest
from app.security.token import verify_token
from app.security.token import oauth2_scheme
from app.schemas.response import Response
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(prefix="/bank_account", tags=["bank_account"])


@router.post("/payments", response_model=Response)
async def make_payment(
    payment: PaymentRequest,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme),
):
    """
    Endpoint para realizar un pago.
    """
    username = verify_token(token) 
    account = process_payment(db, user_id=payment.user_id, amount=payment.amount)
    return Response(
        status="Successful",
        data={"user_id": payment.user_id, "new_balance": account.available_balance},
    )
