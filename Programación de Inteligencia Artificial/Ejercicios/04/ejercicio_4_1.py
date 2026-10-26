import numpy as np

temperaturas = np.array([18,22,19,25,21,20,23])
# 1
print("Tercer día", temperaturas[2])
# 2
print("Del segundo al quinto día", temperaturas[1:5])
# 3
print("Array invertido", temperaturas[::-1])
# 4
numeros = np.arange(1, 13).reshape(4, 3)
print(numeros)
filas_columnas = numeros[[0, 2], 1:3]
print("Columna 1 y 2 de las filas 0 y 2",filas_columnas)
# 5 

view = temperaturas.view()
print(view)
copy = temperaturas.copy()
print(copy)

temperaturas[0] = 12

print(view)
print(copy)