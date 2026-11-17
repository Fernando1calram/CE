import numpy as np

from src.carga import COLUMNAS_NUMERICAS, RANGOS_VALIDOS


def identificar_ausentes(X):
    """Devuelve una máscara con las posiciones que contienen NaN."""
    return np.isnan(X)


def detectar_fuera_rango(X):
    """Detecta valores fuera de los límites físicos del enunciado."""
    fuera_rango = np.zeros(X.shape, dtype=bool)

    for indice in range(len(COLUMNAS_NUMERICAS)):
        columna = COLUMNAS_NUMERICAS[indice]
        minimo, maximo = RANGOS_VALIDOS[columna]

        fuera_rango[:, indice] = (
            (X[:, indice] < minimo)
            | (X[:, indice] > maximo)
        )

    return fuera_rango


def calcular_medianas(X):
    """Calcula las medianas de las columnas ignorando los NaN."""
    medianas = []

    for indice in range(X.shape[1]):
        valores_validos = X[:, indice][~np.isnan(X[:, indice])]

        if len(valores_validos) == 0:
            raise ValueError(
                "No hay valores válidos para calcular la mediana de "
                + COLUMNAS_NUMERICAS[indice]
            )

        medianas.append(np.median(valores_validos))

    return np.array(medianas)


def imputar_valores(X, medianas):
    """Sustituye los NaN utilizando las medianas recibidas."""
    X_imputado = X.copy()

    for indice in range(X.shape[1]):
        mascara = np.isnan(X_imputado[:, indice])
        X_imputado[mascara, indice] = medianas[indice]

    return X_imputado


def calcular_cuartil(valores, proporcion):
    """
    Calcula un cuartil ordenando los datos y utilizando interpolación
    cuando la posición queda entre dos elementos.
    """
    valores_ordenados = list(valores)
    valores_ordenados.sort()

    if len(valores_ordenados) == 0:
        raise ValueError("No se puede calcular un cuartil sin datos.")

    posicion = proporcion * (len(valores_ordenados) - 1)
    indice_inferior = int(posicion)
    indice_superior = indice_inferior + 1

    if indice_superior >= len(valores_ordenados):
        return valores_ordenados[indice_inferior]

    parte_decimal = posicion - indice_inferior

    return (
        valores_ordenados[indice_inferior]
        + parte_decimal
        * (
            valores_ordenados[indice_superior]
            - valores_ordenados[indice_inferior]
        )
    )


def detectar_atipicos_iqr(X):
    """
    Detecta atípicos mediante los límites Q1 - 1.5 * IQR
    y Q3 + 1.5 * IQR.
    """
    atipicos = np.zeros(X.shape, dtype=bool)

    for indice in range(X.shape[1]):
        valores = X[:, indice]

        q1 = calcular_cuartil(valores, 0.25)
        q3 = calcular_cuartil(valores, 0.75)
        iqr = q3 - q1

        limite_inferior = q1 - 1.5 * iqr
        limite_superior = q3 + 1.5 * iqr

        atipicos[:, indice] = (
            (valores < limite_inferior)
            | (valores > limite_superior)
        )

    return atipicos


