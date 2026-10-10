class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._tipo_cuenta = "ahorro"
        self.__saldo = saldo_inicial
        self.movimientos = []

    def consultar_saldo(self):
        return self.__saldo

    def ingresar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a ingresar debe ser positiva")
        self.__saldo += cantidad
        self.movimientos.append(("ingreso",cantidad))

    def retirar(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva")
        self.__saldo -= cantidad
        self.movimientos.append(("retiro",cantidad))

    def _aplicar_comision(self, cantidad):
        self.__saldo -= cantidad
        self.movimientos.append("comisión",cantidad)
        return self.__saldo

    def __str__(self):
        return f"Cuenta de {self.titular} | Saldo: {self.__saldo:.2f}€"

    def __repr__(self):
        return (
            f"CuentaBancaria(titular={self.titular!r}, "
            f"saldo_inicial={self.__saldo})"
        )

    def __len__(self):
        return len(self.movimientos)

    def __add__(self, other):
        if not isinstance(other, CuentaBancaria):
            return NotImplemented

        titular = f"{self.titular} y {other.titular}"
        saldo = self.consultar_saldo() + other.consultar_saldo()

        return CuentaBancaria(titular, saldo)

    def __eq__(self, value):
        if not isinstance(value, CuentaBancaria):
            return NotImplemented

        return (
            self.titular == value.titular
            and self.consultar_saldo() == value.consultar_saldo()
        )

class CuentaJoven(CuentaBancaria):
    def __init__(self, titular, saldo_inicial):
        super().__init__(titular, saldo_inicial)
        self._tipo_cuenta = "joven"

    def aplicar_bono(self):
        print(f"Aplicando bono a cuenta: {self._tipo_cuenta}")
        self.ingresar(10)

cuenta1 = CuentaBancaria("Fernando", 1000)
cuenta2 = CuentaBancaria("María", 500)

cuenta1.ingresar(200)
cuenta1.retirar(100)

print(cuenta1.consultar_saldo())
print(cuenta2.consultar_saldo())

print(cuenta1)
print(str(cuenta1))

print(len(cuenta1))

cuenta_conjunta = cuenta1 + cuenta2
print(cuenta_conjunta)

cuenta3 = CuentaBancaria("Fernando", 1101)

print(cuenta1 == cuenta3)

"""print(cuenta.titular)
cuenta.titular = "Fernando Calles"
print(cuenta.titular)"""

"""print(cuenta._tipo_cuenta)
cuenta._tipo_cuenta = "nómina"
print(cuenta._tipo_cuenta)

print(cuenta.consultar_saldo())
cuenta.ingresar(500)
print(cuenta.consultar_saldo())"""

"""print(cuenta._CuentaBancaria__saldo)
print(cuenta.__dict__)"""

"""joven = CuentaJoven("Ana", 200)
joven.aplicar_bono()
print(joven.consultar_saldo())"""


# YIELD
"""def contar_hasta(n):
    print("Inicio del generador")
    for i in range(1, n + 1):
        print(f"Antes de yield {i}")
        yield i
        print(f"Después de yield {i}")

gen = contar_hasta(3)

print(next(gen))
# Inicio del generador
# Antes de yield 1
# 1

print(next(gen))
# Después de yield 1
# Antes de yield 2
# 2

print(next(gen))
# Después de yield 2
# Antes de yield 3
# 3

print(next(gen))
# Después de yield 3
# StopIteration"""