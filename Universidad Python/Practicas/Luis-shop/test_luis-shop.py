from Modulo.Productos import *
from Servicio.Carrito import *

opcion = None

while opcion != 4:
    try:
            opcion = int(input('''
Elige una opción:
1) Agregar producto al carrito
2) Mostrar contenido del carrito
3) Eliminar productos del carrito
4) Salir

'''))
            
            if opcion == 1:
                producto = input('¿Qué producto quieres agregar? ')
                Carrito.agregar_producto(producto)
            elif opcion == 2:
                Carrito.listar_productos()
            elif opcion == 3:
                Carrito.eliminar_productos()
            else:
                print(f'La opción {opcion} no existe')

    except TypeError as te:
        print(f'Tu opción debe de ser un numero.')
    except Exception as e:
        print(f'Error: {e}')

else:
    print('Saliendo del carrito...')      