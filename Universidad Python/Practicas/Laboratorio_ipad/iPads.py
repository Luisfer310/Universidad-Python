from Accesorios import *
from Funda import *
from Teclado import *

class Ipads:
    contador_ipads = 0

    def __init__(self, modelo, funda, teclado):
        Ipads.contador_ipads += 1
        self._id_ipads = Ipads.contador_ipads
        self._modelo = modelo
        self._funda = funda
        self._teclado = teclado

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def funda(self):
        return self._funda

    @funda.setter
    def funda(self, funda):
        self._funda = funda

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    def __str__(self):
        return f'iPad {self._modelo}, {self._funda}, {self._teclado}'
