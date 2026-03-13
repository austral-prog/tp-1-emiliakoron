def grades():
    """
    Ejercicio 11 - Promedio de Calificaciones

    Dadas tres notas, calcular e imprimir:
    1. El promedio de las tres notas
    2. La nota máxima
    3. La nota mínima
    4. Cuántos puntos faltan del promedio a 10
    """
    nota1 = 8
    nota2 = 7
    nota3 = 9
    promedio = (nota1 + nota2 + nota3) / 3
    nota_max = max(nota1, nota2, nota3)
    nota_min = min(nota1, nota2, nota3)
    puntos_faltan = 10 - promedio

    print("El promedio de las tres notas: ", promedio)
    print("La nota máxima es: ", nota_max)
    print("La nota mínima es = ", nota_min)
    print("Los puntos faltantes del promedio a 10 son: ", puntos_faltan)
