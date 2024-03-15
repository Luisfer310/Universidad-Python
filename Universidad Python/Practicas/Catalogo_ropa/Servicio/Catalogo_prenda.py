import os

class CatalogoPrendas:
    ruta_archivo = 'prendas.txt'

    @classmethod
    def agregar_prenda(cls, prenda):
        with open(cls.ruta_archivo, 'a') as archivo:
            archivo.write(f'{prenda}\n')

    @classmethod
    def listar_prendas(cls):
        with open(cls.ruta_archivo, 'r') as archivo:
            print(archivo.read())

    @classmethod
    def eliminar(cls):
        os.remove(cls.ruta_archivo)