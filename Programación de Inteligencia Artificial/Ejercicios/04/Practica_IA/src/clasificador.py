import numpy as np


def dividir_estratificado(X, y, proporcion_entrenamiento=0.8):
    """
    Divide los datos por clases para conservar aproximadamente
    sus proporciones en entrenamiento y prueba.
    """
    if proporcion_entrenamiento <= 0 or proporcion_entrenamiento >= 1:
        raise ValueError(
            "La proporción de entrenamiento debe estar entre 0 y 1."
        )

    # Fijamos una semilla para que la división sea reproducible.
    np.random.seed(42)

    indices_entrenamiento = []
    indices_prueba = []

    # APARTADO 4: Mantener una distribución equilibrada de las categorías
    # en ambas particiones.
    for estado in [0, 1, 2]:
        indices_clase = np.arange(len(y))[y == estado]
        print("indicesclase",indices_clase)

        if len(indices_clase) < 2:
            raise ValueError(
                f"El estado {estado} necesita al menos dos registros "
                "para aparecer en entrenamiento y prueba."
            )

        indices_mezclados = np.random.permutation(indices_clase)

        # APARTADO 4: Dividir el conjunto de datos en entrenamiento
        # (80 %) y prueba (20 %).
        # El valor predeterminado es 0.8; el redondeo puede producir
        # pequeñas diferencias al trabajar con registros enteros.
        corte = int(len(indices_mezclados) * proporcion_entrenamiento)

        if corte == 0 or corte == len(indices_mezclados):
            raise ValueError(
                f"La división deja una partición vacía para el estado {estado}."
            )

        indices_entrenamiento.extend(indices_mezclados[:corte])
        indices_prueba.extend(indices_mezclados[corte:])

    indices_entrenamiento = np.array(indices_entrenamiento, dtype=int)
    indices_prueba = np.array(indices_prueba, dtype=int)

    indices_entrenamiento = np.random.permutation(indices_entrenamiento)
    indices_prueba = np.random.permutation(indices_prueba)

    return (
        X[indices_entrenamiento],
        X[indices_prueba],
        y[indices_entrenamiento],
        y[indices_prueba]
    )


def normalizar(X_entrenamiento, X_prueba):
    """Normaliza ambos conjuntos con los parámetros de entrenamiento."""

    # APARTADO 4: Normalizar las variables utilizando la media y
    # desviación estándar del conjunto de entrenamiento.
    media = np.mean(X_entrenamiento, axis=0)
    print("media",media)
    desviacion = np.std(X_entrenamiento, axis=0)
    print("desviacion",desviacion)

    # Evitamos dividir entre cero si una variable es constante.
    desviacion_segura = np.where(desviacion == 0, 1.0, desviacion)
    print("desviacion segura",desviacion_segura)

    X_entrenamiento_normalizado = (
        (X_entrenamiento - media) / desviacion_segura
    )

    # APARTADO 4: Aplicar exactamente la misma transformación
    # al conjunto de prueba.
    X_prueba_normalizado = (
        (X_prueba - media) / desviacion_segura
    )

    return (
        X_entrenamiento_normalizado,
        X_prueba_normalizado,
        media,
        desviacion
    )


def calcular_centroides(X_entrenamiento, y_entrenamiento):
    """Obtiene un vector medio para cada categoría."""
    centroides = {}

    # APARTADO 5: Calcular el centroide de cada categoría utilizando
    # los datos de entrenamiento.
    for estado in [0, 1, 2]:
        mascara = y_entrenamiento == estado

        if np.sum(mascara) == 0:
            raise ValueError(
                f"No hay registros de entrenamiento del estado {estado}."
            )

        centroides[estado] = np.mean(
            X_entrenamiento[mascara],
            axis=0
        )

    return centroides


def calcular_distancias(X, centroides):
    """Devuelve una matriz de distancias de observaciones a centroides."""
    estados = np.array([0, 1, 2])
    distancias = np.zeros((X.shape[0], len(estados)))

    # APARTADO 5: Para cada observación del conjunto de prueba,
    # calcular su distancia euclídea respecto a los tres centroides.
    for indice in range(len(estados)):
        estado = estados[indice]
        diferencia = X - centroides[estado]

        # Sumamos los cuadrados por fila y calculamos su raíz.
        distancias[:, indice] = (
            np.sum(diferencia ** 2, axis=1) ** 0.5
        )

    return distancias, estados


def predecir(X, centroides):
    """Clasifica las observaciones mediante el centroide más cercano."""
    distancias, estados = calcular_distancias(X, centroides)

    # APARTADO 5: Asignar a la observación la categoría cuyo centroide
    # se encuentre a menor distancia.
    indices_minimos = np.argmin(distancias, axis=1)
    categorias_asignadas = estados[indices_minimos]

    # APARTADO 5: Almacenar las predicciones obtenidas.
    y_predicho = categorias_asignadas.copy()

    return y_predicho, distancias