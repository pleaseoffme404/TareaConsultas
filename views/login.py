import json
import customtkinter as ctk
from pathlib import Path

accentColor = "#4f8ef7"
accentHover = "#6aa3ff"
bgColor = "#0f1117"
panelColor = "#1a1d27"
borderColor = "#2a2d3e"
entryBgColor = "#12141e"
textColor = "#e8eaf0"
subtextColor = "#7b7f96"
errorColor = "#f75f5f"

usersFilePath = Path(__file__).parent.parent / "users.json"

def validateUser(username, password):
    if not usersFilePath.exists(): return None
    with open(usersFilePath, "r", encoding="utf-8") as f:
        data = json.load(f)
    for user in data.get("users", []):
        if user["username"] == username and user["password"] == password:
            return user
    return None

def showLogin():
    loginWindow = ctk.CTk()
    loginWindow.title("Consultas IA - Login")
    loginWindow.geometry("440x520")
    loginWindow.resizable(False, False)
    loginWindow.configure(fg_color=bgColor)

    panel = ctk.CTkFrame(loginWindow, fg_color=panelColor, corner_radius=16, border_width=1, border_color=borderColor)
    panel.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.85, relheight=0.90)

    ctk.CTkLabel(panel, text="Sistema de Consultas", font=ctk.CTkFont(size=23, weight="bold"), text_color=textColor).place(relx=0.5, rely=0.25, anchor="center")

    entryUser = ctk.CTkEntry(panel, placeholder_text="Usuario", height=42, corner_radius=10, fg_color=entryBgColor, text_color=textColor)
    entryUser.place(relx=0.1, rely=0.45, relwidth=0.80)

    entryPass = ctk.CTkEntry(panel, placeholder_text="Contraseña", show="●", height=42, corner_radius=10, fg_color=entryBgColor, text_color=textColor)
    entryPass.place(relx=0.1, rely=0.60, relwidth=0.80)

    lblError = ctk.CTkLabel(panel, text="", font=ctk.CTkFont(size=12), text_color=errorColor)
    lblError.place(relx=0.5, rely=0.75, anchor="center")

    def onLogin():
        u, p = entryUser.get(), entryPass.get()
        userData = validateUser(u, p)
        if userData:
            loginWindow.destroy()
            from views.hub import showHub
            showHub(userData)
        else:
            lblError.configure(text="Credenciales incorrectas")

    ctk.CTkButton(panel, text="Entrar", height=44, corner_radius=10, fg_color=accentColor, command=onLogin).place(relx=0.1, rely=0.85, relwidth=0.80)
    loginWindow.mainloop()