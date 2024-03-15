import os

class Carrito:
    ruta_archivo = 'produtos.txt'

    @classmethod
    def agregar_producto(cls, producto):
        with open(cls.ruta_archivo, 'a') as archivo:
            archivo.write(f'{producto}\n')

    @classmethod
    def listar_productos(cls):
        with open(cls.ruta_archivo, 'r') as archivo:
            print(archivo.read())

    @classmethod
    def eliminar_productos(cls):
        os.remove(cls.ruta_archivo)