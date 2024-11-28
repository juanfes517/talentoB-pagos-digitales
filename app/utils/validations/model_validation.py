from email_validator import validate_email, EmailNotValidError
from app.utils.exceptions.invalid_field_error import Invalid_field_error
import re


def validate_account_number(value):
    """
    Valida que el valor siga el patrón xxx-xxxxxx-xx.
    """
    pattern = re.compile(r"^\d{3}-\d{6}-\d{2}$")
    if not pattern.match(value):
        raise Invalid_field_error(
            "The account number is not in the format 'xxx-xxxxxx-xx'"
        )
    return value


def validate_email_field(value):
    """
    Valida el correo electrónico
    """
    try:
        valid = validate_email(value)
        return valid.email
    except ValueError as e:
        raise EmailNotValidError(f"Invalid email: {e}")
