from Accesorios import *

class Funda(Accesorios):
    contador_fundas = 0

    def __init__(self, marca, material):
        Funda.contador_fundas += 1
        super().__init__(marca)
        self._id_funda = Funda.contador_fundas
        self._material = material

    @property
    def id_funda(self):
        return self._id_funda
    @id_funda.setter
    def id_funda(self, id_funda):
        self._id_funda = id_funda

    @property
    def material(self):
        return self._material
    @material.setter
    def material(self, material):
        self._material = material

    def __str__(self):
        return super().__str__() + f'\nMaterial: {self._material}'
