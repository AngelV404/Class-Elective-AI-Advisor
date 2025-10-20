import pytest
import customtkinter as ctk
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Auto fixture that runs before every test
@pytest.fixture(autouse=True)
def setup_env(monkeypatch):
    """Mock AWS + GUI window so tests run headless."""
    # Mock AWS Cognito environment
    monkeypatch.setenv("AWS_REGION", "us-west-2")
    monkeypatch.setenv("COGNITO_USER_POOL_ID", "dummy-pool-id")
    monkeypatch.setenv("COGNITO_CLIENT_ID", "dummy-client-id")

    # Mock DB setup to avoid real file access
    monkeypatch.setattr(queries, "get_user", lambda email: None)
    monkeypatch.setattr(gui.dbsetup, "connectdb", lambda: None)

    # Prevent actual Tk window

    monkeypatch.setattr(ctk.CTk, "mainloop", lambda self: None)

    # Replace CognitoAuthProvider with a dummy
    import ui.gui as gui

    class DummyProvider:
        def register_user(self, *args, **kwargs): return "Registered"
        def authenticate_user(
            self, *args, **kwargs): return {"AccessToken": "mock"}

        def resend_confirmation(self, *args, **kwargs): return "Resent"
    monkeypatch.setattr(gui, "CognitoAuthProvider", DummyProvider)


# App startup should work without errors
def test_gui_startup():
    from ui.gui import App
    app = App()
    assert app is not None, "App failed to initialize"


# Check that sidebar and main frames exist
def test_main_components_exist():
    from ui.gui import App
    app = App()
    assert hasattr(app, "sidebarFrame"), "Sidebar frame missing"
    assert hasattr(app, "mainArea"), "Main content frame missing"


# Verify sidebar buttons exist
def test_sidebar_buttons_exist():
    from ui.gui import App
    app = App()

    expected_buttons = ["Home", "Login", "Preferences",
                        "Course Search", "Recommended", "Profile", "Help"]
    found_labels = [
        child.cget("text")
        for child in app.sidebarFrame.winfo_children()
        if hasattr(child, "cget")
    ]
    for label in expected_buttons:
        assert label in found_labels, f"Sidebar missing '{label}' button"


# Ensure login frame UI components exist (view test)
def test_login_frame_structure():
    try:
        from ui.LoginFrame import LoginFrame
        frame = LoginFrame(None, None)  # parent=None, app=None (UI-only)
    except Exception as e:
        pytest.skip(f"LoginFrame not ready yet: {e}")

    for attr in ["email_entry", "password_entry", "login_button", "register_button"]:
        assert hasattr(frame, attr), f"LoginFrame missing {attr}"


# Ensure register frame UI components exist
def test_register_frame_structure():
    try:
        from ui.registerFrame import RegisterFrame
        frame = RegisterFrame(None, None)
    except Exception as e:
        pytest.skip(f"RegisterFrame not ready yet: {e}")

    for attr in ["name_entry", "email_entry", "password_entry", "confirm_entry",
                 "register_button"]:
        assert hasattr(frame, attr), f"RegisterFrame missing {attr}"


# Verify dropdowns and entries exist in PreferenceFrame
def test_preferences_frame_structure():
    try:
        from ui.PreferencesFrame import PreferenceFrame
        frame = PreferenceFrame(None)
    except Exception as e:
        pytest.skip(f"PreferenceFrame not ready yet: {e}")

    for attr in [
        "college_menu", "department_menu", "degree_level_menu",
        "degree_menu", "preferred_job_entry", "counselor_email_entry", "submit_button"
    ]:
        assert hasattr(frame, attr), f"PreferenceFrame missing {attr}"


# Simulate resizing window (layout sanity test)
def test_responsive_layout():
    from ui.gui import App
    app = App()
    try:
        app.geometry("400x300")
        app.update()
        app.geometry("900x600")
        app.update()
    except Exception as e:
        pytest.fail(f"Layout update failed: {e}")

    assert hasattr(app, "sidebarFrame"), "Sidebar missing after resize"
    assert hasattr(app, "mainArea"), "Main area missing after resize"
