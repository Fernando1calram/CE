# Importamos la librería correspondiente para poder leer el archivo .csv
import csv
import numpy as np

COLUMNAS_NUMERICAS = ["temperatura","vibracion","consumo","presion"]
COLUMNAS = ["id"] + COLUMNAS_NUMERICAS + ["estado"]
RANGOS_VALIDOS = {
    "temperatura": (0.0,150.0),
    "vibracion": (0.0,15.0),
    "consumo": (0.0,65.0),
    "presion": (0.0,12.0),
}

# Carga del archivo
def cargar_datos():
    try:
        with open(".\\datos\\sensores.csv", "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            ids = []
            valores = []
            estados = []

            for registro in lector:

                ids.append(registro["id"])
                estados.append(float(registro["estado"]))
                fila = []
                for columna in COLUMNAS_NUMERICAS:
                    texto = registro[columna].strip()
                    if texto == "":
                        fila.append(np.nan)
                    else:
                        try:
                            fila.append(float(texto))
                        except ValueError:
                            fila.append(np.nan)
                valores.append(fila)

                # Convertimos las listas en arrays de Numpy
                x = np.array(valores, dtype=float)
                y = np.array(estados, dtype=int)
                ids = np.array(ids)

                # Comprobamos que los datos se han cargado correctamente
                if(x.shape[1] != len(COLUMNAS_NUMERICAS)):
                    raise ValueError("El número de columnas numéricas no coincide con el esperado")

                if(x.shape[0] != y.shape[0] or x.shape[0] != ids.shape[0]):
                    raise ValueError("El número de registros de x, y e ids no coinciden")

                print(ids)
                print(x)
                print(y)
                return ids, x, y
        
    except FileNotFoundError:
        raise FileNotFoundError("No se ha encontrado el archivo de sensores")

    except KeyError as error:
        raise ValueError("Falta una columna esperada en el .csv")

def explorar_datos(ids, x, y):

    print(f"Numero total de registros: {x.shape[0]}")
    print(f"Numero total de variables predictoras: {x.shape[1]}")
    print(f"Dimensiones de x: {x.shape}")
    print(f"Dimensiones de y: {y.shape}")
    for columna in COLUMNAS:
        print(columna)

    # Muestra de datos
    print(f"Muestra de datos")
    print(x[:5])
    print(ids[:5])
    print(y[:5])

    # Tipos de datos
    print(f"Tipos de datos")
    print(f"{x.dtype}")
    print(f"{ids.dtype}")
    print(f"{y.dtype}")

    # Valores ausentes
    print(f"Valores ausentes")
    valores_ausentes = np.isnan(x)
    total_ausentes = np.sum(valores_ausentes)

    print(f"Total ausencias:  {total_ausentes}")

    # Valores ausentes por variable
    print(f"Valores ausentes por variables")
    for indice, columna in enumerate(COLUMNAS_NUMERICAS):
        cantidad = np.sum(valores_ausentes[:, indice])
        porcentaje = (cantidad / x.shape[0]) * 100
        print(f"{columna}: {cantidad} {porcentaje: .2f} %")

    # Número de registros por categoría
    print(f"Registros por categoría")
    categorias, recuentos = np.unique(y, return_counts=True)
    for categoria, recuento in zip(categorias, recuentos):
        porcentaje = (recuento / y.shape[0]) * 100
        print(f"Estado: {int(categoria)}: {recuento} registros ({porcentaje:.2f} %)")

    # Comprobación de que el archivo está correctamente cargado
    if x.shape[0] == 0:
        raise ValueError("El archivo .csv no contiene registros")

    if not np.all(np.isin(y, [0,1,2])):
        raise ValueError("La variable estado contiene valores no válidos")

    print("Datos cargados correctamente")