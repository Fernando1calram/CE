import numpy as np

array = np.arange(1,25)
print(array)

# 1

# Array en forma de (4,6)
# Array en forma de (2,3,4)
partes_4_6 = array.reshape(4,6)
print("Array en forma de (4,6):\n", partes_4_6)

partes_2_3_4 = array.reshape(2,3,4)
print("Array en forma de (2,3,4):\n", partes_2_3_4)

# 2

# Aplanar matriz con flatten
partes_4_6_flattened = partes_4_6.flatten()
print("Con flatten: ", partes_4_6_flattened)
partes_4_6_flattened[1] = 85
print("Con flatten y cambio: ", partes_4_6)

partes_4_6_raveled = partes_4_6.ravel()
print("Con raveled: ", partes_4_6_raveled)
partes_4_6_raveled[1] = 85
print("Con raveled y cambio: ", partes_4_6)

# 3

array_3d_1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
array_3d_2 = np.array([[10,11,12],[13,14,15],[16,17,18]])

# Concatenar verticalmente
vertical = np.stack([array_3d_1, array_3d_2], axis=0)
print("Vertical: ", vertical)

# Concatenar horizontalmente
horizontal = np.stack([array_3d_1, array_3d_2], axis=1)
print("Horizontal: ", horizontal)

# 4

array_4 = np.arange(1,21)
print(array_4)

en_4 = np.split(array_4, 4)
print(en_4)

en_3 = np.array_split(array_4, 4)
for i, p in enumerate(en_3):
    print(f" Parte {i}:", p)

# 5

v = np.array([1,2,3])
print("Sin expandir: ", v)
v_expandido = np.expand_dims(v, axis = 0)
print("Expandido: ", v_expandido)