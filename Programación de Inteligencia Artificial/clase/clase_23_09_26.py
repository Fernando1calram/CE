# Recorriendo una lista
#frutas = ["manzana", "platano", "pera", "naranja"]
#for fruta in frutas:
#    print(f"Me gusta la {fruta} \n")

# Recorriendo carácteres de una cadena de texto
#for letra in "Fernando":
#    print(letra, end=" ")

# Recorriendo los 5 primeros valores
#for i in range(5):
#    print(i, end=" ")

# Recorriendo los valores comprendidos entre el primer y el segundo parámetro
#for i in range(2,8):
#    print(i, end=" ")

# Recorriendo los valores comprendidos entre el primer y el segundo parámetro
# haciendo saltos según el tercer parámetro
#for i in range(0, 10, 2):
#    print(i, end=" ")

#edades = {"Fernando": 26, "María": 25, "Ana": 36, "Carlos": 24}
#for nombre in edades:
#    Sacamos el nombre que recorre el for y la edad pasando la clave
#    print(f"{nombre}: {edades[nombre]}")

#for nombre, edad in edades.items():
#    Recorremos la clave y el valor del diccionario (RECOMENDADO)
#    print(f" {nombre} tiene {edad} años")

texto = "Python"
invertido = ""

for i in range(len(texto) - 1, -1, -1):
    invertido += texto[i]
#print(f"{texto} invertido -> {invertido}")

suma = 0
for i in range(1,101):
    suma += i
#print(f"{suma}")

numeros = [3, 7, 1, 9, 4, 8]
for n in numeros:
    if n == 9:
#       print(f"Encontrado {n}")
        break
#   print(n, end=" ")

for i in range(1, 11):
    if i % 2 == 0:
        continue
#   print(i, end=" ")

for letra in "Hola":
    if letra == "l":
        pass
#   else:
#       print(letra, end=" ")

cuadrados = []
for numero in range(1,6):
    cuadrados.append(numero ** 2)

print(f"Sin compresión:  {cuadrados}")

cuadrados2 = [numero ** 2 for numero in range(1,6)]
print(f"Con compresión: {cuadrados2}")

cuadrados3 = [numero ** 2 for numero in range(1,6) if numero % 2 == 0]
print(f"Con compresion y condicion: {cuadrados3}")

numeros = list(range(1,11))
etiquetas = ["par" if n % 2 == 0 else "impar" for n in numeros]
print(f"Etiquetas: {list(zip(numeros, etiquetas))}")

valores = [-3, 5, -1, 8, -7, 2]
# Convierte los negativos a 0
positivos = [v if v > 0 else 0 for v in valores]
print(f"Valores positivos {positivos}")