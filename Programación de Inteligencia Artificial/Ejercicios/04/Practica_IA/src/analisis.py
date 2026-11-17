import numpy as np

from src.carga import COLUMNAS_NUMERICAS
from src.limpieza import calcular_cuartil


def calcular_estadisticas(valores):
    """Calcula las estadísticas solicitadas para una variable."""
    if len(valores) == 0:
        raise ValueError("No hay valores para realizar el análisis.")

    estadisticas = {}

    # APARTADO 3: Media.
    estadisticas["media"] = np.mean(valores)

    # APARTADO 3: Mediana.
    estadisticas["mediana"] = np.median(valores)

    # APARTADO 3: Desviación estándar.
    estadisticas["desviacion_estandar"] = np.std(valores)

    # APARTADO 3: Valor mínimo y máximo.
    estadisticas["minimo"] = np.min(valores)
    estadisticas["maximo"] = np.max(valores)

    # APARTADO 3: Primer y tercer cuartil.
    estadisticas["q1"] = calcular_cuartil(valores, 0.25)
    estadisticas["q3"] = calcular_cuartil(valores, 0.75)

    # APARTADO 3: Rango intercuartílico.
    estadisticas["iqr"] = (
        estadisticas["q3"] - estadisticas["q1"]
    )

    return estadisticas


def analisis_global(X):
    """Calcula las estadísticas de las cuatro variables predictoras."""
    resultados = {}

    for indice in range(len(COLUMNAS_NUMERICAS)):
        columna = COLUMNAS_NUMERICAS[indice]
        resultados[columna] = calcular_estadisticas(X[:, indice])

    return resultados


def analisis_por_estado(X, y):
    """Calcula las mismas estadísticas separando los datos por estado."""
    resultados = {}

    for estado in np.unique(y):
        mascara = y == estado
        resultados[estado] = analisis_global(X[mascara])

    return resultados


def mostrar_analisis(resultados, titulo):
    """Muestra un diccionario de estadísticas organizado por variable."""
    print("\n" + titulo)
    print("-" * len(titulo))

    for variable in resultados:
        print("\n" + variable + ":")

        for nombre, valor in resultados[variable].items():
            print(f"  {nombre}: {valor:.3f}")