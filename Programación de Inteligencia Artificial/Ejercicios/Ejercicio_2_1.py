# Función para clasificar la edad
def clasificar_edad(edad):
    if(edad < 2):
        return "Bebé"
    elif(edad >= 2 and edad < 13):
        return "Niño"
    elif(edad >= 13 and edad < 18):
        return "Adolescente"
    elif(edad >= 18 and edad < 65):
        return "Adulto"
    else:
        return "Adulto mayor"

# Llamada a la función asignando con IN las edades a clasificar
for edad in [1, 5, 15, 25, 70]:
    print(f"{edad} años -> {clasificar_edad(edad)}")