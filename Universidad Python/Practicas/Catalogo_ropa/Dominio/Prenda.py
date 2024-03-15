class Prenda:
    def __init__(self, prenda):
        self._prenda = prenda

    @property
    def prenda(self):
        return self._prenda
    @prenda.setter
    def prenda(self, prenda):
        self._prenda = prenda

    def __str__(self):
        return f'{self._prenda}'