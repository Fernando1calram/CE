import numpy as np
from carga import COLUMNAS_NUMERICAS, RANGOS_VALIDOS

def calcular_medianas(x):
    # Calcula la mediana de cada columna, usamos nanmedian para que ignore los valores NaN
    return np.nanmedian(x, axis=0)

def identifica_ausentes(x):
    # Identifica valores ausentes
    return np.isnan(x)

def imputar_ausentes(x):
    x_imputado = x.copy()
    medianas = calcular_medianas(x)

    mascaras_ausentes = np.isnan(x_imputado)

    # Sustitución de cada nan por la mediana de su columna
    for indice_columna in range(x.shape[1]):
        mascaras_columna = mascaras_ausentes[:,indice_columna]
        x_imputado[mascaras_columna, indice_columna] = medianas[indice_columna]

    return x_imputado, medianas

def detectar_fuera_rango(x):
    fuera_rango = np.zeros_like(x, dtype=bool)

    for indice, columna in enumerate(COLUMNAS_NUMERICAS):
        valor_minimo, valor_maximo = RANGOS_VALIDOS[columna]
        fuera_rango[:, indice] = ((x[:, indice] < valor_minimo) | (x[:,indice] > valor_maximo))
        return fuera_rango
