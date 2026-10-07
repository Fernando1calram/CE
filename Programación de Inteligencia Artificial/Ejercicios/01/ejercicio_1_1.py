# Introducimos el precio original
precio_original = float(input("Introduce el precio original del artículo: "))

# Introducimos el porcentaje de descuento
porcentaje_descuento = float(input("Introduce el porcentaje de descuento: "))

# Función que en función del porcentaje escribe el tipo de descuento que se está aplicando
def informa_oferta(porcentaje):
    if(porcentaje == 0):
        return("Sin descuento")
    elif(porcentaje >= 1 and porcentaje <= 15):
        return("Oferta")
    elif(porcentaje >= 16 and porcentaje <= 40):
        return("Gran oferta")
    else:
        return("Liquidación")

# Función que calcula el precio con el descuento aplicado
def calcula_precio(precio, porcentaje):
    return str(precio * (1 - porcentaje / 100))

# Llamada a las funciones
print("El precio final es de "  + calcula_precio(precio_original,porcentaje_descuento) +
    "€. La oferta del artículo es:  " +  informa_oferta(porcentaje_descuento))