# Ejemplo 1
"""class Padre:
    def hablar(self):
        print("Hola desde padre")


class Madre:
    def caminar(self):
        print("Estoy caminando")

class Hijo(Padre, Madre):
    pass

hijo = Hijo()

hijo.hablar()
hijo.caminar()"""

# Ejemplo 2
"""class Padre:
    def hablar(self):
        print("Hola desde padre")

class Madre:
    def hablar(self):
        print("Hola desde madre")

class Hijo1(Padre, Madre):
    pass

class Hijo2(Madre, Padre):
    pass

hijo1 = Hijo1()
hijo2 = Hijo2()

hijo1.hablar()
hijo2.hablar()"""

# Ejemplo 3
""""class A:
    def __init__(self):
        print("A")
        super().__init__()

class B:
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(C,B):
    def __init__(self):
        print("D")
        super().__init__()

prueba = D()"""

# Ejemplo 4
"""class Temperatura:
    def __init__(self, celsius: float):
        self.celsius = celsius

    # LECTOR
    @property
    def celsius(self) -> float:
        return self._celsius

    # ESCRITOR (SETTER) CON VALIDACIÓN
    @celsius.setter
    def celsius(self, value: float):
        if value < -273.15:
            raise ValueError("No puedes estar por debajo del cero absoluto (-273.15ºC)")
        self._celsius = value

    # CONVERSOR (GETTER DERIVADO)
    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32

    # BORRADOR (DELETER)
    @celsius.deleter
    def celsius(self):
        del self._celsius

temp = Temperatura(20.0)
print(temp.celsius)
print(temp.fahrenheit)

temp.celsius = 100.0
print(temp.celsius)

temp.celsius = -300.0"""

# EJEMPLO 5
"""from datetime import date

class Empleado:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    # CONSTRUCTOR ALERNATIVO: CREAR DESDE UN AÑO DE NACIMIENTO
    @classmethod
    def desde_anio_nacimiento(cls, nombre: str, anio_nacimiento: int) -> "Empleado":
        # CLS ES LA CLASE QUE SE USA PARA LLAMAR (EMPLEADO O SUBCLASE)
        edad = date.today().year
        return cls(nombre, edad)

    # MÉTODO DE UTILIDAD: VALIDAR SI UN EMPLEADO ES MAYOR DE EDAD
    @classmethod
    def es_mayor_de_edad(cls, empleado: "Empleado") -> bool:
        return empleado.edad >= 18

emp1 = Empleado("Ana",30)
emp2 = Empleado.desde_anio_nacimiento("Carlos", 1995)

print(emp1.nombre)
print(emp2.nombre)
print(emp2.edad)

print(Empleado.es_mayor_de_edad(emp1))"""