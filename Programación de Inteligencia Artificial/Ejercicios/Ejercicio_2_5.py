texto = "Hola hola python Hola Python PYTHON"
palabra = ""
list = []

for i in texto:
    if(i != " " and i != "\n"):
        palabra  += i
    else:
        list.append(palabra.lower())
        palabra =""
if palabra:
    list.append(palabra.lower())
    list.sort()

# MÍO
#for i, palabra in enumerate(list):
#    if(list[i] != list[i+1] or list[i] != len(list)):
#        print(f"La palabra {list[i]} aparece {list.count(list[0])}")

# IA
# Recorrer con índice, controlando el último elemento
for i in range(len(list)):
    # Si no es el último y la siguiente palabra es distinta
    if i < len(list) - 1 and list[i] != list[i + 1]:
        print(f"La palabra {list[i]} aparece {list.count(list[i])} veces")
    # Si es el último elemento
    elif i == len(list) - 1:
        print(f"La palabra {list[i]} aparece {list.count(list[i])} veces")