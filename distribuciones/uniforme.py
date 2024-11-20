import random

class Uniforme:
    def __init__(self, a, b):
        if a >= b:
            raise ValueError("El límite inferior 'a' debe ser menor que el límite superior 'b'.")
        self.a = a
        self.b = b

    def media(self):
        """Calcula la media de la distribución uniforme."""
        return (self.a + self.b) / 2

    def varianza(self):
        """Calcula la varianza de la distribución uniforme."""
        return ((self.b - self.a) ** 2) / 12

    def densidad(self, x):
        """Calcula la función de densidad en el punto x."""
        if self.a <= x <= self.b:
            return 1 / (self.b - self.a)
        else:
            return 0

    def distribucion_acumulada(self, x):
        """Calcula la función de distribución acumulada en el punto x."""
        if x < self.a:
            return 0
        elif x > self.b:
            return 1
        else:
            return (x - self.a) / (self.b - self.a)

    def generar_valor(self):
        """Genera un valor aleatorio con distribución uniforme entre a y b."""
        return random.uniform(self.a, self.b)

    def __str__(self):
        return f"Distribución Uniforme(a={self.a}, b={self.b})"
