from decimal import Decimal
from sqlalchemy.orm import Session
from app.models.bank_account import Bank_account
from app.utils.exceptions.insufficient_balance_error import Insufficient_balance_error
from app.utils.exceptions.account_not_found_error import Account_not_found_error


def process_payment(db: Session, user_id, amount):
    """
    Realiza un pago desde la cuenta bancaria de un usuario.
    """
    account = db.query(Bank_account).filter(Bank_account.user_id == user_id).first()

    if not account:
        raise Account_not_found_error(user_id)

    if account.available_balance < amount:
        raise Insufficient_balance_error(amount)

    account.available_balance -= Decimal(amount)
    db.commit()
    db.refresh(account)

    return account
