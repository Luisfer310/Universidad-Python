# Define una clase llamada CuentaBancaria con atributos saldo y nombre_titular. Implementa métodos para depositar y retirar dinero, asegurándote de que el saldo no se pueda acceder o modificar directamente desde 
# fuera de la clase.

class CuentaBancaria:
    def __init__(self, saldo, nombre_titular):
        self.__saldo = saldo
        self.__nombre_titular = nombre_titular

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    @property
    def nombre_titular(self):
        return self.__nombre_titular
    @nombre_titular.setter
    def nombre_titular(self, nombre_titular):
        self.__nombre_titular = nombre_titular

    def depositar(self, monto):
        self.__saldo += monto

    def retirar(self, monto):
        self.__saldo -= monto

    def __str__(self):
        return f''' 
Querid@ {self.__nombre_titular}
Su saldo acutual es de: {self.__saldo}
'''
    
CuentaLuis = CuentaBancaria(3000, 'Luis')
print(CuentaLuis)
CuentaLuis.depositar(1000)
print(CuentaLuis)
CuentaLuis.retirar(500)
print(CuentaLuis)