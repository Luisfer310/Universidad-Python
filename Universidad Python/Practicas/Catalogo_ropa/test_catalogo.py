from Dominio.Prenda import *
from Servicio.Catalogo_prenda import CatalogoPrendas as cp

opcion = None

while opcion != 4:
    opcion = int(input('''
Elige la opción deseada:
1) Agregar prenda
2) Listar prendas
3) Eliminar archivo de peliculas
4) Salir

'''))
    
    if opcion == 1:
        prenda = input('¿Qué prenda deseas agregar? ')
        prenda = Prenda(prenda)
        cp.agregar_prenda(prenda)
    elif opcion == 2:
        cp.listar_prendas()
    elif opcion == 3:
        cp.eliminar()
else:
    print('Salimos del programa...')