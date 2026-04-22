import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

try:
    df = pd.read_csv("datos.csv")
except Exception:
    df = pd.DataFrame()

def buildC2(frame):
    izq = ctk.CTkFrame(frame, fg_color="transparent")
    izq.pack(side="left", fill="both", expand=True, padx=20, pady=20)
    der = ctk.CTkFrame(frame, fg_color="#1a1d27", corner_radius=8)
    der.pack(side="right", fill="both", expand=True, padx=20, pady=20)

    ctk.CTkLabel(izq, text="Tamaño vs Precio", font=("Arial", 20, "bold"), text_color="white").pack(anchor="w", pady=(0, 20))
    ctk.CTkLabel(izq, text="Analiza la correlación entre pies cuadrados y precio.", text_color="#7b7f96").pack(anchor="w", pady=(0, 15))
    lbl_mensaje = ctk.CTkLabel(izq, text="", text_color="#10b981")
    lbl_mensaje.pack(anchor="w", pady=(0, 15))

    def ejecutar():
        if df.empty: return
        for widget in der.winfo_children():
            widget.destroy()

        datos = df.query("sq__ft > 0")
        fig, ax = plt.subplots(figsize=(6, 5), facecolor='#1a1d27')
        ax.set_facecolor('#1a1d27')
        ax.scatter(datos["sq__ft"], datos["price"], color="#10b981", alpha=0.5)
        
        ax.set_title("Relación: Pies Cuadrados vs Precio", color="white")
        ax.set_xlabel("Pies Cuadrados", color="white")
        ax.set_ylabel("Precio ($)", color="white")
        ax.tick_params(colors="white")
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=der)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        lbl_mensaje.configure(text="Gráfica generada con éxito", text_color="#10b981")

    ctk.CTkButton(izq, text="Generar Gráfica", fg_color="#4f8ef7", command=ejecutar).pack(fill="x", pady=10)