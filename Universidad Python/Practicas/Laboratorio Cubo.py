# Se desarrollara un programa para calcular el volumen de un cubo. Para esto se le pedira al usuario el ancho, profundo y alto del cubo. Crearemos la clase Cubo y dentro de esta escribiremos un metodo para
# calcular el volumen con la ecuacion ancho*profundo*alto.
class Cubo:
    def __init__(self, ancho, profundo, alto):
        self.__ancho = ancho
        self.__profundo = profundo
        self.__alto = alto

    def calcular_volumen(self):
        return self.__ancho * self.__profundo * self.__alto

ancho = int(input('Ancho: '))
profundo = int(input('Profundidad: '))
alto = int(input('Altura: '))    
Cubo1 = Cubo(ancho, profundo, alto)
print(f'{Cubo1.calcular_volumen()} m3') 