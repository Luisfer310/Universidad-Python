from Accesorios import *

class Cargador(Accesorios):
    contador_cargadores = 0

    def __init__(self, marca, wats):
        Cargador.contador_cargadores += 1
        super().__init__(marca)
        self._id_cargador = Cargador.contador_cargadores
        self._wats = wats

    @property
    def id_cargador(self):
        return self._id_cargador
    @id_cargador.setter
    def id_cargador(self, id_cargador):
        self._id_cargador = id_cargador

    @property
    def wats(self):
        return self._wats
    @wats.setter
    def wats(self, wats):
        self._wats = wats

    def __str__(self):
        return f'El cargador #{self._id_cargador} es marca: {self._marca} y es de {self._wats} Wats'