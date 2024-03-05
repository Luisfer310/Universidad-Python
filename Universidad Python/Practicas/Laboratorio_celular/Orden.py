from Accesorios import *
from Funda import *
from Cargador import *
from Telefonos import * 

class Orden:
    contador_ordenes = 0

    def __init__(self, telefonos):
        Orden.contador_ordenes += 1
        self._id_ordenes = Orden.contador_ordenes
        self._telefonos = telefonos

    @property
    def id_ordenes(self):
        return self._id_ordenes
    @id_ordenes.setter
    def id_ordenes(self, id_ordenes):
        self._id_ordenes = id_ordenes

    @property
    def telefonos(self):
        return self._telefonos
    @telefonos.setter
    def telefonos(self, telefonos):
        self._telefonos = telefonos

    def __str__(self):
        telefonos_str = ''
        for telefono in self._telefonos:
            telefonos_str += telefono.__str__()
        return f'''
            Orden: {self.contador_ordenes}
            Telefono: {telefonos_str}
'''
    
funda = Funda('Gorilla', 'Piel')
cargador = Cargador('Apple', 20)
celular = Celular(cargador, funda, 'Apple', 'iPhone 13 Pro')

funda = Funda('CaseFity', 'Piel')
cargador = Cargador('Apple', 30)
celular1 = Celular(cargador, funda, 'Apple', 'iPhone 14 Pro')

telefonos1 = [celular, celular1]
orden1 = Orden(telefonos1)
print(orden1)