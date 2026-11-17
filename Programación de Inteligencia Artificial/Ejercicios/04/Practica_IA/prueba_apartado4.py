import numpy as np

from src.clasificador import dividir_estratificado, normalizar


def comprobar_arrays(obtenido, esperado, mensaje):
    """Compara arrays permitiendo pequeñas diferencias decimales."""
    assert obtenido.shape == esperado.shape, (
        mensaje + ": las formas no coinciden."
    )

    assert np.max(np.abs(obtenido - esperado)) < 0.000001, mensaje


def probar_division():
    """Comprueba la división estratificada con 15 registros conocidos."""
    filas = []
    etiquetas = []

    # Creamos cinco registros de cada una de las tres categorías.
    # La primera columna identifica de forma única cada fila.
    for estado in [0, 1, 2]:
        for numero in range(5):
            identificador = estado * 5 + numero

            filas.append([
                identificador,
                identificador + 100,
                identificador + 200,
                identificador + 300
            ])

            etiquetas.append(estado)

    X = np.array(filas, dtype=float)
    print("Predictoras", X)
    y = np.array(etiquetas, dtype=int)
    print("Objetivo", y)

    X_original = X.copy()
    y_original = y.copy()

    (
        X_entrenamiento,
        X_prueba,
        y_entrenamiento,
        y_prueba
    ) = dividir_estratificado(X, y)

    # APARTADO 4: Dividir el conjunto de datos en entrenamiento
    # (80 %) y prueba (20 %).
    assert X_entrenamiento.shape == (12, 4), (
        "Debería haber 12 registros de entrenamiento."
    )

    assert X_prueba.shape == (3, 4), (
        "Debería haber tres registros de prueba."
    )

    assert y_entrenamiento.shape == (12,), (
        "Debería haber 12 etiquetas de entrenamiento."
    )

    assert y_prueba.shape == (3,), (
        "Debería haber tres etiquetas de prueba."
    )

    print("Correcto: división 80 % / 20 %.")

    # APARTADO 4: Mantener una distribución equilibrada de las
    # categorías en ambas particiones.
    for estado in [0, 1, 2]:
        assert np.sum(y_entrenamiento == estado) == 4, (
            f"Debería haber cuatro registros del estado {estado} "
            "en entrenamiento."
        )

        assert np.sum(y_prueba == estado) == 1, (
            f"Debería haber un registro del estado {estado} en prueba."
        )

    print("Correcto: proporciones de las tres categorías.")

    # Verificamos que cada registro original aparece exactamente una vez.
    identificadores_entrenamiento = list(X_entrenamiento[:, 0])
    identificadores_prueba = list(X_prueba[:, 0])

    todos_identificadores = (
        identificadores_entrenamiento + identificadores_prueba
    )

    todos_identificadores.sort()

    assert todos_identificadores == list(range(15)), (
        "Se han perdido registros o aparecen registros repetidos."
    )

    for identificador in identificadores_entrenamiento:
        assert identificador not in identificadores_prueba, (
            "Un registro aparece en entrenamiento y prueba."
        )

    print("Correcto: no se pierden ni se repiten registros.")

    # Comprobamos que cada fila conserva su contenido y su etiqueta.
    for datos, estados in [
        (X_entrenamiento, y_entrenamiento),
        (X_prueba, y_prueba)
    ]:
        for posicion in range(len(datos)):
            indice_original = int(datos[posicion, 0])

            comprobar_arrays(
                datos[posicion],
                X[indice_original],
                "La fila ha cambiado durante la división."
            )

            assert estados[posicion] == y[indice_original], (
                "Una etiqueta ya no corresponde a su registro."
            )

    print("Correcto: correspondencia entre registros y etiquetas.")

    # La semilla fija debe producir la misma división en otra llamada.
    (
        X_entrenamiento_2,
        X_prueba_2,
        y_entrenamiento_2,
        y_prueba_2
    ) = dividir_estratificado(X, y)

    comprobar_arrays(
        X_entrenamiento,
        X_entrenamiento_2,
        "La división de entrenamiento no es reproducible."
    )

    comprobar_arrays(
        X_prueba,
        X_prueba_2,
        "La división de prueba no es reproducible."
    )

    comprobar_arrays(
        y_entrenamiento,
        y_entrenamiento_2,
        "Las etiquetas de entrenamiento han cambiado."
    )

    comprobar_arrays(
        y_prueba,
        y_prueba_2,
        "Las etiquetas de prueba han cambiado."
    )

    comprobar_arrays(
        X,
        X_original,
        "La división ha modificado X."
    )

    comprobar_arrays(
        y,
        y_original,
        "La división ha modificado y."
    )

    print("Correcto: reproducibilidad y conservación de los originales.")

    print("\nDistribución obtenida:")

    for estado in [0, 1, 2]:
        print(
            f"- Estado {estado}: "
            f"{np.sum(y_entrenamiento == estado)} en entrenamiento, "
            f"{np.sum(y_prueba == estado)} en prueba."
        )


