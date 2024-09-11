def factorial(n):
    if n == 0 or n == 1:  # El factorial de 0 y 1 es 1
        return 1
    else:
        return n * factorial(n - 1)  # Llamada recursiva

# Ejemplo de uso
print(factorial(5))  # Salida: 120
