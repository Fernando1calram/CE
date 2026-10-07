def filtrar_y_transformar(lista, criterio):
    lista_resultado = []
    # Recorro lista
    for n in lista:
        # Si n cumple lo que pasemos como criterio lo añade al resultado
        if(criterio(n)):
            lista_resultado.append(n * 2)
    return lista_resultado

numeros = [1,3,7,10,2,15]
resultado = filtrar_y_transformar(numeros, lambda x: x > 5)
print(f"Resultado: {resultado}")