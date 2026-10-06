"""with open("ejemplo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Linea 1: Hola Mundo\n")
    archivo.write("Linea 2: Python es genial\n")
    archivo.write("Linea 3: Trabajando con archivos\n")"""

"""with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)

with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
    for i, linea in enumerate(archivo, 1):
        print(f"  Linea {i}: {linea.strip()}")

with open("ejemplo.txt", "a", encoding="utf-8") as archivo:
    archivo.write("Linea 4: Agregada con append\n")

with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
    print(archivo.read())"""

"""import csv

datos = [
    ["Nombre", "Edad", "Ciudad"],
    ["Ana", 25, "Madrid"],
    ["Carlos", 30, "Barcelona"],
    ["Beatriz", 22, "Valencia"],
]

with open("datos.csv", "w", encoding="utf-8", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos)

print("Contenido de datos.csv:")
with open("datos.csv", "r", encoding="utf-8") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(f"  {fila}")

with open("datos.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(f"  {fila["Nombre"]} tiene {fila["Edad"]} años, vive en {fila["Ciudad"]}")"""

import math
import os
from datetime import datetime
from collections import Counter, defaultdict

"""# math: funciones matematicas
print(f"PI = {math.pi:.4f}")
print(f"raiz(2) = {math.sqrt(2):.4f}")
print(f"2^10 = {math.pow(2, 10):.0f}")
print(f"ceil(3.2) = {math.ceil(3.2)}")
print(f"floor(3.8) = {math.floor(3.8)}")

# os: operaciones con sistema de archivos
print(f"Directorio actual: {os.getcwd()}")

# datetime: fechas y horas
ahora = datetime.now()
print(f"Fecha/hora actual: {ahora.strftime("%Y-%m-%d %H:%M:%S")}")

palabras = ["manzana", "platano", "manzana", "pera", "platano", "manzana"]
contador = Counter(palabras)
print(f"Contador de palabras: {contador}")
print(f"Más común: {contador.most_common(1)[0]}")"""

from pathlib import Path

ruta = Path(".")

for archivo in ruta.glob("*.py"):
    print(f"  {archivo.name} ({archivo.stat().st_size} bytes)")

print(f"ejemplo.txt existe: {Path("ejemplo.txt").exists()}")
print(f"no_existe.txt existe: {Path("no_existe.txt").exists()}")

directorio = Path("carpeta_ejemplo")
directorio.mkdir(exist_ok=True)
print(f"Directorio creado: {directorio.absolute()}")

# Unir rutas
ruta_completa = Path("carpeta_ejemplo") / "archivo.txt"
print(f"Ruta completa: {ruta_completa}")
print(f"Extension: {ruta_completa.suffix}")  # .txt
print(f"Nombre sin extension: {ruta_completa.stem}")  # archivo

import shutil
shutil.rmtree("carpeta_ejemplo")
print("Directorio de ejemplo eliminado.")