import tkinter as tk
from scipy.stats import chi2

def abrir_interfaz_chicuadrado():
    chicuadrado_window = tk.Toplevel()
    chicuadrado_window.title("Distribución Chi-Cuadrado")

    tk.Label(chicuadrado_window, text="Grados de libertad:").grid(row=0, column=0)
    grados_libertad_entry = tk.Entry(chicuadrado_window)
    grados_libertad_entry.grid(row=0, column=1)

    tk.Label(chicuadrado_window, text="Nivel de significancia (alfa):").grid(row=1, column=0)
    alfa_entry = tk.Entry(chicuadrado_window)
    alfa_entry.grid(row=1, column=1)

    resultado_label = tk.Label(chicuadrado_window, text="")
    resultado_label.grid(row=3, columnspan=2)

    def calcular_chi_cuadrado():
        try:
            df = int(grados_libertad_entry.get())
            alfa = float(alfa_entry.get())
            chi_critico = chi2.ppf(1 - alfa, df)
            resultado_label.config(text=f"Valor crítico chi-cuadrado: {chi_critico:.4f}")
        except ValueError:
            resultado_label.config(text="Entrada no válida")

    tk.Button(chicuadrado_window, text="Calcular", command=calcular_chi_cuadrado).grid(row=2, column=1)