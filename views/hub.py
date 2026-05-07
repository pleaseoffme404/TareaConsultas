import customtkinter as ctk
from consultas.consulta01 import buildC1
from consultas.consulta02 import buildC2
from consultas.consulta03 import buildC3
from consultas.consulta04 import buildC4
from consultas.consulta05 import buildC5
from consultas.consulta06 import buildC6
from consultas.consulta07 import buildC7
from consultas.consulta08 import buildC8
from consultas.consulta09 import buildC9
from consultas.consulta10 import buildC10
from consultas.consulta11 import buildC11

bgColor = "#0f1117"
topbarColor = "#1a1d27"
accentColor = "#7c3aed"
textColor = "#e8eaf0"

tabLabels = ["Consulta 1", "Consulta 2", "Consulta 3", "Consulta 4", "Consulta 5", "Consulta 6", "Consulta 7", "Consulta 8", "Consulta 9", "Consulta 10", "Actividad 11"]
tabBuilders = [buildC1, buildC2, buildC3, buildC4, buildC5, buildC6, buildC7, buildC8, buildC9, buildC10, buildC11]

def showHub(userData):
    hubWindow = ctk.CTk()
    hubWindow.title("Panel de Consultas CSV")
    hubWindow.geometry("1100x680")
    hubWindow.configure(fg_color=bgColor)

    topbar = ctk.CTkFrame(hubWindow, height=56, fg_color=topbarColor, corner_radius=0)
    topbar.pack(side="top", fill="x")

    ctk.CTkLabel(topbar, text=f"Bienvenido: {userData['name']}", text_color=textColor).place(x=20, rely=0.5, anchor="w")

    tabView = ctk.CTkTabview(hubWindow, segmented_button_selected_color=accentColor)
    tabView.pack(fill="both", expand=True, padx=16, pady=16)

    for i, label in enumerate(tabLabels):
        tabView.add(label)
        tabBuilders[i](tabView.tab(label))

    hubWindow.mainloop()