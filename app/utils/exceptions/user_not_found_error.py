class User_not_found_error(Exception):
    """
    Error para usuario no encontrado
    """

    def __init__(self, username):
        super().__init__(f"No user found with username: {username}")