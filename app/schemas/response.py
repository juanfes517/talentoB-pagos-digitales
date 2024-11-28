from pydantic import BaseModel, Field
from typing import Optional, Any


class Response(BaseModel):
    """
    Respuesta general usando el patrón 'Response Wrapper'
    """

    status: str = Field(
        ..., description="Indica cuando la respuesta fue éxito o fallo."
    )
    data: Optional[Any] = Field(
        None, description="Datos para las solicitudes exitosas."
    )
    error: Optional[dict] = Field(
        None, description="Detalles del error cuando la solicitud falla."
    )
