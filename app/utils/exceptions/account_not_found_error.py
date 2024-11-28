class Account_not_found_error(Exception):
    """
    Error para cuenta de banco no encontrada
    """

    def __init__(self, user_id):
        super().__init__(f"No account found for user: {user_id}")
