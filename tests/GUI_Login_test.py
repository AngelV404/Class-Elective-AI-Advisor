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
    def __init__(self, tokens=None, error=None, reset_error=None, change_error=None):
        self.tokens = tokens or {"tokens": {"AccessToken": "token"}}
        self.error = error
        self.reset_error = reset_error
        self.change_error = change_error
        self.auth_calls = []
        self.resend_calls = []
        self.reset_calls = []
        self.confirm_calls = []
        self.change_calls = []

    def authenticate_user(self, email, password):
        self.auth_calls.append((email, password))
        if self.error is not None:
            raise self.error
        return self.tokens

    def resend_confirmation(self, email):
        self.resend_calls.append(email)

    def start_password_reset(self, email):
        self.reset_calls.append(email)
        if self.reset_error:
            raise self.reset_error

    def confirm_password_reset(self, email, code, new_password):
        self.confirm_calls.append((email, code, new_password))
        if self.reset_error:
            raise self.reset_error

    def change_password(self, token, old_password, new_password):
        self.change_calls.append((token, old_password, new_password))
        if self.change_error:
            raise self.change_error

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


def test_do_forgot_password_requests_and_confirms(monkeypatch, app):
    provider = DummyProvider()
    app.provider = provider
    responses = iter(["123456", "Newpass1", "Newpass1"])
    monkeypatch.setattr("ui.gui.simpledialog.askstring", lambda *args, **kwargs: next(responses))
    monkeypatch.setattr("ui.gui.messagebox.showinfo", lambda *args, **kwargs: None)
    monkeypatch.setattr("ui.gui.messagebox.showerror", lambda *args, **kwargs: None)

    frame = SimpleNamespace(
        email_entry=DummyEntry("student@csu.fullerton.edu"),
        warning_label=DummyLabel(),
    )
    app.do_forgot_password(frame)

    assert provider.reset_calls == ["student@csu.fullerton.edu"]
    assert provider.confirm_calls == [("student@csu.fullerton.edu", "123456", "Newpass1")]


def test_do_change_password_uses_access_token(monkeypatch, app):
    provider = DummyProvider()
    app.provider = provider
    app.auth_tokens = {"tokens": {"AccessToken": "token"}}
    app.is_logged_in = True
    responses = iter(["Oldpass1", "Newpass1", "Newpass1"])
    monkeypatch.setattr("ui.gui.simpledialog.askstring", lambda *args, **kwargs: next(responses))
    monkeypatch.setattr("ui.gui.messagebox.showinfo", lambda *args, **kwargs: None)
    monkeypatch.setattr("ui.gui.messagebox.showerror", lambda *args, **kwargs: None)

    app.do_change_password()

    assert provider.change_calls == [("token", "Oldpass1", "Newpass1")]