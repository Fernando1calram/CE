import numpy as np

np.random.seed(42)

# 1. CREAR ARRAYS

valoraciones = np.array([8.5,7.0,9.2,6.5,8.8,5.9])
anios = np.array([1972,1994,2008,2019,2021,2023])
actores_por_pelicula = np.array([2,4,3,5,6,2])

# COMPROBACIONES

assert isinstance(valoraciones, np.ndarray)
assert isinstance(anios, np.ndarray)
assert isinstance(actores_por_pelicula, np.ndarray)

assert valoraciones.shape == (6,)
assert anios.shape == (6,)
assert actores_por_pelicula.shape == (6,)

print("1. Creación de arrays ✓")
print(f"    Valoraciones: {valoraciones}")
print(f"    Años: {anios}")
print(f"    Actores por película: : {actores_por_pelicula}")

# 2. PROPIEDADES DE LOS ARRAYS

# Matriz de 2 filas y 3 columnas con valoraciones
matriz_valoraciones = np.array([[8.5,7.0,9.2],[6.5,8.8,5.9],])

# Guardamos en estas variables las propiedades de la matriz
forma = matriz_valoraciones.shape
dimensiones = matriz_valoraciones.ndim
tamano_total = matriz_valoraciones.size
tipo_dato = matriz_valoraciones.dtype

assert forma == (2,3)
assert dimensiones == 2
assert tamano_total == 6
assert tipo_dato == np.float64

print("2. Propiedades de arrays ✓")
print(f"    Forma: {forma}")
print(f"    Dimensiones: {dimensiones}")
print(f"    Tamaño total: {tamano_total}")
print(f"    Tipo de dato: {tipo_dato}")

# INDEXACIÓN Y SLICING

# De matriz_valoraciones:

# Valoración de la primera película, tercera posición (fila 0 columna 2)
primera_pelicula_tercera_valoracion = matriz_valoraciones[0,2]

# Valoración de la segunda película, primera posición (fila 1 columna 0)
segunda_pelicula_primera_valoracion = matriz_valoraciones[1,0]

# Todas las valoraciones de la primera película
primera_fila = matriz_valoraciones[0, :]

# Todas las valoraciones de la segunda columna
segunda_columna = matriz_valoraciones[:, 1]

# Dos primeras valoraciones de la segunda película
dos_primeras_segunda_pelicula = matriz_valoraciones[1, 0:2]

assert primera_pelicula_tercera_valoracion == 9.2
assert segunda_pelicula_primera_valoracion == 6.5

assert np.array_equal(primera_fila, np.array([8.5,7.0,9.2]))
assert np.array_equal(segunda_columna, np.array([7.0,8.8]))
assert np.array_equal(dos_primeras_segunda_pelicula, np.array([6.5,8.8]))

print("3. Indexación y slicing ✓")
print(f"    Primera película, tercera valoración: {primera_pelicula_tercera_valoracion}")
print(f"    Segunda película, primera valoración: {segunda_pelicula_primera_valoracion}")
print(f"    Primera fila: {primera_fila}")
print(f"    Segunda columna: {segunda_columna}")
print(f"    Dos primeras valoraciones de la segunda película: {dos_primeras_segunda_pelicula}")

# 4. OPERACIONES VECTORIALES

# Convierte todas las valoraciones de valoraciones a una escala de 0 a 100 (valoracion * 10)
valoraciones_sobre_100 = valoraciones * 10

# Cuantos años han pasado desde cada estreno hasta 2026
anios_desde_estreno = 2026 - anios

# Calcula la valoracion media de todas las peliculas
valoracion_media = np.mean(valoraciones)

# Calcula la valoración máxima
valoracion_maxima = np.max(valoraciones)

# Calcula la valoración mínima
valoracion_minima = np.min(valoraciones)

assert np.allclose(valoraciones_sobre_100, [85.0,70.0,92.0,65.0,88.0,59.0])
assert np.array_equal(anios_desde_estreno, [54,32,18,7,5,3])

assert abs(valoracion_media - 7.65) < 0.01
assert valoracion_maxima == 9.2
assert valoracion_minima == 5.9

print("4. Operaciones vectorizadas ✓")
print(f"    Valoraciones sobre 100: {valoraciones_sobre_100}")
print(f"    Años desde estreno: {anios_desde_estreno}")
print(f"    Valoracion media: {valoracion_media}")
print(f"    Valoracion maxima: {valoracion_maxima}")
print(f"    Valoracion minima: {valoracion_minima}")

# 5. INDEXACIÓN BOOLEANA

# Máscara booleana con true si la valoración es valoracion >= 8
peliculas_buenas = valoraciones >= 8

# Máscara para obtener solo las valoraciones buenas
valoraciones_buenas = valoraciones[peliculas_buenas]

# Máscara para obtener los años de las películas buenas
anios_peliculas_buenas = anios[peliculas_buenas]

# Cuántas películas tienen valoración >= 8
cantidad_buenas = np.sum(peliculas_buenas)

assert np.array_equal(peliculas_buenas, [True, False, True, False, True, False])
assert np.array_equal(valoraciones_buenas, [8.5,9.2,8.8])
assert np.array_equal(anios_peliculas_buenas, [1972,2008,2021])
assert cantidad_buenas == 3

print("5. Indexación booleana ✓")
print(f"    Máscara: {peliculas_buenas}")
print(f"    Valoraciones buenas: {valoraciones_buenas}")
print(f"    Años de las peliculas buenas: {anios_peliculas_buenas}")
print(f"    Cantidad de películas buenas: {cantidad_buenas}")

# 6. CONCATENAR Y DIVIDIR ARRAYS

# Valoraciones de tres películas adicionales
nuevas_valoraciones = np.array([7.7,8.1,6.8])

# Años de peliculas adicionales
nuevos_anios = np.array([2015,2018,2024])

# Concatenar valoraciones y nuevas valoraciones en un único array
todas_valoraciones = np.concatenate((valoraciones, nuevas_valoraciones))

# Concatena anios y años nuevos en un único array
todos_anios = np.concatenate((anios, nuevos_anios))

# Divide todas las valoraciones en dos partes: 3 primeras películas y 3 últimas
primeras_tres = todas_valoraciones[:3]
ultimas_tres = todas_valoraciones[-3:]

# Divide todas las valoraciones en 3 partes iguales
partes_valoraciones = np.split(todas_valoraciones, 3)

# Comprobaciones
assert len(todas_valoraciones) == 9
assert len(todos_anios) == 9

assert np.array_equal(primeras_tres, [8.5,7.0,9.2])
assert np.array_equal(ultimas_tres, [7.7,8.1,6.8])

assert len(partes_valoraciones) == 3
assert np.array_equal(partes_valoraciones[0], [8.5, 7.0, 9.2])
assert np.array_equal(partes_valoraciones[1], [6.5, 8.8, 5.9])
assert np.array_equal(partes_valoraciones[2], [7.7, 8.1, 6.8])

print("6. Concatenación y división ✓")
print(f"   Todas las valoraciones: {todas_valoraciones}")
print(f"   Todos los años: {todos_anios}")
print(f"   Primeras tres: {primeras_tres}")
print(f"   Últimas tres: {ultimas_tres}")
print(f"   Partes: {partes_valoraciones}\n")

print("=" * 55)
print("  ¡TODAS LAS PRUEBAS PASADAS!")
print("=" * 55)