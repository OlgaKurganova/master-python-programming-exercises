def hours_minutes(seconds):
  # Your code here
  # Calcula el número de horas
    hours = seconds // 3600
    
    # Calcula el número de minutos restantes después de extraer las horas
    minutes = (seconds % 3600) // 60
    
    # Retorna las horas y los minutos como una tupla
    return hours, minutes

# Invoke the function and pass any integer as its argument
print(hours_minutes(3900))
