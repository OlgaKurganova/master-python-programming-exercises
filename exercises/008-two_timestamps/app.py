def two_timestamp(hr1, min1, sec1, hr2, min2, sec2):
    # Your code here   
    # Convertir ambas marcas de tiempo a segundos
    time1_in_seconds = hr1 * 3600 + min1 * 60 + sec1
    time2_in_seconds = hr2 * 3600 + min2 * 60 + sec2
    
    # Calcular la diferencia en segundos
    difference_in_seconds = time2_in_seconds - time1_in_seconds
    
    return difference_in_seconds

# Invoke the function and pass two timestamps(6 intergers) as its arguments
print(two_timestamp(1,1,1,2,2,2))
