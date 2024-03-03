from Producto import *

class Orden:
    contador_ordenes = 0
    
    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos_lista = list(productos)

    def agregar_productos(self, producto):
        self._productos_lista.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self._productos_lista:
            total += producto.precio
        return total
    
    def __str__(self):
        productos_str = '' # Esta variable sera temporal para que guarde cada producto en ella en el ciclo for
        for producto in self._productos_lista: # Por cada producto en la lista de productos
            productos_str += str(producto) + '\n' # Se le concatenara a la variable temporal el elemento repasado en el ciclo y lo convertira en str
        return f'Tu orden {self._id_orden}, tiene los productos: \n{productos_str} \nY da un total de ${self.calcular_total()}' # Se utiliza 'productos_str' por que esta variable guarda los elementos del objeto
    
if __name__ == '__main__':
    Producto1 = Producto('Blusa', 250.00)
    Producto2 = Producto('Falda', 450.00)
    Producto3 = Producto('Sueter', 500.00)
    Orden1 = Orden([Producto1, Producto2, Producto3])
    print(Orden1)