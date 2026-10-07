import csv

datos = [
    ["Nombre", "Edad", "Nota"],
    ["Ana", 22, 8.5],
    ["Carlos", 24, 9.2],
    ["Beatriz", 21, 10],
    ["David", 23, 6.5],
    ["Elena", 22, 9.8],
]

with open("registro.csv", "w", encoding="utf-8", newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos)
print("Archivo datos.csv creado.")

"""with open("registro.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    notas = []
    for fila in lector:
        notas.append(float(fila["Nota"]))
print(f"La nota media es: {sum(notas)/len(notas)}")"""

# SIN DICCIONARIO
"""with open("registro.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    alumno_notas = {}
    mayor_nota = 0
    nombre_nota = ""
    for fila in lector:
        if(mayor_nota < float(fila["Nota"])):
            mayor_nota = float(fila["Nota"])
            nombre_nota = fila["Nombre"]
    print(f"El alumno con mayor nota es: {nombre_nota} con un {mayor_nota}")"""

# CON DICCIONARIO
with open("registro.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    alumno_notas = {}
    for fila in lector:
        alumno_notas[fila["Nombre"]] = float(fila["Nota"])
mayor_nota = max(alumno_notas, key=alumno_notas.get)
print(f"La alumna con mayor nota es: {mayor_nota}")