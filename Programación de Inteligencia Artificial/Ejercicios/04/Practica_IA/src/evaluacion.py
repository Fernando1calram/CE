import numpy as np


NOMBRES_ESTADOS = {
    0: "Funcionamiento normal",
    1: "Desgaste mecánico",
    2: "Sobrecalentamiento"
}


def matriz_confusion(y_real, y_predicho):
    """Construye la matriz de confusión de las tres categorías."""
    if len(y_real) == 0:
        raise ValueError("No hay observaciones para evaluar.")

    if len(y_real) != len(y_predicho):
        raise ValueError(
            "El número de etiquetas reales y predicciones no coincide."
        )

    clases = [0, 1, 2]
    matriz = np.zeros((3, 3), dtype=int)

    # APARTADO 6: Matriz de confusión.
    # Las filas representan el estado real y las columnas el predicho.
    for indice_real in range(len(clases)):
        for indice_predicho in range(len(clases)):
            matriz[indice_real, indice_predicho] = np.sum(
                (y_real == clases[indice_real])
                & (y_predicho == clases[indice_predicho])
            )

    return matriz, clases


def calcular_metricas(y_real, y_predicho):
    """Calcula las métricas utilizando la matriz de confusión."""
    matriz, clases = matriz_confusion(y_real, y_predicho)
    metricas = {}

    # APARTADO 6: Accuracy.
    accuracy = np.mean(y_real == y_predicho)

    for indice in range(len(clases)):
        clase = clases[indice]

        verdaderos_positivos = matriz[indice, indice]
        falsos_positivos = (
            np.sum(matriz[:, indice]) - verdaderos_positivos
        )
        falsos_negativos = (
            np.sum(matriz[indice, :]) - verdaderos_positivos
        )

        # APARTADO 6: Precision por categoría.
        if verdaderos_positivos + falsos_positivos > 0:
            precision = (
                verdaderos_positivos
                / (verdaderos_positivos + falsos_positivos)
            )
        else:
            precision = 0.0

        # APARTADO 6: Recall por categoría.
        if verdaderos_positivos + falsos_negativos > 0:
            recall = (
                verdaderos_positivos
                / (verdaderos_positivos + falsos_negativos)
            )
        else:
            recall = 0.0

        # APARTADO 6: F1-score por categoría.
        if precision + recall > 0:
            f1 = 2 * precision * recall / (precision + recall)
        else:
            f1 = 0.0

        metricas[clase] = {
            "precision": precision,
            "recall": recall,
            "f1": f1
        }

    return accuracy, matriz, clases, metricas


def mostrar_evaluacion(y_real, y_predicho):
    """Muestra la matriz de confusión y las métricas calculadas."""
    accuracy, matriz, clases, metricas = calcular_metricas(
        y_real,
        y_predicho
    )

    print("\n=== APARTADO 6: EVALUACIÓN ===")

    print("\nMatriz de confusión:")
    print("Filas = estado real; columnas = estado predicho.")
    print("Orden de los estados:", clases)
    print(matriz)

    print(f"\nAccuracy: {accuracy:.4f} ({accuracy * 100:.2f} %)")

    print("\nMétricas por categoría:")

    for clase in clases:
        valores = metricas[clase]

        print(f"\nEstado {clase}: {NOMBRES_ESTADOS[clase]}")
        print(f"  Precision: {valores['precision']:.4f}")
        print(f"  Recall: {valores['recall']:.4f}")
        print(f"  F1-score: {valores['f1']:.4f}")

    return accuracy, matriz, clases, metricas


def analizar_resultados(matriz, clases, metricas):
    """Interpreta los resultados obtenidos en el conjunto de prueba."""
    print("\nAnálisis de los resultados:")

    valores_f1 = np.array(
        [metricas[clase]["f1"] for clase in clases]
    )
    valores_recall = np.array(
        [metricas[clase]["recall"] for clase in clases]
    )

    mejor_f1 = np.max(valores_f1)
    peor_recall = np.min(valores_recall)

    print("\nCategorías con mejor F1-score:")

    for clase in clases:
        if metricas[clase]["f1"] == mejor_f1:
            print(
                f"- Estado {clase}: {NOMBRES_ESTADOS[clase]}, "
                f"F1 = {mejor_f1:.4f}"
            )

    # Quitamos la diagonal para buscar únicamente errores.
    errores = matriz.copy()

    for indice in range(len(clases)):
        errores[indice, indice] = 0

    mayor_confusion = np.max(errores)

    print("\nConfusiones más frecuentes:")

    if mayor_confusion == 0:
        print("No se han producido errores en el conjunto de prueba.")
    else:
        for indice_real in range(len(clases)):
            for indice_predicho in range(len(clases)):
                if errores[indice_real, indice_predicho] == mayor_confusion:
                    print(
                        f"- Estado real {clases[indice_real]} clasificado "
                        f"como {clases[indice_predicho]}: "
                        f"{mayor_confusion} registros."
                    )

    print("\nCategorías con menor recall:")

    for clase in clases:
        if metricas[clase]["recall"] == peor_recall:
            print(
                f"- Estado {clase}: {NOMBRES_ESTADOS[clase]}, "
                f"recall = {peor_recall:.4f}"
            )

    print(
        "\nUn recall menor indica que quedan más casos de esa categoría "
        "sin identificar correctamente. Si hay empate, se muestran "
        "todas las categorías empatadas."
    )

    print(
        "\nEl resultado de una única partición de prueba no basta para "
        "considerar el sistema adecuado para un entorno industrial real. "
        "Los errores deben revisarse teniendo en cuenta sus consecuencias, "
        "especialmente cuando una incidencia se clasifica como normal."
    )