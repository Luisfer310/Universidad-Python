from Accesorios import *
from Funda import *
from Teclado import *
from iPads import *

class Orden:
    contador_ordenes = 0

    def __init__(self, ipads):
        Orden.contador_ordenes += 1
        self._id_ipads = Orden.contador_ordenes
        self._ipads = ipads

    def agregar_ipad(self, ipad):
        self._ipads.append(ipad)

    def __str__(self):
        ipad_str = ''
        for ipad in self._ipads:
            ipad_str += ipad.__str__() + '\n'
        return f'''
            Orden #{self._id_ipads}
            {ipad_str}
'''
    
funda = Funda('Mobo', 'Silicon')
teclado = Teclado('Redragon', 'Español')
ipad = Ipads('Air 5', funda, teclado)
orden = Orden([ipad])
print(orden)

funda = Funda('Mobo', 'Silicon')
teclado = Teclado('Redragon', 'Español')
ipad1 = Ipads('Air 4', funda, teclado)
orden = Orden([ipad, ipad1])
print(orden)