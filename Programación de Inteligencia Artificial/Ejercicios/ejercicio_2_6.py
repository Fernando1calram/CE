def invertir_palabra(palabra):
    list = palabra.split(" ")
    list.reverse()
    return " ".join(list)


print(f"Invertir palabra: {invertir_palabra("Hola mundo Python")}")