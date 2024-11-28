from pydantic import BaseModel, Field


class PaymentRequest(BaseModel):
    """
    Datos para realizar un pago.
    """

    user_id: int = Field(..., description="ID del usuario que realiza el pago.")
    amount: float = Field(..., gt=0, description="Monto a pagar (debe ser mayor a 0).")
