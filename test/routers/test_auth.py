import pytest
from fastapi.testclient import TestClient
from app.main import app  
from app.models.user import User
from unittest.mock import MagicMock

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

@pytest.fixture
def mock_db():
    db = MagicMock()
    yield db
    
@pytest.fixture
def mock_authenticate_user(mocker):
    mock_user = User(username="testuser", first_name="juan", last_name="escobar")
    mocker.patch("app.routers.auth.authenticate_user", return_value=mock_user)
    return mock_user

def test_login(client, mock_db, mock_authenticate_user):
    # Arrange
    login_data = {
        "username": "testuser",
        "password": "testpassword"
    }

    # Act
    response = client.post("/auth/login", data=login_data)

    # Assert
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"