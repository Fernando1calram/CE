def procesar_lista(lista):
    try:
        if not lista:
            raise ValueError(f"La lista está vacía")
        suma = 0
        for n in lista:
            try:
                if n < 0:
                    raise ValueError()
                suma += n
            except TypeError:
                print(f"Error: tipo de dato incorrecto")
            except ValueError:
                print(f"{n} es un número negativo")
        return suma

    except ValueError as e:
            print(f"Error: {e}")
            return 0

# Pruebas
#print(procesar_lista([1, 2, 3, "hola","b", 4]))
#print(procesar_lista([10, 20, -4, 30]))
print(procesar_lista([]))