# Con split separa el texto en una lista
texto = "Hola hola Hola Python python PYTHON"
acumula = ""
list = []

for i in range(len(texto)):
    if(texto[i] != " " ):
        acumula += texto[i].lower()
    else:
        list.append(acumula)
        acumula = ""

if (acumula != ""):
    list.append(acumula)

frecuencia = {}

for palabra in list:
    frecuencia[palabra] = frecuencia.get(palabra, 0) +1

print(f"{frecuencia}")