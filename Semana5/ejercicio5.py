"""
Ejercicio 5:
Calcular la potencia de una base elevada a un exponente entero positivo.
"""

def potencia_ciclo(base, exponente):
    pot = 1
    for i in range(exponente):
        pot += base
    return pot

print(potencia_ciclo(5,3))

def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 0
    elif exponente == 1:
        return base
    else:
        return potencia_recursiva(base, exponente - 1) * base 

print(potencia_recursiva(5,3))