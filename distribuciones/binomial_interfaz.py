import tkinter as tk
from distribuciones.binomial import Binomial

def abrir_interfaz_binomial():
    binomial_window = tk.Toplevel()
    binomial_window.title("Distribución Binomial")

    tk.Label(binomial_window, text="Número de pruebas (n):").grid(row=0, column=0, padx=5, pady=5)
    n_entry = tk.Entry(binomial_window)
    n_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(binomial_window, text="Probabilidad de éxito (p):").grid(row=1, column=0, padx=5, pady=5)
    p_entry = tk.Entry(binomial_window)
    p_entry.grid(row=1, column=1, padx=5, pady=5)

    resultado_label = tk.Label(binomial_window, text="")
    resultado_label.grid(row=3, column=0, columnspan=2, pady=10)

    def calcular_binomial():
        try:
            n = int(n_entry.get())
            p = float(p_entry.get())
            distribucion = Binomial(n, p)
            
            media = distribucion.media()
            varianza = distribucion.varianza()
            
            resultado_label.config(text=f"Media: {media:.2f}, Varianza: {varianza:.2f}")
        except ValueError:
            resultado_label.config(text="Error: Valores no válidos")

    tk.Button(binomial_window, text="Calcular", command=calcular_binomial).grid(row=2, column=1, pady=10)
