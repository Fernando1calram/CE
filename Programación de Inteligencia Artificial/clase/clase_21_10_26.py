# Ejemplo 1
"""from datetime import date

class Empleado:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    # Función de utilidad: calcular edad a partir del año de nacimiento
    @staticmethod
    def calcular_edad(anio_nacimiento: int) -> int:
        return date.today().year - anio_nacimiento

    # Función de utilidad: validar formato de email (regla simple)
    @staticmethod
    def validar_email(email: str) -> bool:
        return "@" in email and "." in email.split("@")[-1]

print(Empleado.calcular_edad(1990))
print(Empleado.calcular_edad(1990))

print(Empleado.validar_email("ana@correo.com"))
print(Empleado.validar_email("correo.invalido"))

emp = Empleado("Ana", 30)
print(emp.calcular_edad(1990))"""

# Ejemplo 2
"""from abc import ABC, abstractmethod

class Imprimible(ABC):
    @abstractmethod
    def imprimit(self) -> str:
        pass

# Registrar una clase que NO hereda de Imprimible
class Documento:
    def __init__(self, texto: str):
        self.texto = texto

    def  imprimir(self) -> str:
        return self.texto

# Registrar manualmente (verisifcación solo de método, no de herencia)
Imprimible.register(Documento)

# Ahora Documento "cumple el contrato"
doc = Documento("Hola mundo")
print(isinstance(doc, Imprimible)) # True (virtaul subclass)
print(doc.imprimir())"""


# Ejemplo 3 clase iterable
"""class MiColeccion:
    def __init__(self, datos):
        self._datos = datos

    # Es iterable porque implementa __iter__
    def __iter__(self):
        return iter(self._datos)

    # Pero no implementa __next__ por lo que no es iterador
    # Por eso no devuelve una referencia a si misma, sino al iterador de list.

col = MiColeccion([10,20,30])
for valor in col: # Funciona porque MiColeccion es iterable
    print(valor)"""

# Ejemplo 4
"""class CuentaAtras:
        Clase que ES SU PROPIO iterador.
        Útil cuando el estado del iterador no necesita persistir
        después de consumir la secuencia.

    def __init__(self, inicio: int):
        self._inicio = inicio
        self._actual = inicio # estado del iterador

    def __iter__(self) -> "CuentaAtras":
        return self # Devuelve si mismo

    def __next__(self) -> int:
        if self._actual < 0:
            raise StopIteration
        valor = self._actual
        self._actual -= 1 # decrementa
        return valor

    def __repr__(self):
        return f"CuentaAtras({self._inicio})"

# USO
cuenta = CuentaAtras(5)
print("\nEmpieza el primer recorrido")
for n in cuenta:
    print(n, end=" ")
# Salida: 5 4 3 2 1 0
print("\nEmpieza el segundo recorrido:")
# No se puede repetir"""

# Ejemplo 5
from collections.abc import Iterator, Iterable
class NumerosPares:
    """
    Clase ITERABLE: representa una secuencia de números pares.
    No avanza por los elementos; solo sabe crear iteradores."""
    def __init__(self, maximo: int):
        self.maximo = maximo

    def __iter__(self) -> "IteradorNumerosPares":
        # Cada vez que llamas iter(), creas un iterador NUEVO.
        # Esto permite hacer 'for' múltples veces sobre el mismo objeto.
        return IteradorNumerosPares(self.maximo)

class IteradorNumerosPares:
    """ Class ITERADORA: avanza de uno en uno por los números pares. """
    def __init__(self, maximo: int):
        self._actual = 0        # primer valor a devolver
        self._maximo = maximo   # limite

    def __next__(self) -> int:
        if(self._actual > self._maximo):
            raise StopIteration # fin de la secuencia
        valor = self._actual
        self._actual += 2       # siguiente par
        return valor

# USO
# Primer 'for': crea un iterador, avanza 0, 2, 4, 6, 8, 10
secuencia = NumerosPares(10)
for n in secuencia:
    print(n, end= " ")
# Salida: 0 2 4 6 8 10
# Segundo 'for': crea un iterador NUEVO, vuelve a empezar
for n in secuencia:
    print(n, end=" ")
#Salida: 0 2 4 6 8 10 <- se puede repetir porque el iterable es reutilizable

print(isinstance(secuencia, Iterable)) # True (tiene __iter__)
print(isinstance(secuencia, Iterator)) # False (no tiene __next)