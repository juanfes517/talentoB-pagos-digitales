class Insufficient_balance_error(Exception):
    """
    Error para saldo insuficiente
    """

    def __init__(self, mount):
        super().__init__(f"the action cannot be performed with: {mount}")
