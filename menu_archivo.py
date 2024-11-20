import tkinter as tk
from tkinter import messagebox, filedialog

class ArchivoMenu:
    def __init__(self, root, menu_bar):
        archivo_menu = tk.Menu(menu_bar, tearoff=0)
        archivo_menu.add_command(label="Abrir", command=self.abrir_archivo)
        archivo_menu.add_command(label="Cerrar", command=self.cerrar_archivo)
        archivo_menu.add_command(label="Guardar", command=self.guardar_archivo)
        archivo_menu.add_command(label="Exportar", command=self.exportar_archivo)
        archivo_menu.add_command(label="Imprimir", command=self.imprimir_archivo)
        archivo_menu.add_command(label="Configurar", command=self.configurar_archivo)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=root.quit)
        menu_bar.add_cascade(label="Archivo", menu=archivo_menu)

    def abrir_archivo(self):
        filedialog.askopenfilename()

    def cerrar_archivo(self):
        messagebox.showinfo("Cerrar", "Cerrando archivo...")

    def guardar_archivo(self):
        filedialog.asksaveasfilename()

    def exportar_archivo(self):
        messagebox.showinfo("Exportar", "Exportando archivo...")

    def imprimir_archivo(self):
        messagebox.showinfo("Imprimir", "Imprimiendo archivo...")

    def configurar_archivo(self):
        messagebox.showinfo("Configurar", "Configurando archivo...")
