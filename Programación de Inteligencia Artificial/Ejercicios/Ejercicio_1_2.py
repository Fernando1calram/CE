def grados():
    return float(input("Introduce los grados en Celsius: "))

def convertir_a_fahrenheit(grados):
    return (grados * 9/5) + 32

def mostrar(grados):
    print("Los grados en Fahrenheit son: " + f'{convertir_a_fahrenheit(grados)}')

mostrar(grados())