from Accesorios import *
from Funda import *
from Cargador import *

class Celular:
    contador_celulares = 0

    def __init__(self, cargador, funda, marca, modelo):
        Celular.contador_celulares += 1
        self._id_celulares = Celular.contador_celulares
        self._cargador = cargador
        self._funda = funda
        self._marca = marca
        self._modelo = modelo

    @property
    def id_celulares(self):
        return self._id_celulares
    @id_celulares.setter
    def id_celulares(self, id_celulares):
        self._id_celulares = id_celulares

    @property
    def cargador(self):
        return self._cargador
    @cargador.setter
    def cargador(self, cargador):
        self._cargador = cargador

    @property
    def funda(self):
        return self._funda
    @funda.setter
    def funda(self, funda):
        self._funda = funda

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    def __str__(self):
        return f'Tu celular {self._marca} {self._modelo}, tendra los accesorios: Funda:[{self._funda}], Cargador:[{self._cargador}]'
    
if __name__ == '__main__':
    funda = Funda('Gorilla', 'Piel')
    cargador = Cargador('Apple', 20)
    celular = Celular(cargador, funda, 'Apple', 'iPhone 13 Pro')
    print(celular)