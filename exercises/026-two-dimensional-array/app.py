# Your code here
def  two_dimensional_list(x,y):
    matrix = [[i * j for j in range(y)] for i in range(x)]
    return matrix
x = 3  # número de filas
y = 5  # número de columnas

result = two_dimensional_list(x,y)

for row in result:
    print(row)