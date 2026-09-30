def invertir_palabras(palabra):
    # No necesita parámetro el split en este caso, por defecto es el espacio
    list = palabra.split()
    list.reverse()
    return " ".join(list)

print(invertir_palabras("Hola mundo Python"))
print(invertir_palabras("IA es el futuro"))