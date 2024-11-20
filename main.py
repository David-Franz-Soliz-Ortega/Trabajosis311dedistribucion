import tkinter as tk
from menu_archivo import ArchivoMenu
from menu_edicion import EdicionMenu
from menu_entrada import EntradaMenu
from menu_estadistica import EstadisticaMenu
#from menu_ajuste import AjusteMenu
from menu_utilidades import UtilidadesMenu
#from menu_vista import VistaMenu
#from menu_ventana import VentanaMenu
#from menu_ayuda import AyudaMenu

class AjusteStatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AjusteStat")
        self.root.geometry("800x600")

        # Crear barra de menú
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # Instanciar los menús
        ArchivoMenu(self.root, menu_bar)
        EdicionMenu(self.root, menu_bar)
        EntradaMenu(self.root, menu_bar)
        EstadisticaMenu(self.root, menu_bar)
#        AjusteMenu(self.root, menu_bar)
        UtilidadesMenu(self.root, menu_bar)
#        VistaMenu(self.root, menu_bar)
#        VentanaMenu(self.root, menu_bar)
#        AyudaMenu(self.root, menu_bar)

if __name__ == "__main__":
    root = tk.Tk()
    app = AjusteStatApp(root)
    root.mainloop()
