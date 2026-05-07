import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def buildC11(frame):
    izq = ctk.CTkFrame(frame, fg_color="transparent")
    izq.pack(side="left", fill="both", expand=True, padx=20, pady=20)
    der = ctk.CTkFrame(frame, fg_color="#1a1d27", corner_radius=8)
    der.pack(side="right", fill="both", expand=True, padx=20, pady=20)

    ctk.CTkLabel(izq, text="Graficador f(x) = mx + b", font=("Arial", 20, "bold"), text_color="white").pack(anchor="w", pady=(0, 20))
    ctk.CTkLabel(izq, text="Genera funciones lineales con NumPy.", text_color="#7b7f96").pack(anchor="w", pady=(0, 15))

    ctk.CTkLabel(izq, text="Pendiente (m):", font=("Arial", 12, "bold"), text_color="#7b7f96").pack(anchor="w")
    entrada_m = ctk.CTkEntry(izq, height=40, corner_radius=8, fg_color="#12141e", text_color="white")
    entrada_m.pack(fill="x", pady=(5, 10))

    ctk.CTkLabel(izq, text="Intersección en Y (b):", font=("Arial", 12, "bold"), text_color="#7b7f96").pack(anchor="w")
    entrada_b = ctk.CTkEntry(izq, height=40, corner_radius=8, fg_color="#12141e", text_color="white")
    entrada_b.pack(fill="x", pady=(5, 15))

    lbl_mensaje = ctk.CTkLabel(izq, text="", text_color="#10b981")
    lbl_mensaje.pack(anchor="w", pady=(0, 15))

    def ejecutar():
        for widget in der.winfo_children():
            widget.destroy()

        try:
            m = float(entrada_m.get().strip())
            b = float(entrada_b.get().strip())
        except ValueError:
            lbl_mensaje.configure(text="Error: Ingrese valores numéricos válidos", text_color="#f75f5f")
            return

        x = np.linspace(-10, 10, 100)
        y = m * x + b

        fig, ax = plt.subplots(figsize=(6, 5), facecolor='#1a1d27')
        ax.set_facecolor('#1a1d27')
        
        ax.plot(x, y, color="#4f8ef7", linestyle="--", label=f"f(x) = {m}x + {b}")
        
        ax.set_title("Función Lineal", color="white")
        ax.set_xlabel("Eje X", color="white")
        ax.set_ylabel("Eje Y", color="white")
        ax.tick_params(colors="white")
        
        ax.axhline(0, color='white', linewidth=1)
        ax.axvline(0, color='white', linewidth=1)
        ax.grid(True, color='#2a2d3e', linestyle=':')
        
        leyenda = ax.legend(loc=1)
        leyenda.get_frame().set_facecolor('#1a1d27')
        leyenda.get_frame().set_edgecolor('#2a2d3e')
        for texto in leyenda.get_texts():
            texto.set_color("white")
            
        fig.tight_layout()

        canvas = FigureCanvasTkAgg(fig, master=der)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)
        lbl_mensaje.configure(text="Gráfica generada con éxito", text_color="#10b981")

    ctk.CTkButton(izq, text="Graficar", fg_color="#4f8ef7", command=ejecutar).pack(fill="x", pady=10)