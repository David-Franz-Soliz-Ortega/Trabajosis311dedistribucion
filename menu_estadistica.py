import tkinter as tk
from distribuciones.uniforme_interfaz import abrir_interfaz_uniforme
#from distribuciones.normal_interfaz import abrir_interfaz_normal
#from distribuciones.exponencial_interfaz import abrir_interfaz_exponencial
#from distribuciones.gamma_interfaz import abrir_interfaz_gamma
from distribuciones.binomial_interfaz import abrir_interfaz_binomial
#from distribuciones.poisson_interfaz import abrir_interfaz_poisson
#from distribuciones.geometrica_interfaz import abrir_interfaz_geometrica
#from distribuciones.bernoulli_interfaz import abrir_interfaz_bernoulli

class EstadisticaMenu:
    def __init__(self, root, menu_bar):
        estadistica_menu = tk.Menu(menu_bar, tearoff=0)
        
        # Distribuciones Discretas
        estadistica_menu.add_command(label="Distribución Binomial", command=abrir_interfaz_binomial)
        
        # Separador entre discretas y continuas
        estadistica_menu.add_separator()

        # Distribuciones Continuas
        estadistica_menu.add_command(label="Distribución Chi-Cuadrado", command=abrir_interfaz_chicuadrado)
        estadistica_menu.add_command(label="Distribución Uniforme", command=abrir_interfaz_uniforme)
        
        menu_bar.add_cascade(label="Estadística", menu=estadistica_menu)