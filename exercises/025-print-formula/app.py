# Your code here
import math

def print_formula(d):
    # Valores fijos
    c = 50
    h = 30
    # Cálculo de Q
    Q = math.sqrt((2 * c * d) / h)
    # Imprimir el valor de Q
    print(f"El valor de Q es: {Q}")

# Ejemplo de uso
print_formula(100)  # Puedes probar con cualquier valor de d
