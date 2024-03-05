class Accesorios:
    contador_accesorios = 0

    def __init__(self, marca):
        Accesorios.contador_accesorios += 1
        self._id_accesorios = Accesorios.contador_accesorios
        self._marca = marca

    @property
    def id_accesorios(self):
        return self._id_accesorios
    @id_accesorios.setter
    def id_accesios(self, id_accesorios):
        self._id_accesorios = id_accesorios

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    def __str__(self):
        return f'Accesorio marca: {self._marca}'