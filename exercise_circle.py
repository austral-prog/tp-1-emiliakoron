from math import pi


def circle():
    """
    Ejercicio 6 - Geometría de Círculo

    Dado el radio de un círculo, calcular e imprimir:
    1. El área (π × radio²)
    2. La circunferencia (2 × π × radio)
    """
    radio = 5
    area_circulo = pi * radio ** 2
    print("El area del circulo es: ", area_circulo)
    circunferencia_circulo = 2 * pi * radio
    print("La circunferencia es de: ", circunferencia_circulo)