def probar_normalizacion():
    """Comprueba la normalización con resultados calculados a mano."""
    X_entrenamiento = np.array([
        [10.0, 2.0, 100.0, 5.0],
        [30.0, 6.0, 300.0, 5.0]
    ])

    X_prueba = np.array([
        [40.0,  8.0, 400.0, 5.0],
        [50.0, 10.0, 500.0, 7.0]
    ])

    entrenamiento_original = X_entrenamiento.copy()
    prueba_original = X_prueba.copy()

    (
        entrenamiento_normalizado,
        prueba_normalizada,
        media,
        desviacion
    ) = normalizar(X_entrenamiento, X_prueba)

    # APARTADO 4: Normalizar las variables utilizando la media y
    # desviación estándar del conjunto de entrenamiento.
    media_esperada = np.array([20.0, 4.0, 200.0, 5.0])
    desviacion_esperada = np.array([10.0, 2.0, 100.0, 0.0])

    entrenamiento_esperado = np.array([
        [-1.0, -1.0, -1.0, 0.0],
        [ 1.0,  1.0,  1.0, 0.0]
    ])

    comprobar_arrays(
        media,
        media_esperada,
        "La media no coincide con la del entrenamiento."
    )

    comprobar_arrays(
        desviacion,
        desviacion_esperada,
        "La desviación no coincide con la del entrenamiento."
    )

    comprobar_arrays(
        entrenamiento_normalizado,
        entrenamiento_esperado,
        "El entrenamiento no se ha normalizado correctamente."
    )

    print("\nCorrecto: normalización del entrenamiento.")

    # APARTADO 4: Aplicar exactamente la misma transformación
    # al conjunto de prueba.
    prueba_esperada = np.array([
        [2.0, 2.0, 2.0, 0.0],
        [3.0, 3.0, 3.0, 2.0]
    ])

    comprobar_arrays(
        prueba_normalizada,
        prueba_esperada,
        "La prueba no utiliza los parámetros del entrenamiento."
    )

    print("Correcto: la prueba utiliza los parámetros del entrenamiento.")

    # La cuarta columna es constante en entrenamiento.
    # La función debe sustituir su divisor cero por uno.
    assert desviacion[3] == 0.0, (
        "La cuarta variable debería tener desviación cero."
    )

    assert prueba_normalizada[1, 3] == 2.0, (
        "Para la cuarta variable debería calcularse (7 - 5) / 1 = 2."
    )

    comprobar_arrays(
        X_entrenamiento,
        entrenamiento_original,
        "La normalización ha modificado el entrenamiento original."
    )

    comprobar_arrays(
        X_prueba,
        prueba_original,
        "La normalización ha modificado la prueba original."
    )

    print("Correcto: tratamiento de columnas constantes.")
    print("Correcto: conservación de los arrays originales.")

    print("\nMedia de entrenamiento:")
    print(media)

    print("\nDesviación de entrenamiento:")
    print(desviacion)

    print("\nEntrenamiento normalizado:")
    print(entrenamiento_normalizado)

    print("\nPrueba normalizada:")
    print(prueba_normalizada)


def main():
    print("=== PRUEBAS CONTROLADAS DEL APARTADO 4 ===\n")

    probar_division()
    probar_normalizacion()

    print("\nTodas las pruebas controladas han terminado correctamente.")


if __name__ == "__main__":
    main()