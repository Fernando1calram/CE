import numpy as np

from src.carga import (
    cargar_datos,
    explorar_datos,
    COLUMNAS,
    COLUMNAS_NUMERICAS
)


def probar_apartado1():
    """Comprueba el apartado 1 con un CSV de resultados conocidos."""
    ids, X, y = cargar_datos("datos/sensores_prueba.csv")

    # Mostramos la salida que también debe revisarse visualmente.
    explorar_datos(ids, X, y)

    print("\n=== COMPROBACIONES AUTOMÁTICAS ===")

    # APARTADO 1: Obtener las dimensiones del conjunto de datos.
    assert X.shape == (6, 4), "X debería tener 6 filas y 4 columnas."
    assert y.shape == (6,), "y debería contener 6 estados."
    assert ids.shape == (6,), "ids debería contener 6 identificadores."

    print("Correcto: dimensiones del conjunto de datos.")

    # APARTADO 1: Identificar las variables disponibles.
    columnas_esperadas = [
        "id",
        "temperatura",
        "vibracion",
        "consumo",
        "presion",
        "estado"
    ]

    predictoras_esperadas = [
        "temperatura",
        "vibracion",
        "consumo",
        "presion"
    ]

    assert COLUMNAS == columnas_esperadas, (
        "Los nombres o el orden de las columnas no son los esperados."
    )

    assert COLUMNAS_NUMERICAS == predictoras_esperadas, (
        "Las variables predictoras no son las esperadas."
    )

    print("Correcto: nombres de las variables.")

    # APARTADO 1: Mostrar una muestra de los registros.
    # Comprobamos los datos que debe contener la primera fila.
    assert ids[0] == "P001", "El primer identificador debería ser P001."
    assert X[0, 0] == 70.0, "La primera temperatura debería ser 70.0."
    assert X[0, 1] == 1.0, "La primera vibración debería ser 1.0."
    assert X[0, 2] == 20.0, "El primer consumo debería ser 20.0."
    assert X[0, 3] == 6.0, "La primera presión debería ser 6.0."
    assert y[0] == 0, "El primer estado debería ser 0."

    # También verificamos que el último registro se ha cargado.
    assert ids[-1] == "P006", "El último identificador debería ser P006."
    assert y[-1] == 2, "El último estado debería ser 2."

    print("Correcto: contenido de los registros comprobados.")
    print("Revisa visualmente que la muestra muestra P001 hasta P005.")

    # APARTADO 1: Comprobar los tipos de datos.
    # Comparamos con arrays creados con los tipos esperados,
    # sin depender de que el entero sea int32 o int64.
    assert X.dtype == np.array([0.0], dtype=float).dtype, (
        "Las variables predictoras deberían ser de tipo float."
    )

    assert y.dtype == np.array([0], dtype=int).dtype, (
        "Los estados deberían ser de tipo entero."
    )

    assert ids.dtype == np.array(["P001"]).dtype, (
        "Los identificadores deberían ser cadenas de cuatro caracteres."
    )

    print("Correcto: tipos de datos.")

    # APARTADO 1: Identificar los valores ausentes.
    ausentes = np.isnan(X)

    assert np.sum(ausentes) == 4, (
        "Debería haber exactamente 4 valores ausentes."
    )

    for indice in range(4):
        assert np.sum(ausentes[:, indice]) == 1, (
            f"Debería haber un ausente en {COLUMNAS_NUMERICAS[indice]}."
        )

    # Verificamos las posiciones concretas de los campos vacíos.
    assert np.isnan(X[3, 0]), "Falta el NaN de temperatura en P004."
    assert np.isnan(X[4, 1]), "Falta el NaN de vibración en P005."
    assert np.isnan(X[4, 3]), "Falta el NaN de presión en P005."
    assert np.isnan(X[5, 2]), "Falta el NaN de consumo en P006."

    print("Correcto: cantidad y posición de los valores ausentes.")

    # APARTADO 1: Calcular el número de registros correspondientes
    # a cada categoría.
    categorias, recuentos = np.unique(y, return_counts=True)

    assert len(categorias) == 3, "Debería haber tres categorías."

    for indice in range(3):
        assert categorias[indice] == indice, (
            "Las categorías deberían ser 0, 1 y 2."
        )

        assert recuentos[indice] == 2, (
            f"Debería haber dos registros del estado {indice}."
        )

    assert np.sum(recuentos) == X.shape[0], (
        "La suma de los recuentos debería coincidir con el total de filas."
    )

    print("Correcto: recuentos por categoría.")

    print("\nTodas las comprobaciones automáticas han terminado correctamente.")


if __name__ == "__main__":
    probar_apartado1()