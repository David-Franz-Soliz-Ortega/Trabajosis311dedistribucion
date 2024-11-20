import tkinter as tk

class UtilidadesMenu:
    def __init__(self, root, menu_bar):
        utilidades_menu = tk.Menu(menu_bar, tearoff=0)
        utilidades_menu.add_command(label="Calculadora", command=self.calculadora)
        menu_bar.add_cascade(label="Utilidades", menu=utilidades_menu)

    def calculadora(self):
        calc_window = tk.Toplevel()
        calc_window.title("Calculadora")

        display = tk.Entry(calc_window, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
        display.grid(row=0, column=0, columnspan=4)

        def agregar_numero(num):
            display.insert(tk.END, num)

        def calcular():
            try:
                resultado = eval(display.get())
                display.delete(0, tk.END)
                display.insert(tk.END, str(resultado))
            except Exception:
                display.delete(0, tk.END)
                display.insert(tk.END, "Error")

        botones = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', 'C', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for boton in botones:
            action = lambda x=boton: agregar_numero(x) if x not in ('=', 'C') else calcular() if x == '=' else display.delete(0, tk.END)
            tk.Button(calc_window, text=boton, width=5, height=2, command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
