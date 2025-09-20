import tkinter as tk

class LoginFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        tk.Label(self, text="Login Page").pack(pady=20)
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()
        self.pass_entry = tk.Entry(self, show="*")
        self.pass_entry.pack()
        tk.Button(self, text="Submit").pack()