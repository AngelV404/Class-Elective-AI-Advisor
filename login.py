from pathlib import Path
from dotenv import load_dotenv
import customtkinter as ctk
from ui.gui import App

# Load environment variables (.env file next to this file)
load_dotenv(dotenv_path=Path(__file__).with_name(".env"))

if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    app = App()
    app.mainloop()