"""matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

aplanada = [num for f in matriz for num in f]
print(f"aplanada: {aplanada}")

pares_matriz = [num for f in matriz for num in f if num % 2 == 0]
print(f"pares: {pares_matriz}")

sumas_fila = [sum(f) for f in matriz]
print(f"sumas: {sumas_fila}")"""

# TUPLAS

"""coordenadas = (10,20)
punto3d = (1,2,3)
un_elemento = (42,)

x, y = coordenadas
print(f"coordenadas: ({x}, {y})")

a,b,c = punto3d;
print(f"3D: x={a}, y={b}, z={c}")

primero, *resto = (10,20,30,40,50)
print(f"primero={primero}, resto{resto}")"""

# DICCIONARIOS

"""alumno = {
    "nombre": "Ana García",
    "edad": 22,
    "carrera": "Inteligencia Artificial",
    "notas": [8.5, 9.0, 7.5]
}"""

#print(f"Nombre: {alumno["nombre"]}")
#print(f"Domicilio: {alumno.get("domicilio", "No especificado")}")

"""alumno["email"] = "ana@universidad.edu"
alumno["edad"] = 23
print(f"Actualizado: {alumno}")

del alumno["email"]
nota_borrada = alumno.pop("notas")
print(f"Notas borradas: {nota_borrada}")
print(f"Actualizado: {alumno}")

print(f"Claves: {list(alumno.keys())}")
print(f"Valores: {list(alumno.values())}")

print(f"Recorriendo: ")
for clave, valor in alumno.items():
    print(f" {clave}: {valor}")"""

"""numeros = [1,2,3,4,5]
cuadrados = {n: n**2 for n in numeros}
print(f"cuadrados {cuadrados}")"""

"""inventario = {"manzana":10, "platano": 2, "uva": 5}
invertido = {v: k for k, v in inventario.items()}
print(f"Invertido: {invertido}")

mayores_5 = {k: v for k, v in inventario.items() if v > 5}
print(f"Mayores que 5: {mayores_5}")"""

"""precios = {"laptop": 999.99, "telefono": 123.32, "auriculares": 254.69}
descuento = {k: v * 0.9 for k, v in precios.items()}
print(f"Precios con descuento: {descuento}")"""

# ZIP

"""nombres = ["manzana", "pera", "uva"]
precios = [1.2, 0.9, 8.5]
frutas_precios = zip(nombres, precios)
print(f"Lista: {list(frutas_precios)}")
print(f"Otra vez: {list(frutas_precios)}")"""

"""nombres = ["manzana", "platano", "pera"]
precios = [1.2, 0.8, 2.5]
frutas_precios = zip(nombres, precios)
almacenado = list(frutas_precios)
print(f"Frutas y precios: {almacenado}")
print(f"Volvemos a mostrarlo: {almacenado}")"""

"""pares = [(1, 'a', 3), (2, 'b', 5), (3, 'c', 7)]
numeros, letras, mas_numeros = zip(*pares)
print(numeros)  # (1, 2, 3)
print(letras)   # ('a', 'b', 'c')
print(mas_numeros) # (3, 5, 7)"""

"""palabra = "banana"
frecuencia = {}
for letra in palabra:
    frecuencia[letra] = frecuencia.get(letra, 0) +1
print(f"Frecuencia de letras en banana: {frecuencia}")"""

# CONJUNTOS

"""numeros_set = {1,2,3,4,5}
numeros_dupes = {1,2,2,3,3,4,5}
print(f"original: {numeros_set}")
print(f"dupes: {numeros_dupes}")

lista_con_dupes = [1, 2, 2, 3, 3, 4, 5]
sin_dupes = set(lista_con_dupes)
print(f"sin dupes: {sin_dupes}")"""

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
print(f"{a ^ b}")

mi_set = {1, 2, 3}
mi_set.add(4)
print(f"Después de add(4): {mi_set}")

mi_set.discard(99)  # sin error si no existe
print(f"Después de discard(99): {mi_set}")