#grupo Diego Roberto Arancibia Delgado, Efrain Salazar Santos
import tkinter as tk
from distribuciones.poisson import Poisson

def abrir_interfaz_poisson():
    poisson_window = tk.Toplevel()
    poisson_window.title("Distribución Poisson")

    # Entrada para lambda
    tk.Label(poisson_window, text="Tasa media de ocurrencia (λ):").grid(row=0, column=0, padx=5, pady=5)
    lambda_entry = tk.Entry(poisson_window)
    lambda_entry.grid(row=0, column=1, padx=5, pady=5)

    # para mostrar los resultados
    resultado_label = tk.Label(poisson_window, text="")
    resultado_label.grid(row=2, column=0, columnspan=2, pady=10)

    def calcular_poisson():
        try:
            # Leer y convertir el parámetro lambda
            lambda_param = float(lambda_entry.get())
            distribucion = Poisson(lambda_param)

            # Calculo de la media y varianza
            media = distribucion.media()
            varianza = distribucion.varianza()

            # resultados
            resultado_label.config(text=f"Media: {media:.2f}, Varianza: {varianza:.2f}")
        except ValueError:
            resultado_label.config(text="Error: Valor no válido para λ")

    # Btn calcular
    tk.Button(poisson_window, text="Calcular", command=calcular_poisson).grid(row=1, column=1, pady=10)
