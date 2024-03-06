from Accesorios import *

class Funda(Accesorios):
    contador_funda = 0

    def __init__(self, marca, material):
        super().__init__(marca)
        Funda.contador_funda += 1
        self.__id_funda = Funda.contador_funda
        self._material = material

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, material):
        self._material = material

    def __str__(self):
        return f'Funda: {self._marca}, Material de funda: {self._material}'
