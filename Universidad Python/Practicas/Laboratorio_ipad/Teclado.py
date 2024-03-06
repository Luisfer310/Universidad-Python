from Accesorios import *

class Teclado(Accesorios):
    contador_teclados = 0

    def __init__(self, marca, idioma):
        super().__init__(marca)
        Teclado.contador_teclados += 1
        self.__id_teclado = Teclado.contador_teclados
        self._idioma = idioma

    @property
    def idioma(self):
        return self._idioma

    @idioma.setter
    def idioma(self, idioma):
        self._idioma = idioma

    def __str__(self):
        return f'Teclado: {self._marca}, Idioma del teclado: {self._idioma}'
