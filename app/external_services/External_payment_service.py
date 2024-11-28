import httpx


class External_payment_service:
    @staticmethod
    def simulate_payment(amount: float, user_id: int) -> bool:
        """
        Simula un pago a través de un servicio externo.
        """
        response = httpx.post(
            "https://example.com/payments", json={"user_id": user_id, "mount": amount}
        )

        return response.status_code == 200
