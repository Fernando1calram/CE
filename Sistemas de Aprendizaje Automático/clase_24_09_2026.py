# Ejemplo 1
"""numero = 10
Numero = 20
saludo = "Hola Mundo"
print(numero)
print(Numero)
print(numero + Numero)
print("Saludo " + saludo)
print(type(numero))
print(type(saludo))"""

# Ejemplo 2
"""a = 5
b = 10
a,b = b,a
print(a)
print(b)"""

# Ejemplo 3
"""a = 5
b = "25"
c = "25.7"
print("Número: " + str(a))
print(int(b))
print(float(c))"""

# Ejemplo 4
"""cadena = "Hola mundo"
print(cadena)
print(cadena[2])
print(cadena[2:])
print(cadena[:2])
print(cadena[2:6])
print(cadena[-2])
print(len(cadena))"""

# Ejemplo 5
from datetime import datetime

"""datenow1 = datetime.now().date()
print("Fecha: ", datenow1)
datenow2 = datetime.now()
print("Fecha: ", datenow2)
print("Año: ", datenow2.year)
print("Mes: ", datenow2.month)
print("Día: ", datenow2.day)
print(f"Hola:  {datenow2.hour}:{datenow2.minute}")"""

# Ejemplo 6
"""fecha = "10-11-2018"
obj = datetime.strptime(fecha, "%m-%d-%Y").date()
print(obj)
print(f"{obj.day}-{obj.month}-{obj.year}")"""""

# Ejemplo 7
"""fecha = datetime.now()
print(fecha.strftime("%A, %d %b %Y"))"""

# Ejemplo 8
#mensaje = """Hola Claudio Moyano
#, estoy introduciendo
#saltos de línea"""

#print(mensaje)

# Ejemplo 9
"""def mensaje():

    print("Aquí ponemos la sentencia uno")
    print("Aquí ponemos la sentencia dos")
    print("Aquí ponemos la sentencia tres")

mensaje()

print("---------------------------------------")

mensaje()"""

# Ejemplo 10
"""def suma(num1, num2):
    resultado = num1 + num2
    return resultado

almacena_resultado = suma(35,70)

print(almacena_resultado)"""

# Ejemplo 11
"""def calcular_precio_final(precio, iva=0.21):
    return precio * (1 - iva)

precio = calcular_precio_final(100)
print(precio)

precio_reducido = calcular_precio_final(100,0.10)
print(precio_reducido)"""

# Ejemplo 12
"""def calcular_promedio(*numeros):
    if not numeros:
        return 0

    return sum(numeros) / len(numeros)

print(calcular_promedio(10,20,30))
print(calcular_promedio(5,10,15,20,25))"""