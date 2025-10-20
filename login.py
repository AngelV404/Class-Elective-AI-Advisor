import os
from pathlib import Path
from dotenv import load_dotenv
import customtkinter as ctk

# Load environment variables (.env file next to this file)
load_dotenv(dotenv_path=Path(__file__).with_name(".env"))

# Import your new frames and controller
from controller_app import AppController
from ui.LoginFrame import LoginFrame
from ui.registerFrame import RegisterFrame

# Start CustomTkinter
if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.geometry("900x650")
    root.title("Smart Elective Advisor — Cognito Login")

    # Launch the controller which manages both frames
    AppController(root, login_frame_cls=LoginFrame, register_frame_cls=RegisterFrame)

    root.mainloop()