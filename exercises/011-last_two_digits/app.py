# Complete the function to print the last two digits of an integer greater than 9
def last_two_digits(num):
    last_two = num % 100
    
    # Imprimir los últimos dos dígitos
    print(last_two)
    
   
# Invoke the function with any integer greater than 9
print(last_two_digits(1234))
