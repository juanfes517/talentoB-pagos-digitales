from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey
from app.utils.validations.model_validation import validate_account_number
from sqlalchemy.orm import validates, relationship
from app.models.user import User
from app.database import Base
from datetime import datetime


class Bank_account(Base):
    __tablename__ = "bank_account"

    account_id = Column(Integer, primary_key=True, index=True)
    available_balance = Column(Numeric(10, 2), default=0.00)
    account_number = Column(String(13), unique=True, nullable=False)
    createdAt = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("user.user_id"), unique=True, nullable=False)

    owner = relationship("User", back_populates="bank_account")

    @validates("account_number")
    def validate_account_number(self, key, value):
        validate_account_number(value)
