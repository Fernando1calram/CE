# Pedimos la temperatura
temperatura = float(input("Introduce la temperatura: "))

# Función para convertir a Fahrenheit
def convierte_fahrenheit(grados):
    return (grados * (9/5) + 32)

# Llamada a la función y muestra de resultados
print(str(temperatura) + "ºC = " + str(convierte_fahrenheit(temperatura)) + "ºF")