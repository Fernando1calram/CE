# Prueba
def intercambio_variables():
    a = input("Introduce el valor de a: ")
    b = input("Introduce el valor de b: ")
    print("Antes del intercambio: a =", a, ", b =", b)
    a, b = b, a
    print("Después del intercambio: a =", a, ", b =", b)

intercambio_variables();