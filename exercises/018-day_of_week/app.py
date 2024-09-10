# Complete the function to return the number of day of the week for k'th day of year
def day_of_week(k):

  # Día 0 es jueves (1 de enero)
    days_of_week = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
     # Calculamos el día de la semana para el k-ésimo día
    day_index = (k - 1) % 7  # Restamos 1 porque el primer día es jueves (día 0)
    
    # Devolvemos el nombre del día de la semana correspondiente
    return days_of_week[day_index]

    


# Invoke function day_of_week with an integer between 1 and 365
print(day_of_week())



    
   
# Ejemplo de uso
print(day_of_week(1))  # Debería devolver "Thursday"
print(day_of_week(2))  # Debería devolver "Friday"
print(day_of_week(365))  # Último día del año, debería devolver "Thursday"
