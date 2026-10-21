numeros = [2, 3, 5, 7, 11, 13, 14, 15, 17, 18, 19, 20, 21, 23]
palabras = ["ana", "elefante", "uva", "arbol", "oso", "perro", "higo"]

# 1. Solo los números primos
primos = [n for n in numeros if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))]
print("Primos: " + primos)

# 2. Diccionario {numero: raiz_cuadrada} para numeros > 5
raices = {n: n**0.5 for n in numeros if n > 5}
print("Raices: " + raices)

# 3. Conjunto con los caracteres únicos de todas las palabras
caracteres = {c for palabra in palabras for c in palabra}
print("Caracteres: " + caracteres)

# 4. Palabras que empiezan por vocal, convertidas a mayúscula
vocales = [p.upper() for p in palabras if p[0] in "aeiou"]
print("Vocales " + vocales)
 