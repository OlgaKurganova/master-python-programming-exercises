# Your code here
def sequence_of_words(input_string):
    # Dividir la cadena en una lista de palabras
    words = input_string.split(",")
    # Ordenar la lista alfabéticamente
    words_sorted = sorted(words)
    # Unir las palabras ordenadas en una cadena separada por comas
    result = ",".join(words_sorted)
    # Imprimir el resultado
    print(result)

# Ejemplo de uso
input_string = "banana,apple,orange,grape"
sequence_of_words(input_string)




# como se usa split
# text = "Este es un texto de ejemplo"
# print(text.split())
#resultado["Este", "es", "un", "texto", "de", "ejemplo"]

#color_string = "azul#rojo#amarillo#naranja"
#colores = color_string.split ( "#", 1 )
#print (colores)
#["azul", "rojo#amarillo#naranja"]

  ##a = [5, 1, 4, 3]
  ##print(sorted(a))  ## [1, 3, 4, 5]
  ##print(a)  ## [5, 1, 4, 3]