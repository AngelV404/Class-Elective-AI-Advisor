from types import SimpleNamespace
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from auth.auth_provider import AuthError
from ui.gui import App


class DummyEntry:
    def __init__(self, value):
        self._value = value

    def get(self):
        return self._value


class DummyLabel:
    def __init__(self):
        self.last_config = {}

    def configure(self, **kwargs):
        self.last_config.update(kwargs)


class DummyProvider:
    def __init__(self, tokens=None, error=None):
        self.tokens = tokens or {"tokens": {"AccessToken": "token"}}
        self.error = error
        self.auth_calls = []
        self.resend_calls = []

    def authenticate_user(self, email, password):
        self.auth_calls.append((email, password))
        if self.error is not None:
            raise self.error
        return self.tokens

    def resend_confirmation(self, email):
        self.resend_calls.append(email)


@pytest.fixture
def app(monkeypatch):
    app = App.__new__(App)
    app.auth_tokens = None
    app.current_user_email = None
    app.selectedButton = "Login"
    app.buttons = {"Home": SimpleNamespace(configure=lambda **kwargs: None)}
    clicked = []
    app.buttonClicked = lambda name: clicked.append(name)
    app._clicked = clicked
    monkeypatch.setattr("ui.gui.messagebox.showinfo", lambda *args, **kwargs: None)
    monkeypatch.setattr("ui.gui.messagebox.showerror", lambda *args, **kwargs: None)
    return app


def test_do_login_success_sets_tokens_and_navigates(app):
    provider = DummyProvider(tokens={"tokens": {"AccessToken": "ok"}})
    app.provider = provider
    frame = SimpleNamespace(
        email_entry=DummyEntry("student@csu.fullerton.edu"),
        password_entry=DummyEntry("Password1"),
        warning_label=DummyLabel(),
    )
    app.do_login(frame)
    assert provider.auth_calls == [("student@csu.fullerton.edu", "Password1")]
    assert app.auth_tokens == {"tokens": {"AccessToken": "ok"}}
    assert app.current_user_email == "student@csu.fullerton.edu"
    assert "Home" in app._clicked
    assert frame.warning_label.last_config.get("text", "") == ""


def test_do_login_failure_surfaces_warning(app):
    provider = DummyProvider(error=AuthError("Login failed"))
    app.provider = provider
    warning = DummyLabel()
    frame = SimpleNamespace(
        email_entry=DummyEntry("student@csu.fullerton.edu"),
        password_entry=DummyEntry("Password1"),
        warning_label=warning,
    )
    app.do_login(frame)
    assert provider.auth_calls == [("student@csu.fullerton.edu", "Password1")]
    assert warning.last_config.get("text") == "Login failed"


def test_do_resend_code_forwards_to_provider(app):
    provider = DummyProvider()
    app.provider = provider
    frame = SimpleNamespace(
        email_entry=DummyEntry("student@csu.fullerton.edu"),
        warning_label=DummyLabel(),
    )
    app.do_resend_code(frame)
    assert provider.resend_calls == ["student@csu.fullerton.edu"]