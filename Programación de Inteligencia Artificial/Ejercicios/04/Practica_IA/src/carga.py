import csv
import numpy as np


COLUMNAS_NUMERICAS = ["temperatura", "vibracion", "consumo", "presion"]
COLUMNAS = ["id"] + COLUMNAS_NUMERICAS + ["estado"]

RANGOS_VALIDOS = {
    "temperatura": (0.0, 150.0),
    "vibracion": (0.0, 15.0),
    "consumo": (0.0, 65.0),
    "presion": (0.0, 12.0)
}


def cargar_datos(ruta_csv):
    """
    Carga el CSV y devuelve los identificadores, las variables
    predictoras y la variable objetivo en arrays de NumPy.
    """
    try:
        with open(ruta_csv, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            ids = []
            valores = []
            estados = []

            for registro in lector:
                ids.append(registro["id"])

                # Validamos el estado antes de convertirlo a entero
                # para no aceptar accidentalmente valores como 1.5.
                estado = float(registro["estado"])

                if estado != 0 and estado != 1 and estado != 2:
                    raise ValueError(
                        "La variable estado contiene un valor no válido."
                    )

                estados.append(int(estado))
                fila_numerica = []

                for columna in COLUMNAS_NUMERICAS:
                    texto = registro[columna]

                    if texto is None:
                        raise ValueError(
                            "Un registro tiene menos campos de los esperados."
                        )

                    texto = texto.strip()

                    # Representamos los campos vacíos mediante NaN.
                    if texto == "":
                        fila_numerica.append(np.nan)
                    else:
                        try:
                            fila_numerica.append(float(texto))
                        except ValueError:
                            # Un texto no numérico se marca para su tratamiento.
                            fila_numerica.append(np.nan)

                valores.append(fila_numerica)

        # Comprobamos que hay datos antes de consultar las dimensiones.
        if len(valores) == 0:
            raise ValueError("El archivo CSV no contiene registros.")

        ids = np.array(ids)

        # APARTADO 4: Separar las variables predictoras de la variable objetivo.
        X = np.array(valores, dtype=float)
        y = np.array(estados, dtype=int)

        if X.shape[1] != len(COLUMNAS_NUMERICAS):
            raise ValueError(
                "El número de variables predictoras no es el esperado."
            )

        if X.shape[0] != y.shape[0] or X.shape[0] != ids.shape[0]:
            raise ValueError(
                "El número de registros de X, y e ids no coincide."
            )

        return ids, X, y

    except FileNotFoundError:
        raise FileNotFoundError(
            f"No se ha encontrado el archivo: {ruta_csv}"
        )

    except KeyError as error:
        raise ValueError(
            f"Falta una columna esperada en el CSV: {error}"
        )


def explorar_datos(ids, X, y):
    """Muestra la exploración inicial del conjunto de datos."""
    print("\n=== APARTADO 1: CARGA Y EXPLORACIÓN ===")

    # APARTADO 1: Obtener las dimensiones del conjunto de datos.
    print("\nNúmero total de registros:", X.shape[0])
    print("Número de variables predictoras:", X.shape[1])
    print("Dimensiones de X:", X.shape)
    print("Dimensiones de y:", y.shape)

    # APARTADO 1: Identificar las variables disponibles.
    print("\nVariables disponibles:")

    for columna in COLUMNAS:
        print("-", columna)

    # APARTADO 1: Mostrar una muestra de los registros.
    print("\nPrimeros cinco registros:")
    print("id | temperatura | vibracion | consumo | presion | estado")

    numero_muestras = min(5, X.shape[0])

    for indice in range(numero_muestras):
        print(ids[indice], X[indice], y[indice])

    # APARTADO 1: Comprobar los tipos de datos.
    print("\nTipos de datos:")
    print("Identificadores:", ids.dtype)
    print("Variables predictoras:", X.dtype)
    print("Variable objetivo:", y.dtype)

    # APARTADO 1: Identificar los valores ausentes.
    ausentes = np.isnan(X)

    print("\nNúmero total de valores ausentes:", np.sum(ausentes))
    print("Valores ausentes por variable:")

    for indice in range(len(COLUMNAS_NUMERICAS)):
        cantidad = np.sum(ausentes[:, indice])
        porcentaje = cantidad / X.shape[0] * 100

        print(
            f"- {COLUMNAS_NUMERICAS[indice]}: "
            f"{cantidad} ({porcentaje:.2f} %)"
        )

    # APARTADO 1: Calcular el número de registros correspondientes
    # a cada categoría.
    categorias, recuentos = np.unique(y, return_counts=True)

    print("\nRegistros por categoría:")

    for indice in range(len(categorias)):
        porcentaje = recuentos[indice] / len(y) * 100

        print(
            f"- Estado {categorias[indice]}: "
            f"{recuentos[indice]} registros ({porcentaje:.2f} %)"
        )

    print("\nLa carga de los datos se ha completado correctamente.")