from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from auth.cognito_auth import CognitoAuthProvider, AuthError


class DummyCognitoClient:
    def __init__(self):
        self.sign_up_calls = []
        self.initiate_auth_calls = []
        self.list_users_calls = []
        self.confirm_sign_up_calls = []
        self.resend_calls = []

    
    def sign_up(self, **kwargs):
        self.sign_up_calls.append(kwargs)
        return {"UserConfirmed": False}

    def initiate_auth(self, **kwargs):
        self.initiate_auth_calls.append(kwargs)
        return {
            "AuthenticationResult": {
                "AccessToken": "access-token",
                "RefreshToken": "refresh-token",
            }
        }

    def list_users(self, **kwargs):
        self.list_users_calls.append(kwargs)
        return {
            "Users": [
                {
                    "Username": "abc123",
                    "Attributes": [
                        {"Name": "email", "Value": kwargs.get("Filter", "").split('"')[1]},
                        {"Name": "name", "Value": "Test User"},
                    ],
                    "UserStatus": "CONFIRMED",
                }
            ]
        }

    def confirm_sign_up(self, **kwargs):
        self.confirm_sign_up_calls.append(kwargs)
        return {}

    def resend_confirmation_code(self, **kwargs):
        self.resend_calls.append(kwargs)
        return {}


@pytest.fixture
def fake_env(monkeypatch):
    monkeypatch.setenv("AWS_REGION", "us-west-2")
    monkeypatch.setenv("COGNITO_USER_POOL_ID", "pool")
    monkeypatch.setenv("COGNITO_CLIENT_ID", "client")


@pytest.fixture
def provider(monkeypatch, fake_env):
    dummy = DummyCognitoClient()

    def fake_client(service_name, region_name=None):
        assert service_name == "cognito-idp"
        return dummy

    monkeypatch.setattr("auth.cognito_auth.boto3.client", fake_client)
    return CognitoAuthProvider(), dummy


def test_missing_environment_variables(monkeypatch):
    monkeypatch.delenv("AWS_REGION", raising=False)
    monkeypatch.delenv("COGNITO_USER_POOL_ID", raising=False)
    monkeypatch.delenv("COGNITO_CLIENT_ID", raising=False)
    with pytest.raises(RuntimeError):
        CognitoAuthProvider()


def test_register_user_validates_email_domain(provider):
    cognito, dummy = provider
    with pytest.raises(AuthError) as excinfo:
        cognito.register_user("Full Name", "user@gmail.com", "Password1")
    assert "csu.fullerton.edu" in str(excinfo.value)
    assert dummy.sign_up_calls == []


def test_authenticate_user_returns_tokens_and_profile(provider):
    cognito, dummy = provider
    result = cognito.authenticate_user("student@csu.fullerton.edu", "Password1")
    assert result["tokens"]["AccessToken"] == "access-token"
    assert result["user"] == {
        "email": "student@csu.fullerton.edu",
        "full_name": "Test User",
    }
    assert dummy.initiate_auth_calls
    assert dummy.list_users_calls


def test_resend_confirmation_invokes_client(provider):
    cognito, dummy = provider
    cognito.resend_confirmation("student@csu.fullerton.edu")
    assert dummy.resend_calls