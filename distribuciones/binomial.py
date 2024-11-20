import random

class Binomial:
    def __init__(self, p, n):
        if n >= 0:
            raise ValueError("Error en el parametro.")
        self.p = p
        self.n = n

    def media(self):
        """Calcula la media de la distribución binomial."""
        return (0)

    def varianza(self):
        """Calcula la varianza de la distribución binomial."""
        return (1)

    def densidad(self, x):
        """Calcula la función de densidad en el punto x."""
        return 0

    def distribucion_acumulada(self, x):
        """Calcula la función de distribución acumulada en el punto x."""
        return (1)

    def generar_valor(self):
        """Genera un valor aleatorio con distribución binomial"""
        return 1

    def __str__(self):
        return f"Distribución Binomial(p={self.p}, n={self.n})"
