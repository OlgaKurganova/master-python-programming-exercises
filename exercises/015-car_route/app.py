# Complete the function to return the amount of days it will take to cover a route
import math

def car_route(n,m):

  days = math.ceil(m / n)

  # Verificamos si hay una distancia restante que necesita un día adicional
     #  if M % N != 0:
        #   days += 1

  return days


# Invoke the function with two integers
print(car_route(20,40))
