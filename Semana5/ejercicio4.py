"""
Ejercicio 4:
Dado un número entero positivo N, contar cuántos números pares existen entre 1 y N.
"""

def contar_pares_ciclo(n):
    suma = 0
    for i in range(1, n+1):
        if n % 2 == 0:
            suma += suma + 1
    return suma
    
print(contar_pares_ciclo(24))


def contar_pares_recursivo(n):
    if n <= 0:
        return 0
    if n % 2 == 0:
        return contar_pares_recursivo(n - 2)
    else:
        return contar_pares_recursivo(n - 1)

print(contar_pares_recursivo(24))