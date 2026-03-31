"""
Ejercicio 3:
Dado un número entero positivo N, calcular su factorial.

Debe implementar una versión iterativa y una recursiva.
"""

def factorial_ciclo(n):
    fact = 1
    for i in range(2, n + 1):
        resiltado *= i
    return fact
print(factorial_ciclo(4))

def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return factorial_recursivo(n - 1) * 1
