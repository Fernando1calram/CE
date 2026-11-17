import numpy as np

from src.analisis import (
    calcular_estadisticas,
    analisis_global,
    analisis_por_estado,
    mostrar_analisis
)


def comprobar_resultados(obtenidos, esperados):
    """Compara cada estadística con su resultado esperado."""
    for nombre in esperados:
        diferencia = abs(obtenidos[nombre] - esperados[nombre])

        # Permitimos una pequeña diferencia por los cálculos decimales.
        assert diferencia < 0.000001, (
            f"Error en {nombre}: "
            f"obtenido={obtenidos[nombre]}, "
            f"esperado={esperados[nombre]}"
        )


def probar_estadisticas_variable():
    """Comprueba las estadísticas de una variable."""
    # Los valores están desordenados intencionadamente.
    valores = np.array([50.0, 10.0, 40.0, 20.0, 30.0])

    resultados = calcular_estadisticas(valores)

    # APARTADO 3: Media.
    assert resultados["media"] == 30.0, (
        "La media debería ser 30."
    )

    # APARTADO 3: Mediana.
    assert resultados["mediana"] == 30.0, (
        "La mediana debería ser 30."
    )

    # APARTADO 3: Desviación estándar.
    # Media = 30.
    # Suma de desviaciones al cuadrado = 400 + 400 + 100 + 100 + 0.
    # Varianza = 1000 / 5 = 200.
    desviacion_esperada = 200 ** 0.5

    assert abs(
        resultados["desviacion_estandar"] - desviacion_esperada
    ) < 0.000001, (
        "La desviación estándar debería ser aproximadamente 14.142136."
    )

    # APARTADO 3: Valor mínimo y máximo.
    assert resultados["minimo"] == 10.0, (
        "El mínimo debería ser 10."
    )

    assert resultados["maximo"] == 50.0, (
        "El máximo debería ser 50."
    )

    # APARTADO 3: Primer y tercer cuartil.
    assert resultados["q1"] == 20.0, (
        "El primer cuartil debería ser 20."
    )

    assert resultados["q3"] == 40.0, (
        "El tercer cuartil debería ser 40."
    )

    # APARTADO 3: Rango intercuartílico.
    assert resultados["iqr"] == 20.0, (
        "El rango intercuartílico debería ser 20."
    )

    # Comprobamos que no se modifica el orden del array original.
    assert list(valores) == [50.0, 10.0, 40.0, 20.0, 30.0], (
        "El análisis no debería modificar los datos originales."
    )

    print("Correcto: las seis estadísticas de una variable.")


