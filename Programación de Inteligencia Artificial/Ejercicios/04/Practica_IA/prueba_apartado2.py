import numpy as np

from src.limpieza import (
    identificar_ausentes,
    detectar_fuera_rango,
    calcular_cuartil,
    detectar_atipicos_iqr,
    limpiar_datos,
    mostrar_informe_limpieza
)


def probar_apartado2():
    """Comprueba los cinco puntos del apartado 2."""
    ids = np.array([
        "P001", "P002", "P003", "P004", "P005",
        "P006", "P007", "P008", "P009", "P010"
    ])

    # Columnas: temperatura, vibracion, consumo y presion.
    X = np.array([
        [60.0,   2.0,    20.0,  6.0],
        [65.0,   2.0,    20.0,  6.0],
        [70.0,   2.0,    20.0,  6.0],
        [75.0,   2.0,    20.0,  6.0],
        [80.0,   2.0,    20.0,  6.0],
        [85.0,   2.0,    20.0,  6.0],
        [np.nan, 2.0,    20.0,  6.0],
        [-10.0,  2.0,    20.0,  6.0],
        [140.0,  2.0,    20.0,  6.0],
        [70.0,   np.nan, 20.0, -1.0]
    ], dtype=float)

    # Guardamos una copia para comprobar que la limpieza no modifica X.
    X_original = X.copy()

    # APARTADO 2: Identificar los registros que contienen valores ausentes
    # y establecer un procedimiento para tratarlos.
    ausentes = identificar_ausentes(X)
    registros_con_ausentes = np.sum(ausentes, axis=1) > 0

    print("ausentes", ausentes)

    assert np.sum(ausentes) == 2, (
        "Debería haber dos valores ausentes."
    )

    assert ausentes[6, 0], (
        "P007 debería tener la temperatura ausente."
    )

    assert ausentes[9, 1], (
        "P010 debería tener la vibración ausente."
    )

    assert list(ids[registros_con_ausentes]) == ["P007", "P010"], (
        "Los registros con ausentes deberían ser P007 y P010."
    )

    # Ejecutamos el proceso completo para comprobar las correcciones.
    X_limpio, mascara_valida, informe = limpiar_datos(X)

    assert np.sum(np.isnan(X_limpio)) == 0, (
        "Los datos limpios no deberían contener NaN."
    )

    assert informe["medianas"][0] == 75.0, (
        "La mediana válida de temperatura debería ser 75."
    )

    assert X_limpio[6, 0] == 75.0, (
        "La temperatura ausente de P007 debería sustituirse por 75."
    )

    print("Correcto: detección y tratamiento de valores ausentes.")

    # APARTADO 2: Detectar mediciones que se encuentren fuera de
    # los rangos físicos admisibles de los sensores.
    fuera_rango = detectar_fuera_rango(X)

    assert np.sum(fuera_rango) == 2, (
        "Debería haber dos mediciones fuera de rango."
    )

    assert fuera_rango[7, 0], (
        "La temperatura -10 de P008 debería estar fuera de rango."
    )

    assert fuera_rango[9, 3], (
        "La presión -1 de P010 debería estar fuera de rango."
    )

    assert not fuera_rango[8, 0], (
        "La temperatura 140 de P009 está dentro del rango físico."
    )

    assert X_limpio[7, 0] == 75.0, (
        "La temperatura incorrecta de P008 debería sustituirse por 75."
    )

    # Comprobamos que los límites exactos se aceptan.
    limites = np.array([
        [0.0,   0.0,  0.0,  0.0],
        [150.0, 15.0, 65.0, 12.0]
    ])

    assert np.sum(detectar_fuera_rango(limites)) == 0, (
        "Los valores iguales a los límites deberían ser válidos."
    )

    print("Correcto: detección y corrección de errores físicos.")

    # APARTADO 2: Identificar posibles valores atípicos mediante
    # técnicas estadísticas.
    q1 = calcular_cuartil(X_limpio[:, 0], 0.25)
    q3 = calcular_cuartil(X_limpio[:, 0], 0.75)

    assert q1 == 70.0, "Q1 de temperatura debería ser 70."
    assert q3 == 80.0, "Q3 de temperatura debería ser 80."
    assert q3 - q1 == 10.0, "El IQR debería ser 10."

    atipicos = detectar_atipicos_iqr(X_limpio)

    assert atipicos[8, 0], (
        "La temperatura 140 de P009 debería ser un atípico."
    )

    assert np.sum(atipicos) == 1, (
        "Debería haber un único valor atípico."
    )

    print("Correcto: detección de atípicos mediante IQR.")

    # APARTADO 2: Diferenciar entre errores de medición y observaciones
    # extremas que puedan representar situaciones reales de funcionamiento anómalo.
    assert X_limpio[7, 0] == 75.0, (
        "El error físico -10 debería corregirse."
    )

    assert X_limpio[8, 0] == 140.0, (
        "El atípico físicamente válido 140 debería conservarse."
    )

    print("Correcto: los errores se corrigen y el atípico válido se conserva.")

    # APARTADO 2: Separar los registros válidos de aquellos que
    # deban descartarse o corregirse.
    assert X_limpio.shape == (9, 4), (
        "Deberían conservarse nueve registros."
    )

    assert list(ids[informe["registros_descartados"]]) == ["P010"], (
        "Solo debería descartarse P010."
    )

    assert list(ids[informe["registros_a_corregir"]]) == ["P007", "P008"], (
        "Solo deberían corregirse P007 y P008."
    )

    assert np.sum(informe["registros_sin_problemas"]) == 7, (
        "Debería haber siete registros sin ausencias ni errores físicos."
    )

    assert list(ids[mascara_valida]) == list(ids[:9]), (
        "Deberían conservarse P001 hasta P009, en el mismo orden."
    )

    print("Correcto: separación de registros conservados y descartados.")

    # Comprobamos que las seis primeras filas permanecen intactas.
    assert np.sum(X_limpio[:6] != X_original[:6]) == 0, (
        "Los registros válidos iniciales no deberían modificarse."
    )

    # Verificamos que la matriz original conserva sus valores.
    assert np.isnan(X[6, 0]), (
        "La limpieza no debería modificar el NaN del array original."
    )

    assert X[7, 0] == -10.0, (
        "La limpieza no debería modificar el -10 del array original."
    )

    print("Correcto: los registros válidos y los datos originales se respetan.")

    mostrar_informe_limpieza(ids, informe)

    print("\nDatos finales:")
    print(X_limpio)

    print("\nTodas las pruebas del apartado 2 han terminado correctamente.")


if __name__ == "__main__":
    probar_apartado2()