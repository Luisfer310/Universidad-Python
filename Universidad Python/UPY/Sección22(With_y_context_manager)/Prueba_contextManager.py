from with_contextManager import *

with ManejoArchivo('NuevoArchivo.txt') as archivo:
    print(archivo.read())