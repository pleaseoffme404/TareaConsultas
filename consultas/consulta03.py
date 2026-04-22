import customtkinter as ctk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

try:
    df = pd.read_csv("datos.csv")
except Exception:
    df = pd.DataFrame()

def buildC3(frame):
    izq = ctk.CTkFrame(frame, fg_color="transparent")
    izq.pack(side="left", fill="both", expand=True, padx=20, pady=20)
    der = ctk.CTkFrame(frame, fg_color="#1a1d27", corner_radius=8)
    der.pack(side="right", fill="both", expand=True, padx=20, pady=20)

    ctk.CTkLabel(izq, text="Distribución de Precios", font=("Arial", 20, "bold"), text_color="white").pack(anchor="w", pady=(0, 20))
    ctk.CTkLabel(izq, text="Histograma de frecuencias de los precios de venta.", text_color="#7b7f96").pack(anchor="w", pady=(0, 15))
    lbl_mensaje = ctk.CTkLabel(izq, text="", text_color="#10b981")
    lbl_mensaje.pack(anchor="w", pady=(0, 15))

    def ejecutar():
        if df.empty: return
        for widget in der.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(6, 5), facecolor='#1a1d27')
        ax.set_facecolor('#1a1d27')
        df['price'].plot(kind='hist', bins=30, color="#8b5cf6", edgecolor="black", ax=ax)
        
        ax.set_title("Frecuencia de Precios en el Mercado", color="white")
        ax.set_xlabel("Precio ($)", color="white")
        ax.set_ylabel("Frecuencia", color="white")
        ax.tick_params(colors="white")
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=der)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        lbl_mensaje.configure(text="Histograma generado", text_color="#10b981")

    ctk.CTkButton(izq, text="Generar Gráfica", fg_color="#4f8ef7", command=ejecutar).pack(fill="x", pady=10)