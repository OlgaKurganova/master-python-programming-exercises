# Complete the function to return the tens digit and the units digit of any interger
def two_digits(number):
  # Your code here
  # Obtener el dígito de las decenas dividiendo por 10 y obteniendo la parte entera
    des_digit = number // 10
    unidades_left=number % 10
    print(des_digit)
    return des_digit, unidades_left
   

# Invoke the function with any two digit integer as its argument
print(two_digits(79))
