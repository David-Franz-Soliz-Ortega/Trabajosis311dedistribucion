import tkinter as tk
from distribuciones.uniforme import Uniforme

def abrir_interfaz_uniforme():
    uniforme_window = tk.Toplevel()
    uniforme_window.title("Distribución Uniforme")

    tk.Label(uniforme_window, text="Límite inferior (a):").grid(row=0, column=0, padx=5, pady=5)
    limite_inferior = tk.Entry(uniforme_window)
    limite_inferior.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(uniforme_window, text="Límite superior (b):").grid(row=1, column=0, padx=5, pady=5)
    limite_superior = tk.Entry(uniforme_window)
    limite_superior.grid(row=1, column=1, padx=5, pady=5)

    resultado_label = tk.Label(uniforme_window, text="")
    resultado_label.grid(row=3, column=0, columnspan=2, pady=10)

    def calcular_uniforme():
        try:
            a = float(limite_inferior.get())
            b = float(limite_superior.get())
            distribucion = Uniforme(a, b)
            
            media = distribucion.media()
            varianza = distribucion.varianza()
            
            resultado_label.config(text=f"Media: {media:.2f}, Varianza: {varianza:.2f}")
        except ValueError:
            resultado_label.config(text="Error: Valores no válidos")

    tk.Button(uniforme_window, text="Calcular", command=calcular_uniforme).grid(row=2, column=1, pady=10)
