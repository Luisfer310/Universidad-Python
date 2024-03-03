class Producto:
    contador_producto = 0

    def __init__(self, nombre, precio):
        Producto.contador_producto += 1
        self._id = Producto.contador_producto
        self._nombre = nombre
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, precio):
        self._precio = precio

    def __str__(self):
        return(f'El proucto: {self._nombre}, tiene un precio de ${self._precio}. [ID: {self._id}]')
    
if __name__ == '__main__':
    Producto1 = Producto('Camisa', 250.00)
    print(Producto1)
    Producto2 = Producto('Pantalon', 300.00)
    print(Producto2)