def limpiar_datos(X):
    """
    Detecta problemas, descarta registros poco fiables y corrige
    los valores ausentes o incorrectos de los registros conservados.

    Devuelve los datos limpios, la máscara de filas conservadas
    y un informe del proceso.
    """
    if X.shape[0] == 0:
        raise ValueError("No hay registros disponibles para limpiar.")

    # APARTADO 2: Identificar los registros que contienen valores ausentes
    # y establecer un procedimiento para tratarlos.
    ausentes = identificar_ausentes(X)
    registros_con_ausentes = np.sum(ausentes, axis=1) > 0

    # Los valores ausentes de los registros conservados se imputarán
    # con la mediana de su variable.

    # APARTADO 2: Detectar mediciones que se encuentren fuera de
    # los rangos físicos admisibles de los sensores.
    fuera_rango = detectar_fuera_rango(X)

    # APARTADO 2: Separar los registros válidos de aquellos que
    # deban descartarse o corregirse.
    problemas = ausentes | fuera_rango
    numero_problemas = np.sum(problemas, axis=1)

    # Es una decisión de diseño: descartamos filas con al menos
    # dos variables problemáticas y corregimos las que tienen una.
    registros_descartados = numero_problemas >= 2
    registros_a_corregir = numero_problemas == 1
    registros_sin_problemas = numero_problemas == 0

    mascara_valida = ~registros_descartados
    X_preparado = X[mascara_valida].copy()

    if X_preparado.shape[0] == 0:
        raise ValueError("No quedan registros después del descarte.")

    # Marcamos también los errores físicos como NaN para excluirlos
    # del cálculo de las medianas.
    fuera_rango_conservados = fuera_rango[mascara_valida]
    X_preparado[fuera_rango_conservados] = np.nan

    medianas = calcular_medianas(X_preparado)
    X_limpio = imputar_valores(X_preparado, medianas)

    # APARTADO 2: Identificar posibles valores atípicos mediante
    # técnicas estadísticas.
    atipicos = detectar_atipicos_iqr(X_limpio)

    # APARTADO 2: Diferenciar entre errores de medición y observaciones
    # extremas que puedan representar situaciones reales de funcionamiento anómalo.
    # Los valores fuera de los límites físicos se corrigen.
    # Los atípicos estadísticos dentro de los límites se conservan:
    # el criterio IQR no demuestra que una medición sea un error.

    informe = {
        "ausentes_por_variable": np.sum(ausentes, axis=0),
        "registros_con_ausentes": registros_con_ausentes,
        "fuera_rango_por_variable": np.sum(fuera_rango, axis=0),
        "atipicos_por_variable": np.sum(atipicos, axis=0),
        "medianas": medianas,
        "registros_descartados": registros_descartados,
        "registros_a_corregir": registros_a_corregir,
        "registros_sin_problemas": registros_sin_problemas,
        "registros_conservados": np.sum(mascara_valida)
    }

    return X_limpio, mascara_valida, informe


def mostrar_informe_limpieza(ids, informe):
    """Muestra los problemas detectados y las decisiones tomadas."""
    print("\n=== APARTADO 2: LIMPIEZA Y PREPARACIÓN ===")

    print("\nValores ausentes por variable:")

    for indice in range(len(COLUMNAS_NUMERICAS)):
        print(
            f"- {COLUMNAS_NUMERICAS[indice]}: "
            f"{informe['ausentes_por_variable'][indice]}"
        )

    print("\nIdentificadores de registros con valores ausentes:")
    print(ids[informe["registros_con_ausentes"]])

    print("\nValores fuera del rango físico por variable:")

    for indice in range(len(COLUMNAS_NUMERICAS)):
        print(
            f"- {COLUMNAS_NUMERICAS[indice]}: "
            f"{informe['fuera_rango_por_variable'][indice]}"
        )

    print("\nMedianas utilizadas para corregir valores:")

    for indice in range(len(COLUMNAS_NUMERICAS)):
        print(
            f"- {COLUMNAS_NUMERICAS[indice]}: "
            f"{informe['medianas'][indice]:.3f}"
        )

    print("\nAtípicos IQR en los registros conservados:")

    for indice in range(len(COLUMNAS_NUMERICAS)):
        print(
            f"- {COLUMNAS_NUMERICAS[indice]}: "
            f"{informe['atipicos_por_variable'][indice]}"
        )

    print("\nRegistros sin problemas de ausencia o rango físico:")
    print(np.sum(informe["registros_sin_problemas"]))

    print("\nIdentificadores de registros corregidos:")
    print(ids[informe["registros_a_corregir"]])

    print("\nIdentificadores de registros descartados:")
    print(ids[informe["registros_descartados"]])

    print("\nTotal de registros conservados:")
    print(informe["registros_conservados"])

    print(
        "\nLos errores físicos se han corregido y los atípicos "
        "estadísticos se han conservado."
    )