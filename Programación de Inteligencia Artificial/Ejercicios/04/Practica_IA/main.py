from src.carga import cargar_datos, explorar_datos

def main():
    ids, x, y = cargar_datos()
    explorar_datos(ids,x,y)

if __name__ == "__main__":
    main()