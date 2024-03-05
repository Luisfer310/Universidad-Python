from Teclado import *
from Raton import *
from Monitor import *
from Computadora import *
from Orden import *

teclado = 'Redragon'
raton = 'Apple'
monitor = 'Samsung'
nombre = 'Macbook Pro'
computadora1 = Computadora(nombre, monitor, teclado, raton)

teclado = 'HP'
raton = 'Ryzen'
monitor = 'Samsung'
nombre = 'Macbook Air'
computadora2 = Computadora(nombre, monitor, teclado, raton)

Orden1 = Orden([computadora1, computadora2])
print(Orden1)