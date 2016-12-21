import numpy as np
fila = 1
columna = 2

matriz = [[1,3,6],
    [5,7,9],
    [3,18,0]]

print (matriz[fila][columna])

arreglo = np.array(matriz)
print (arreglo)

valor_max = np.max(arreglo)
print (valor_max)

matriz = np.random.randint(1,50,(10,5))
print (matriz)

print (np.sum(matriz))

print (np.sum(matriz,axis = 1))