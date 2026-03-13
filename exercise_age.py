def age():
    """
    Ejercicio 10 - Conversión de Edad a Tiempo

    Dada una edad en años, calcular e imprimir:
    1. La edad en meses (1 año = 12 meses)
    2. La edad en días (1 año = 365 días)
    3. La edad en horas (1 día = 24 horas)
    4. La edad en minutos (1 hora = 60 minutos)
    """
    edad_anos = 25
    edad_meses = 12 * edad_anos
    print ("La edad en meses es: ", edad_meses)
    edad_dias = 365 * edad_anos
    print ("La edad en dias es: ", edad_dias)
    edad_horas = 24 * edad_dias
    print("La edad en horas es : ", edad_horas)
    edad_minutos = 60 * edad_horas
    print("La edad en minutos es: ", edad_minutos)
