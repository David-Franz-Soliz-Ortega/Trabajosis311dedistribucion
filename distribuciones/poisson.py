import math
import random

class Poisson:
    def __init__(self, lambda_param):
        if lambda_param <= 0:
            raise ValueError("La tasa de ocurrencia (λ) debe ser mayor que cero.")
        self.lambda_param = lambda_param

    def media(self):
        """Calculo de la media de la distribución de Poisson."""
        return self.lambda_param

    def varianza(self):
        """Calculo de la varianza de la distribución de Poisson."""
        return self.lambda_param

    def densidad(self, k):
        """Calculo de la función de densidad de probabilidad en el punto k."""
        return (self.lambda_param ** k * math.exp(-self.lambda_param)) / math.factorial(k)

    def distribucion_acumulada(self, k):
        """Calculo de la función de distribución acumulada hasta el punto k."""
        acumulado = sum(self.densidad(i) for i in range(k + 1))
        return acumulado

    def generar_valor(self):
        """Genera un valor aleatorio con distribución de Poisson."""
        L = math.exp(-self.lambda_param)
        k = 0
        p = 1
        while p > L:
            k += 1
            p *= random.uniform(0, 1)
        return k - 1

    def __str__(self):
        return f"Distribución Poisson(λ={self.lambda_param})"
