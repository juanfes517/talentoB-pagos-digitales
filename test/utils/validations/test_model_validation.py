import pytest
from app.utils.validations.model_validation import (
    validate_account_number,
    validate_email_field,
)
from app.utils.exceptions.invalid_field_error import Invalid_field_error
from email_validator import EmailNotValidError


def test_validate_account_number_valid():
    # Arrange
    valid_account_number = "123-456789-01"

    # Act
    result = validate_account_number(valid_account_number)

    # Assert
    assert result == valid_account_number


def test_validate_account_number_invalid():
    # Arrange
    invalid_account_number = "123-45678-01"

    # Act
    with pytest.raises(Invalid_field_error) as exc_info:
        validate_account_number(invalid_account_number)

    # Assert
    assert (
        str(exc_info.value) == "The account number is not in the format 'xxx-xxxxxx-xx'"
    )


def test_validate_email_field_valid():
    # Arrange
    valid_email = "juanfes@mail.com"

    # Act
    result = validate_email_field(valid_email)

    # Assert
    assert result == valid_email


def test_validate_email_field_invalid():
    # Arrange
    invalid_email = "juanfes"

    # Act
    with pytest.raises(EmailNotValidError) as exc_info:
        validate_email_field(invalid_email)

    # Assert
    assert (
        str(exc_info.value) == "Invalid email: An email address must have an @-sign."
    )
