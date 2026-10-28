import numpy as np

grupo_a = np.array([7.5,8.0,6.5,9.0,7.0])
grupo_b = np.array([8.5,7.0,7.5,8.0,6.5])

# 1

# SUMA
suma = grupo_a + grupo_b
print("Suma ", suma)

# RESTA
resta = grupo_a - grupo_b
print("Resta ", resta)

# MULTIPLICACIÓN
multiplicacion = grupo_a * grupo_b
print("Multiplicación ", multiplicacion)

# DIVISIÓN
division = grupo_a / grupo_b
print("División ", division)

# 2

# MEDIA
media_a = np.mean(grupo_a)
media_b = np.mean(grupo_b)
print("Media A ", media_a)
print("Media B ", media_b)

# MEDIANA
mediana_a = np.median(grupo_a)
mediana_b = np.median(grupo_b)
print("Mediana A ", mediana_a)
print("Mediana B ", mediana_b)

# DESVIACIÓN ESTÁNDAR
desviacion_a = np.std(grupo_a)
desviacion_b = np.std(grupo_b)
print("Desviación A ", desviacion_a)
print("Desviación B ", desviacion_b)

# VARIANZA
varianza_a = np.var(grupo_a)
varianza_b = np.var(grupo_b)
print("Varianza A ", varianza_a)
print("Varianza B ", varianza_b)

# 3

grupo_a_t = np.transpose(grupo_a)
multiplicacion_transpuesta = grupo_a @ grupo_b
print("multiplicación transpuesta: ", multiplicacion_transpuesta.T)

# 4

angulos = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])

seno = np.sin(angulos)
print("Seno ", seno)

coseno = np.cos(angulos)
print("Coseno ", coseno)

tangente = np.tan(angulos)
print("Tangente ", tangente)

# 5

estadisticas = np.array([5.0, np.nan, 7.0, np.nan, 9.0])
print("Suma:", np.nansum(estadisticas))
print("Media (promedio):", np.nanmean(estadisticas))
print("Mediana:", np.nanmedian(estadisticas))
print("Desviación estándar:", np.nanstd(estadisticas))
print("Varianza:", np.nanvar(estadisticas))
print("Mínimo:", np.nanmin(estadisticas))
print("Máximo:", np.nanmax(estadisticas))
print("Índice del mínimo:", np.nanargmin(estadisticas))
print("Índice del máximo:", np.nanargmax(estadisticas))