def probar_analisis_global_y_por_estado():
    """Comprueba el análisis de las cuatro variables y las tres clases."""
    # Columnas: temperatura, vibracion, consumo y presion.
    X = np.array([
        [10.0, 1.0,  2.0,  3.0],
        [20.0, 2.0,  4.0,  6.0],
        [30.0, 3.0,  6.0,  9.0],
        [40.0, 4.0,  8.0, 12.0],
        [50.0, 5.0, 10.0, 15.0],
        [60.0, 6.0, 12.0, 18.0]
    ])

    y = np.array([0, 0, 1, 1, 2, 2])

    # Estos datos prueban el análisis estadístico de forma aislada.
    # No se pasan por la limpieza ni representan un CSV industrial real.
    globales = analisis_global(X)

    # Resultados calculados previamente, sin utilizar las funciones
    # estadísticas que estamos comprobando.
    esperados_globales = {
        "temperatura": {
            "media": 35.0,
            "mediana": 35.0,
            "desviacion_estandar": (1750 / 6) ** 0.5,
            "minimo": 10.0,
            "maximo": 60.0,
            "q1": 22.5,
            "q3": 47.5,
            "iqr": 25.0
        },
        "vibracion": {
            "media": 3.5,
            "mediana": 3.5,
            "desviacion_estandar": (17.5 / 6) ** 0.5,
            "minimo": 1.0,
            "maximo": 6.0,
            "q1": 2.25,
            "q3": 4.75,
            "iqr": 2.5
        },
        "consumo": {
            "media": 7.0,
            "mediana": 7.0,
            "desviacion_estandar": (70 / 6) ** 0.5,
            "minimo": 2.0,
            "maximo": 12.0,
            "q1": 4.5,
            "q3": 9.5,
            "iqr": 5.0
        },
        "presion": {
            "media": 10.5,
            "mediana": 10.5,
            "desviacion_estandar": (157.5 / 6) ** 0.5,
            "minimo": 3.0,
            "maximo": 18.0,
            "q1": 6.75,
            "q3": 14.25,
            "iqr": 7.5
        }
    }

    assert len(globales) == 4, (
        "El análisis global debería incluir cuatro variables."
    )

    for variable in esperados_globales:
        assert variable in globales, (
            f"Falta la variable {variable}."
        )

        comprobar_resultados(
            globales[variable],
            esperados_globales[variable]
        )

    print("Correcto: análisis global de las cuatro variables.")

    por_estado = analisis_por_estado(X, y)

    assert len(por_estado) == 3, (
        "El análisis por estado debería incluir tres categorías."
    )

    # Cada fila de esta lista contiene los resultados de temperatura
    # de una categoría, calculados a partir de dos observaciones.
    temperaturas_por_estado = [
        [10.0, 20.0],
        [30.0, 40.0],
        [50.0, 60.0]
    ]

    # Las otras columnas son múltiplos de la temperatura.
    factores = {
        "temperatura": 1.0,
        "vibracion": 0.1,
        "consumo": 0.2,
        "presion": 0.3
    }

    for estado in [0, 1, 2]:
        assert estado in por_estado, (
            f"Falta el estado {estado}."
        )

        assert len(por_estado[estado]) == 4, (
            f"El estado {estado} debería incluir cuatro variables."
        )

        menor = temperaturas_por_estado[estado][0]
        mayor = temperaturas_por_estado[estado][1]

        for variable, factor in factores.items():
            esperados = {
                "media": ((menor + mayor) / 2) * factor,
                "mediana": ((menor + mayor) / 2) * factor,
                "desviacion_estandar": 5.0 * factor,
                "minimo": menor * factor,
                "maximo": mayor * factor,
                "q1": (menor + 2.5) * factor,
                "q3": (menor + 7.5) * factor,
                "iqr": 5.0 * factor
            }

            comprobar_resultados(
                por_estado[estado][variable],
                esperados
            )

    print("Correcto: estadísticas por categoría y por variable.")

    # Comprobación visual de la presentación de resultados.
    mostrar_analisis(globales, "Estadísticas globales de prueba")

    for estado in por_estado:
        mostrar_analisis(
            por_estado[estado],
            f"Estadísticas de prueba del estado {estado}"
        )


def probar_casos_especiales():
    """Comprueba una variable constante y un conjunto de un solo valor."""
    for valores in [
        np.array([25.0, 25.0, 25.0, 25.0]),
        np.array([25.0])
    ]:
        resultados = calcular_estadisticas(valores)

        esperados = {
            "media": 25.0,
            "mediana": 25.0,
            "desviacion_estandar": 0.0,
            "minimo": 25.0,
            "maximo": 25.0,
            "q1": 25.0,
            "q3": 25.0,
            "iqr": 0.0
        }

        comprobar_resultados(resultados, esperados)

    print("Correcto: variable constante y conjunto de un solo valor.")

    # La función debe rechazar una variable sin observaciones.
    error_detectado = False

    try:
        calcular_estadisticas(np.array([]))
    except ValueError:
        error_detectado = True

    assert error_detectado, (
        "Un array vacío debería provocar un ValueError."
    )

    print("Correcto: control de datos vacíos.")


def main():
    print("=== PRUEBAS DEL APARTADO 3 ===\n")

    probar_estadisticas_variable()
    probar_analisis_global_y_por_estado()
    probar_casos_especiales()

    print("\nTodas las pruebas del apartado 3 han terminado correctamente.")


if __name__ == "__main__":
    main()