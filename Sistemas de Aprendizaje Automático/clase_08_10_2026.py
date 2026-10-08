# Ejemplo 1
"""print("----- Asignaturas optativas -----")

opcion = input("Escribe la asignatura a elegir: ")
asignatura = opcion.lower()

if asignatura in ("informática gráfica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida " + asignatura)
else:
    print("La asignatura elegida no se contempla")"""

# Ejemplo 2
"""for i in [1,2,3]:
    print("Hola")"""

# Ejemplo 2.1
"""for estaciones_anio in ["primavera","verano","otoño","invierno"]:
    print(estaciones_anio)"""

# Ejemplo 3
"""contEmail = 0
contPunto = 0

miEmail = input("Introduce tu dirección de email: ")

for i in miEmail:

    if(i == "@"):
        contEmail = contEmail + 1
    elif (i == "."):
        contPunto = contPunto + 1

if (contEmail == 1 and(contPunto >= 1 and contPunto <= 4)):
    print("El email es correcto")
else:
    print("El email no es correcto")"""

# Ejemplo 4
"""for i in range(5):
    print(i)"""

"""for i in range(5,50,3):
    print(i)"""

"""valido = False
email = input("Introduce tu email: ")

for i in range(len(email)):
    if email[i] == "@":
        valido = True

if valido:
    print("Email correcto")
else:
    print("Email incorrecto")"""

# Ejemplo 5
"""citricos = ["limon","naranja","pomelo","lima"]
for fruta in citricos:
    print(fruta)
for numero in range(3):
    print(f"Número: {numero}")
for numero in range(len(citricos)):
    print(f"P: {numero} - V: {citricos[numero]}")"""

# Ejemplo 6
"""i = 1

while i <= 10:
    print("Ejecución: " + str(i))
    i = i + 1

print("Teminó la ejecución")"""

# Ejemplo 6.1
"""edad = int(input("Introduce tu edad: "))

while edad < 5 or edad > 100:
    print("Has introducido una edad erronea. Vuelva a intentarlo")
    edad = int(input("Introduce tu edad: "))

print("Gracias")
print("Edad del usuario: " + str(edad))"""

# Ejemplo 6.2
"""import math

print("--- Programa de calculo de raíz cuadrada ---")
numero = int(input("Introduce un numero: "))

intentos = 0

while numero < 0:
    print("No se puede hallar la raíz de un número negativo")

    if intentos == 2:
        print("Has consumido demasiados intentos")
        print("El programa ha finalizado")
        break

    numero = int(input("Introduce un numero: "))

    if numero < 0:
        intentos = intentos + 1

if intentos < 2:
    solucion = math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es: " + str(solucion))"""

# Ejemplo 7
"""for letra in "Python":
    if letra == "h":
        continue
    print("Letra: " + letra)

class MiClase:
    pass

nombre = "fernando calles"

contador = 0

for i in nombre:
    if i == " ":
        continue
    contador += 1

print(contador)"""

# Ejemplo 8
"""def generaPares(limite):
    num = 1

    while num < limite:
        yield num * 2
        num = num + 1
    
devuelvePares = generaPares(10)
print(next(devuelvePares))
print("-----------------")
print(next(devuelvePares))
print("-----------------")
print(next(devuelvePares))"""

# Ejemplo 9
"""def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield from elemento

ciudades_devueltas = devuelve_ciudades("Madrid","Zamora","Valladolid","Cuenca")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))"""

# Ejemplo 10
"""numero1 = 100
numero2 = 0

try:
    print(numero1 / numero2)
except ZeroDivisionError:
    print("Error al dividir entre cero")
except:
    print("Error")
else:
    print("La división se calculo correctamente")
finally:
    print("Fin del programa")"""

# Ejemplo 11
"""def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplica(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        op1 = (float(input("Introduce el primer número: ")))
        op2 = (float(input("Introduce el segundo número: ")))
        return num1 / num2
    except ValueError:
        print("El valor introducido es erroneo")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    finally:
        print("Calculo finalizado")

while True:
    try:
        op1 = (int(input("Introduce el primer número: ")))
        op2 = (int(input("Introduce el segundo número: ")))
        break

    except ValueError:
        print("Los valores introducidos no son correctos. Inténtalo de nuevo")


operacion = input("Introduce la operación a realizar (sum,resta,multiplica,divide): ")

if operacion == "suma":
    print(suma(op1,op2))
elif operacion == "resta":
    print(resta(op1,op2))
elif operacion == "multiplica":
    print(multiplica(op1,op2))
elif operacion == "divide":
    print(divide(op1,op2))
else:
    print("Operación no contemplada")

print("Operación ejecutada: Continuación de ejecución del programa")"""

# Ejercicio 12
"""def evaluaEdad(edad):
    if edad < 0:
        raise TypeError("No se permiten edades negativas")
    if edad < 20:
        print("Eres muy joven")"""

# Ejercicio 13
import math
def calculaRaiz(num1):
    if num1 < 0:
        raise ValueError("El número no puede ser negativo")
    else:
        return math.sqrt(num1)

op1 = (int(input("Introduce un error: ")))

try:
    print(calculaRaiz(op1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print("Programa teminado")