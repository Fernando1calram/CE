def precio():
    return float(input("Introduce el precio original del articulo: "))

def porcentaje_descuento():
    return float(input("Introduce el porcentaje de descuento: "))

def calcular_descuento(precio, porcentaje_de_descuento):
    return float(precio) - (float(precio) * (float(porcentaje_de_descuento) / 100))

def muestra_resultado(porcentaje_descuento):
    if (porcentaje_descuento == 0):
        return "Sin descuento"
    elif (porcentaje_descuento >= 1 and porcentaje_descuento <= 15):
        return "Oferta"
    elif (porcentaje_descuento >= 16 and porcentaje_descuento <= 40):
        return "Gran oferta"
    else:
        return "Liquidación"

def mostrar(precio, porcentaje_descuento):
    print("El precio final es de: " + f'{calcular_descuento(precio, porcentaje_descuento)}' + " ya que el artículo tiene un/una " + 
          f'{muestra_resultado(porcentaje_descuento)}' + " de descuento.")

mostrar(precio(), porcentaje_descuento())