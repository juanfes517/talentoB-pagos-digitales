class Invalid_field_error(Exception):
    """
    Error para formatos de campos no validos
    """

    def __init__(self, message):
        super().__init__(message)
