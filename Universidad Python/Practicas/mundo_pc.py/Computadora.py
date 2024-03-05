from Monitor import *
from Teclado import *
from Raton import *

class Computadora:
    contador_cmomputadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_cmomputadoras += 1
        self.id_computadra = Computadora.contador_cmomputadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self._monitor
    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado
    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self._raton
    @raton.setter
    def raton(self, raton):
        self._raton = raton

    def __str__(self):
        return f'''
            Computadora: {self._nombre}
            Dispositivos: Teclado[{self._teclado}], Raton[{self._raton}], Monitor[{self._monitor}]
'''
    
if __name__ == '__main__':    
    nombre = input('Nombre de la PC: ')
    monitor = input('Monitor: ')
    teclado = input('Teclado: ')
    raton = input('Raton: ')
    compu = Computadora(nombre, monitor, teclado, raton)
    print(compu)