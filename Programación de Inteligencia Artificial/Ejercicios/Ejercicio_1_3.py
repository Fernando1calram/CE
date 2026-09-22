#Introducimos los valores de a y b
a = input("Introduce un valor para a: ")
b = input("Introduce un valor para b: ")

# Esribimos sus valores actuales
print("a = " + a + " b = " + b)

# Intercambiamos sus valores
a, b = b, a

# Mostramos sus nuevos valores
print("a = " + a + " b = " + b)