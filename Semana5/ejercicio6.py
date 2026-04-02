"""
Ejercicio 6:
Una tienda registra sus ventas diarias en una lista de números. Cada número representa el monto de ventas de un día.
Se solicita calcular el total de ventas acumuladas.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""

def total_ventas_ciclo(ventas):
    """
    Retorna el total de ventas usando ciclos.
    """
    total = 0
    for i in range(len(ventas)):
        total += ventas
    return total

print(total_ventas_ciclo([1,2,3,4,5]))

def total_ventas_recursivo(ventas):
    """
    Retorna el total de ventas usando recursividad.
    """
    # Escriba aquí su solución
    if ventas == []:  
        return 0
    return ventas[0] + total_ventas_recursivo(ventas[1:])
