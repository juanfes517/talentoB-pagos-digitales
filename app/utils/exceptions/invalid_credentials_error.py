class Invalid_credentials_error(Exception):
  """
  Error para credenciales incorrectas
  """
  def __init__(self):
    super().__init__("Invalid username or password")