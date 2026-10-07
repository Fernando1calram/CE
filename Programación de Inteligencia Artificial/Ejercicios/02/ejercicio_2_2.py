# Tu solucion aqui
numeros = [4, 7, 12, -3, 0]

for n in numeros:

    # Asignamos resultado a PAR y si el MODULO de n es distinto de 0 que cambie a IMPAR
    resultado = "PAR" if n % 2 == 0 else "IMPAR"
    print(f"{n} -> {resultado}")