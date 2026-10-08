class CuentaBancaria:

    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        self.saldo -= monto

    def __str__(self):
        return f"Cuenta de {self.titular}: {self.saldo:.2f}€"

    def __add__(self, other):
        return f"{self.saldo + other.saldo}€"

cuenta_bancaria_1 = CuentaBancaria("Fernando", 100.0)
cuenta_bancaria_2 = CuentaBancaria("Ismael", 500.0)

print(cuenta_bancaria_1)
print(cuenta_bancaria_2)
print(cuenta_bancaria_1.__add__(cuenta_bancaria_2))
    