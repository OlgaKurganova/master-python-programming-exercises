# Complete the function to return the swapped digits of a given two-digit integer
def swap_digits(num):
  # Your code here
   # Obtener el dígito de las decenas dividiendo por 10 y obteniendo la parte entera
    des_digit = num // 10
    unidades_left=num % 10
    print(des_digit)
    return  unidades_left, des_digit


   
# Invoke the function with any two-digit integer as its argument
print(swap_digits(30))
