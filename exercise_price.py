def price():
    """
    Ejercicio 8 - Cálculo de Precio Final

    Dado un precio base, calcular e imprimir:
    1. El monto del impuesto (21%)
    2. El subtotal (precio base + impuesto)
    3. El monto de la propina (10% del subtotal)
    4. El precio final (subtotal + propina)
    """
    precio_base = 100
    monto_impuesto = 21
    monto_subtotal = precio_base + monto_impuesto
    monto_propina = monto_subtotal / 10
    precio_final = monto_subtotal + monto_propina

    print(monto_impuesto)
    print(monto_subtotal)
    print(monto_propina)
    print (precio_final)
