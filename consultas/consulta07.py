import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

try:
    df = pd.read_csv("datos.csv")
except Exception:
    df = pd.DataFrame()

def buildC7(frame):
    izq = ctk.CTkFrame(frame, fg_color="transparent")
    izq.pack(side="left", fill="both", expand=True, padx=20, pady=20)
    der = ctk.CTkFrame(frame, fg_color="#1a1d27", corner_radius=8)
    der.pack(side="right", fill="both", expand=True, padx=20, pady=20)

    ctk.CTkLabel(izq, text="Distribución de Baños", font=("Arial", 20, "bold"), text_color="white").pack(anchor="w", pady=(0, 20))
    ctk.CTkLabel(izq, text="Cantidad de propiedades agrupadas por baños.", text_color="#7b7f96").pack(anchor="w", pady=(0, 15))
    lbl_mensaje = ctk.CTkLabel(izq, text="", text_color="#10b981")
    lbl_mensaje.pack(anchor="w", pady=(0, 15))

    def ejecutar():
        if df.empty: return
        for widget in der.winfo_children():
            widget.destroy()

        conteo_banos = df["baths"].value_counts().sort_index()
        fig, ax = plt.subplots(figsize=(6, 5), facecolor='#1a1d27')
        ax.set_facecolor('#1a1d27')
        conteo_banos.plot(kind="bar", color="#4f8ef7", ax=ax)
        
        ax.set_title("Propiedades según cantidad de baños", color="white")
        ax.set_xlabel("Número de baños", color="white")
        ax.set_ylabel("Cantidad", color="white")
        ax.tick_params(colors="white")
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=der)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        lbl_mensaje.configure(text="Gráfica generada", text_color="#10b981")

    ctk.CTkButton(izq, text="Generar Gráfica", fg_color="#4f8ef7", command=ejecutar).pack(fill="x", pady=10)