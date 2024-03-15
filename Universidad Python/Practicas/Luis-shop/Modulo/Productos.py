class Productos:
    def __init__(self, producto):
        self._producto = producto

    @property
    def producto(self):
        return self._producto
    @producto.setter
    def producto(self, producto):
        self._producto = producto

    def __str__(self):
        print(f'{self._producto}')