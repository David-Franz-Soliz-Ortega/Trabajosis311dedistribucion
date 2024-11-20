import tkinter as tk
from datetime import datetime

class EntradaMenu:
    def __init__(self, root, menu_bar):
        entrada_menu = tk.Menu(menu_bar, tearoff=0)
        entrada_menu.add_command(label="Edad", command=self.entrada_edad)
        menu_bar.add_cascade(label="Entrada", menu=entrada_menu)

    def entrada_edad(self):
        edad_window = tk.Toplevel()
        edad_window.title("Calcular Edad")

        tk.Label(edad_window, text="Nombre:").grid(row=0, column=0)
        nombre_entry = tk.Entry(edad_window)
        nombre_entry.grid(row=0, column=1)

        tk.Label(edad_window, text="Fecha de Nacimiento (dd/mm/yyyy):").grid(row=1, column=0)
        fecha_entry = tk.Entry(edad_window)
        fecha_entry.grid(row=1, column=1)

        def calcular_edad():
            try:
                fecha_nac = datetime.strptime(fecha_entry.get(), "%d/%m/%Y")
                edad = datetime.now().year - fecha_nac.year
                tk.Label(edad_window, text=f"Tienes {edad} años").grid(row=3, columnspan=2)
            except ValueError:
                tk.Label(edad_window, text="Formato de fecha inválido").grid(row=3, columnspan=2)

        tk.Button(edad_window, text="Calcular", command=calcular_edad).grid(row=2, column=1)
