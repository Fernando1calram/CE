import numpy as np

from src.evaluacion import (
    matriz_confusion,
    calcular_metricas,
    mostrar_evaluacion,
    analizar_resultados
)


def comprobar_numero(obtenido, esperado, mensaje):
    """Compara dos resultados admitiendo pequeñas diferencias decimales."""
    assert abs(obtenido - esperado) < 0.000001, (
        f"{mensaje}: obtenido={obtenido}, esperado={esperado}"
    )


def probar_evaluacion_con_errores():
    """Comprueba todas las métricas con aciertos y errores conocidos."""
    y_real = np.array([0, 0, 0, 1, 1, 2, 2, 2, 2])
    y_predicho = np.array([0, 0, 1, 1, 2, 0, 1, 2, 2])

    # APARTADO 6: Matriz de confusión.
    matriz, clases = matriz_confusion(y_real, y_predicho)

    matriz_esperada = np.array([
        [2, 1, 0],
        [0, 1, 1],
        [1, 1, 2]
    ])

    assert list(clases) == [0, 1, 2], (
        "El orden de las categorías debería ser 0, 1 y 2."
    )

    assert matriz.shape == (3, 3), (
        "La matriz de confusión debería tener tres filas y tres columnas."
    )

    assert np.sum(matriz != matriz_esperada) == 0, (
        "La matriz de confusión no coincide con la esperada."
    )

    assert np.sum(matriz) == 9, (
        "La matriz debería contabilizar los nueve registros."
    )

    print("Correcto: matriz de confusión.")

    accuracy, matriz_metricas, clases, metricas = calcular_metricas(
        y_real,
        y_predicho
    )

    assert np.sum(matriz_metricas != matriz_esperada) == 0, (
        "La matriz utilizada para calcular las métricas es incorrecta."
    )

    # APARTADO 6: Accuracy.
    comprobar_numero(
        accuracy,
        5 / 9,
        "La accuracy debería ser 5/9"
    )

    print("Correcto: accuracy.")

    # Los resultados esperados se han calculado previamente.
    esperados = {
        0: {
            "precision": 2 / 3,
            "recall": 2 / 3,
            "f1": 2 / 3
        },
        1: {
            "precision": 1 / 3,
            "recall": 1 / 2,
            "f1": 2 / 5
        },
        2: {
            "precision": 2 / 3,
            "recall": 1 / 2,
            "f1": 4 / 7
        }
    }

    # APARTADO 6: Precision por categoría.
    for clase in [0, 1, 2]:
        comprobar_numero(
            metricas[clase]["precision"],
            esperados[clase]["precision"],
            f"Precision incorrecta para el estado {clase}"
        )

    print("Correcto: precision de las tres categorías.")

    # APARTADO 6: Recall por categoría.
    for clase in [0, 1, 2]:
        comprobar_numero(
            metricas[clase]["recall"],
            esperados[clase]["recall"],
            f"Recall incorrecto para el estado {clase}"
        )

    print("Correcto: recall de las tres categorías.")

    # APARTADO 6: F1-score por categoría.
    for clase in [0, 1, 2]:
        comprobar_numero(
            metricas[clase]["f1"],
            esperados[clase]["f1"],
            f"F1 incorrecto para el estado {clase}"
        )

    print("Correcto: F1-score de las tres categorías.")

    # Mostramos la evaluación para comprobar también su presentación.
    mostrar_evaluacion(y_real, y_predicho)
    analizar_resultados(matriz, clases, metricas)


def probar_predicciones_perfectas():
    """Comprueba que todas las métricas valen uno si no hay errores."""
    y_real = np.array([0, 0, 1, 1, 2, 2])
    y_predicho = y_real.copy()

    accuracy, matriz, clases, metricas = calcular_metricas(
        y_real,
        y_predicho
    )

    comprobar_numero(accuracy, 1.0, "La accuracy debería ser uno")

    matriz_esperada = np.array([
        [2, 0, 0],
        [0, 2, 0],
        [0, 0, 2]
    ])

    assert np.sum(matriz != matriz_esperada) == 0, (
        "Con predicciones perfectas solo debería haber valores en la diagonal."
    )

    for clase in clases:
        for nombre in ["precision", "recall", "f1"]:
            comprobar_numero(
                metricas[clase][nombre],
                1.0,
                f"{nombre} debería valer uno para el estado {clase}"
            )

    print("\nCorrecto: caso de predicciones perfectas.")


def probar_categoria_sin_predicciones():
    """Comprueba el control de denominadores cero."""
    y_real = np.array([0, 1, 2])

    # El clasificador predice siempre el estado 0.
    y_predicho = np.array([0, 0, 0])

    accuracy, matriz, clases, metricas = calcular_metricas(
        y_real,
        y_predicho
    )

    comprobar_numero(accuracy, 1 / 3, "La accuracy debería ser 1/3")

    comprobar_numero(
        metricas[0]["precision"],
        1 / 3,
        "Precision incorrecta para el estado 0"
    )

    comprobar_numero(
        metricas[0]["recall"],
        1.0,
        "Recall incorrecto para el estado 0"
    )

    comprobar_numero(
        metricas[0]["f1"],
        0.5,
        "F1 incorrecto para el estado 0"
    )

    # Para los estados 1 y 2 no hay predicciones.
    # Nuestra implementación asigna cero cuando el denominador es cero.
    for clase in [1, 2]:
        for nombre in ["precision", "recall", "f1"]:
            comprobar_numero(
                metricas[clase][nombre],
                0.0,
                f"{nombre} debería valer cero para el estado {clase}"
            )

    print("Correcto: categorías sin predicciones y control de división por cero.")


def probar_entradas_incorrectas():
    """Comprueba el rechazo de datos vacíos o de longitudes distintas."""
    casos = [
        (np.array([]), np.array([])),
        (np.array([0, 1]), np.array([0]))
    ]

    for y_real, y_predicho in casos:
        error_detectado = False

        try:
            calcular_metricas(y_real, y_predicho)
        except ValueError:
            error_detectado = True

        assert error_detectado, (
            "La entrada incorrecta debería provocar un ValueError."
        )

    print("Correcto: control de entradas vacías y longitudes distintas.")


def main():
    print("=== PRUEBAS CONTROLADAS DEL APARTADO 6 ===\n")

    probar_evaluacion_con_errores()
    probar_predicciones_perfectas()
    probar_categoria_sin_predicciones()
    probar_entradas_incorrectas()

    print("\nTodas las pruebas del apartado 6 han terminado correctamente.")


if __name__ == "__main__":
    main()