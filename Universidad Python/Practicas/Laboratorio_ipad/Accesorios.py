class Accesorios:
    contador_accesorios = 0

    def __init__(self, marca):
        Accesorios.contador_accesorios += 1
        self._id_accesorio = Accesorios.contador_accesorios
        self._marca = marca

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    def __str__(self):
        return f'El accesorio #{self._id_accesorio} es de la marca {self._marca}'
