# Ejemplo 1
"""class Coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False

    def arrancar(self):
        self.enmarcha = True

    def estado(self):
        if(self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"

miCoche = Coche()
print("El largo del coche es: ", miCoche.largoChasis)
print("El coche tiene: ", miCoche.ruedas, "ruedas,")
miCoche.arrancar()

print(miCoche.estado())"""

# Ejemplo 2
"""class Coche():
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False

    def arrancar(self, arrancamos):  # self es el this de java
        self.enmarcha = arrancamos
        if(self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene", self.ruedas, " ruedas. Un ancho de", self.anchoChasis,
              " y un largo de ", self.largoChasis)


miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("--------- A continuación creamos el segundo objeto ---------")

miCoche2 = Coche()
print(miCoche.arrancar(False))
miCoche2.estado()"""

# Ejemplo 3
"""class Coche():
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    def arrancar(self, arrncamos):
        if(self.__enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene", self.__ruedas, " ruedas. Un ancho de", self.__anchoChasis,
              " y un largo de ", self.__largoChasis)

miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("--------- A continuación creamos el segundo objeto ---------")

miCoche2 = Coche()
print(miCoche.arrancar(False))
miCoche2.ruedas = 2
miCoche2.estado()"""

# Ejemplo 4
"""class Coche():
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos

        if(self.__enmarcha):
            chequeo = self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "El coche está en marcha"
        elif(self.__enmarcha and chequeo == False):
            return "Algo ha ido mal en el chequeop. No se puede arrancar"
        else:
            return "El coche está parado"

    def estado(self):
        print("El coche tiene", self.__ruedas, " ruedas. Un ancho de", self.__anchoChasis,
              " y un largo de ", self.__largoChasis)

    def __chequeo_interno(self):
        print("Realizando chequeo interno")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"
        if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False
print("--------- A continuación creamos el primer objeto ---------")

miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("--------- A continuación creamos el segundo objeto ---------")

miCoche2 = Coche()
print(miCoche.arrancar(False))
miCoche2.estado()"""

# Ejemplo 5
"""class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo; ", self.modelo, "\nEn Marcha: ",
              self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena,)

class Moto(Vehiculos):
    pass

miMoto = Moto("Honda", "CBR")
miMoto.estado()"""

# Ejemplo 6
"""class Vehiculos():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo; ", self.modelo, "\nEn Marcha: ",
              self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena,)

class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar
        if(self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"

class Moto(Vehiculos):
    hcaballito = ""
    def caballito(self):
        self.hcaballito = "Voy haciendo un caballito"

    def estado(self):
        print("Marcha: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ",
              self.enmarcha, "\nAccelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hcaballito)

class VElectricos():
    def __init__(self):
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True

miMoto = Moto("Honda","CBR")
miMoto.caballito()
miMoto.estado()

miFurgoneta = Furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

class BicicletaElectrica(VElectricos, Vehiculos):
    pass

miBici = BicicletaElectrica()"""

# Ejemplo 7
"""class Persona():
    def __init__(self, nombre, edad , Lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = Lugar_residencia

    def descripcion(self):
        print("Nombre: ", self.nombre, "Edad: ", self.edad, "Residencia: ", self.lugar_residencia)

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad

    def descripcion(self):
        super().descripcion()
        print("Salario: ", self.salario, "Antiguedad: ", self.antiguedad)

print("--------------------")
Antonio = Empleado(1500,15, "Antonio", 55, "España")
Antonio.descripcion()
print("--------------------")
Manuel = Persona("Manuel", 60, "España")
Manuel.descripcion()
print("--------------------")
print(isinstance(Antonio, Empleado))
print(isinstance(Antonio, Persona))
print(isinstance(Manuel, Persona))
print(isinstance(Manuel, Empleado))"""

# Ejemplo 8
class Coche():
    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo = Camion()
desplazamientoVehiculo(miVehiculo)