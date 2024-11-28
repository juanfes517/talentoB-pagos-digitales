from app.utils.validations.model_validation import validate_email
from sqlalchemy.orm import validates, relationship
from sqlalchemy import Column, Integer, String
from app.database import Base


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String(10), unique=True, nullable=False)
    password = Column(String(100))
    first_name = Column(String(30))
    last_name = Column(String(30))
    email = Column(String(50), unique=True, nullable=False)

    bank_account = relationship("Bank_account", back_populates="owner", uselist=False)

    @validates("email")
    def validate_email_field(self, key, value):
        validate_email(value)
