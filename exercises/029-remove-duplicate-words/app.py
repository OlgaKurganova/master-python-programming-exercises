# Your code here
def remove_duplicate_words(input_string):
    # Dividir el string en palabras
    words = input_string.split()
    # Usar set para eliminar duplicados y luego ordenar alfabéticamente
    unique_words = sorted(set(words))
    # Unir las palabras únicas en un string de nuevo, separadas por espacios
    result = " ".join(unique_words)
    return result

# Ejemplo de uso
input_string = "gato perro perro caballo gato caballo"
resultado = remove_duplicate_words(input_string)
print(resultado)



#s = set([5, 4, 6, 8, 8, 1])

#print(s)       #{1, 4, 5, 6, 8}

#print(type(s)) #<class 'set'>