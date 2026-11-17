import numpy as np

from src.clasificador import (
    calcular_centroides,
    calcular_distancias,
    predecir
)


def comprobar_arrays(obtenido, esperado, mensaje):
    """Compara arrays permitiendo pequeñas diferencias decimales."""
    assert obtenido.shape == esperado.shape, (
        mensaje + ": las formas no coinciden."
    )

    assert np.max(np.abs(obtenido - esperado)) < 0.000001, mensaje


def probar_apartado5():
    """Comprueba los centroides, las distancias y las predicciones."""

    # Datos artificiales para probar el algoritmo directamente.
    # Representan coordenadas en el espacio de cuatro variables.
    # No son mediciones físicas ni se pasan por la limpieza.
    X_entrenamiento = np.array([
        [0.0, 0.0, 0.0, -1.0],
        [0.0, 0.0, 0.0,  1.0],

        [4.0, 0.0, 0.0, -1.0],
        [4.0, 0.0, 0.0,  1.0],

        [0.0, 6.0, 0.0, -1.0],
        [0.0, 6.0, 0.0,  1.0]
    ])

    y_entrenamiento = np.array([0, 0, 1, 1, 2, 2])

    entrenamiento_original = X_entrenamiento.copy()

    # APARTADO 5: Calcular el centroide de cada categoría utilizando
    # los datos de entrenamiento.
    centroides = calcular_centroides(
        X_entrenamiento,
        y_entrenamiento
    )

    centroides_esperados = {
        0: np.array([0.0, 0.0, 0.0, 0.0]),
        1: np.array([4.0, 0.0, 0.0, 0.0]),
        2: np.array([0.0, 6.0, 0.0, 0.0])
    }

    assert len(centroides) == 3, (
        "Debería calcularse un centroide para cada categoría."
    )

    for estado in [0, 1, 2]:
        assert estado in centroides, (
            f"Falta el centroide del estado {estado}."
        )

        comprobar_arrays(
            centroides[estado],
            centroides_esperados[estado],
            f"El centroide del estado {estado} es incorrecto."
        )

    comprobar_arrays(
        X_entrenamiento,
        entrenamiento_original,
        "El cálculo de centroides ha modificado el entrenamiento."
    )

    print("Correcto: cálculo de los tres centroides.")

    X_prueba = np.array([
        [0.0, 0.0, 0.0, 0.0],
        [4.0, 0.0, 0.0, 0.0],
        [0.0, 6.0, 0.0, 0.0],
        [1.0, 0.0, 0.0, 0.0],
        [3.0, 0.0, 0.0, 0.0],
        [0.0, 5.0, 0.0, 0.0],
        [0.0, 0.0, 3.0, 4.0]
    ])

    prueba_original = X_prueba.copy()

    # APARTADO 5: Para cada observación del conjunto de prueba,
    # calcular su distancia euclídea respecto a los tres centroides.
    # Usamos los centroides esperados para probar esta función
    # independientemente del cálculo anterior.
    distancias, estados = calcular_distancias(
        X_prueba,
        centroides_esperados
    )

    distancias_esperadas = np.array([
        [0.0, 4.0,       6.0],
        [4.0, 0.0,       52 ** 0.5],
        [6.0, 52 ** 0.5, 0.0],
        [1.0, 3.0,       37 ** 0.5],
        [3.0, 1.0,       45 ** 0.5],
        [5.0, 41 ** 0.5, 1.0],
        [5.0, 41 ** 0.5, 61 ** 0.5]
    ])

    assert list(estados) == [0, 1, 2], (
        "Las columnas de distancias deberían corresponder a 0, 1 y 2."
    )

    comprobar_arrays(
        distancias,
        distancias_esperadas,
        "Las distancias euclídeas son incorrectas."
    )

    print("Correcto: distancias de las siete observaciones.")

    # APARTADO 5: Asignar a la observación la categoría cuyo centroide
    # se encuentre a menor distancia.
    y_predicho, distancias_prediccion = predecir(
        X_prueba,
        centroides
    )

    predicciones_esperadas = np.array([0, 1, 2, 0, 1, 2, 0])

    comprobar_arrays(
        y_predicho,
        predicciones_esperadas,
        "Las categorías asignadas no son las esperadas."
    )

    comprobar_arrays(
        distancias_prediccion,
        distancias_esperadas,
        "Las distancias devueltas por predecir son incorrectas."
    )

    print("Correcto: asignación de la categoría más cercana.")

    # APARTADO 5: Almacenar las predicciones obtenidas.
    assert y_predicho.shape == (7,), (
        "Debería almacenarse una predicción por observación."
    )

    assert y_predicho.dtype == np.array([0], dtype=int).dtype, (
        "Las predicciones deberían almacenarse como enteros."
    )

    comprobar_arrays(
        X_prueba,
        prueba_original,
        "La predicción ha modificado los datos de prueba."
    )

    print("Correcto: almacenamiento de las siete predicciones.")
    print("Correcto: conservación de los datos originales.")

    print("\nCentroides calculados:")

    for estado in [0, 1, 2]:
        print(f"- Estado {estado}: {centroides[estado]}")

    print("\nDistancias a los estados 0, 1 y 2:")
    print(distancias)

    print("\nPredicciones esperadas:")
    print(predicciones_esperadas)

    print("\nPredicciones obtenidas:")
    print(y_predicho)

    print("\nTodas las pruebas del apartado 5 han terminado correctamente.")


if __name__ == "__main__":
    probar_apartado5()