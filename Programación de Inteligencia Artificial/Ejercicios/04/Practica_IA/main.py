import os

from src.carga import cargar_datos, explorar_datos

from src.limpieza import (
    limpiar_datos,
    mostrar_informe_limpieza
)

from src.analisis import (
    analisis_global,
    analisis_por_estado,
    mostrar_analisis
)

from src.clasificador import (
    dividir_estratificado,
    normalizar,
    calcular_centroides,
    predecir
)

from src.evaluacion import (
    mostrar_evaluacion,
    analizar_resultados
)

from src.graficos import (
    crear_carpeta_graficos,
    grafico_distribucion_estados,
    grafico_metricas_por_estado,
    grafico_matriz_confusion
)


RUTA_DATOS = "datos/sensores.csv"


def mostrar_conclusiones(accuracy, informe):
    """Muestra una base de conclusiones para elaborar la memoria."""
    print("\n=== APARTADO 7: ANÁLISIS Y CONCLUSIONES ===")

    print(
        "\nSe han cargado los datos, identificado los problemas "
        "de calidad y calculado las estadísticas globales y por estado."
    )

    print(
        "\nRegistros conservados después de la limpieza:",
        informe["registros_conservados"]
    )

    print(
        "\nLos valores ausentes y fuera del rango físico se han "
        "corregido con la mediana de su variable. Los registros con "
        "dos o más variables problemáticas se han descartado."
    )

    print(
        "\nLos atípicos estadísticos se han conservado porque "
        "pueden corresponder a situaciones reales de funcionamiento anómalo."
    )

    print(
        "\nEl clasificador representa cada categoría mediante el promedio "
        "de sus observaciones de entrenamiento normalizadas y asigna cada "
        "registro de prueba al centroide más cercano."
    )

    print(f"\nAccuracy obtenida: {accuracy:.4f}")

    print(
        "\nLimitaciones:"
        "\n- Cada categoría se representa mediante un único centroide."
        "\n- La imputación introduce valores estimados."
        "\n- El descarte reduce el número de observaciones."
        "\n- La evaluación utiliza una única división de los datos."
        "\n- Las medianas de esta versión se calculan antes de dividir "
        "el conjunto en entrenamiento y prueba."
    )

    print(
        "\nPosibles mejoras:"
        "\n- Incorporar nuevas mediciones reales."
        "\n- Revisar los registros corregidos con información de los sensores."
        "\n- Comprobar la estabilidad de los resultados con otras particiones."
        "\n- Calcular las medianas exclusivamente con entrenamiento "
        "y aplicar esos mismos valores a prueba."
        "\n- Analizar las consecuencias de cada tipo de error."
    )


def main():
    print("=== PRÁCTICA SENSORES - FERNANDO CALLES RAMOS ===")

    # Cargamos y exploramos los datos originales.
    ids, X, y = cargar_datos(RUTA_DATOS)
    explorar_datos(ids, X, y)

    # Aplicamos el procedimiento de limpieza.
    X_limpio, mascara_valida, informe = limpiar_datos(X)
    mostrar_informe_limpieza(ids, informe)

    # Mantenemos alineados los datos, las etiquetas y los identificadores.
    y_limpio = y[mascara_valida]
    ids_limpios = ids[mascara_valida]

    print("\nDimensiones después de la limpieza:")
    print("Variables predictoras:", X_limpio.shape)
    print("Variable objetivo:", y_limpio.shape)
    print("Identificadores:", ids_limpios.shape)

    print("\n=== APARTADO 3: ANÁLISIS ESTADÍSTICO ===")

    resultados_globales = analisis_global(X_limpio)
    mostrar_analisis(resultados_globales, "Estadísticas globales")

    # Mostramos cada categoría por separado para respetar
    # la estructura del diccionario de resultados.
    resultados_por_estado = analisis_por_estado(X_limpio, y_limpio)

    for estado in resultados_por_estado:
        mostrar_analisis(
            resultados_por_estado[estado],
            f"Estadísticas del estado {estado}"
        )

    print("\n=== APARTADO 4: TRANSFORMACIÓN Y NORMALIZACIÓN ===")

    (
        X_entrenamiento,
        X_prueba,
        y_entrenamiento,
        y_prueba
    ) = dividir_estratificado(X_limpio, y_limpio)

    (
        X_entrenamiento_normalizado,
        X_prueba_normalizado,
        media,
        desviacion
    ) = normalizar(X_entrenamiento, X_prueba)

    print("\nDimensiones de entrenamiento:", X_entrenamiento.shape)
    print("Dimensiones de prueba:", X_prueba.shape)

    # Mostramos los recuentos para comprobar la distribución por clase.
    print("\nDistribución por categoría:")

    for estado in [0, 1, 2]:
        cantidad_entrenamiento = sum(y_entrenamiento == estado)
        cantidad_prueba = sum(y_prueba == estado)

        print(
            f"- Estado {estado}: "
            f"{cantidad_entrenamiento} en entrenamiento y "
            f"{cantidad_prueba} en prueba."
        )

    print("\nMedia de entrenamiento utilizada para normalizar:")
    print(media)

    print("\nDesviación estándar de entrenamiento:")
    print(desviacion)

    print("\n=== APARTADO 5: CLASIFICACIÓN ===")

    centroides = calcular_centroides(
        X_entrenamiento_normalizado,
        y_entrenamiento
    )

    print("\nCentroides normalizados:")

    for estado in centroides:
        print(f"- Estado {estado}: {centroides[estado]}")

    y_predicho, distancias = predecir(
        X_prueba_normalizado,
        centroides
    )

    print("\nPrimeros diez estados reales:")
    print(y_prueba[:10])

    print("\nPrimeras diez predicciones:")
    print(y_predicho[:10])

    print("\nDistancias a los tres centroides de esos registros:")
    print(distancias[:10])

    accuracy, matriz, clases, metricas = mostrar_evaluacion(
        y_prueba,
        y_predicho
    )

    analizar_resultados(matriz, clases, metricas)

    # APARTADO 7: Generación de gráficos
    ruta_graficos = os.path.join("resultados", "graficos")
    crear_carpeta_graficos(ruta_graficos)

    grafico_distribucion_estados(
        y_limpio,
        os.path.join(ruta_graficos, "distribucion_estados.png")
    )

    grafico_matriz_confusion(
        matriz,
        os.path.join(ruta_graficos, "matriz_confusion.png")
    )

    precisiones = [
        metricas[0]["precision"],
        metricas[1]["precision"],
        metricas[2]["precision"]
    ]

    recalls = [
        metricas[0]["recall"],
        metricas[1]["recall"],
        metricas[2]["recall"]
    ]

    f1_scores = [
        metricas[0]["f1"],
        metricas[1]["f1"],
        metricas[2]["f1"]
    ]

    grafico_metricas_por_estado(
        matriz,
        precisiones,
        recalls,
        f1_scores,
        os.path.join(ruta_graficos, "metricas_por_estado.png")
    )

    print("\nGráficos generados en:", ruta_graficos)

if __name__ == "__main__":
    try:
        main()
    except (FileNotFoundError, ValueError) as error:
        print("\nNo se ha podido completar la ejecución:")
        print(error)