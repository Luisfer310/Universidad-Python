# Importar clase y decorador de ABC(Abstract Base Class)
from abc import ABC, abstractmethod

# Definición de la clase abstracta
class FiguraGeometrica(ABC): # Con esta clase padre dentro de esta clase, haremos que la clase sea abstracta y podamos usar el decorador de abstract
    def __init__(self, ancho, alto):
        if 0 < ancho < 11:
            self._ancho = ancho
        else:
            self._ancho = 0
            print(f'El valor de ancho no esta en el rango de 0 a 10')
        
        if 0 < alto < 11:
            self._alto = alto
        else:
            self._alto = 0
            print(f'El valor de alto no esta en el rango de 0 a 10')

    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, ancho):
        if 0 < ancho < 11:
            self._ancho = ancho

    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self, alto):
        if 0 < alto < 11:
            self._alto = alto

    @abstractmethod
    def calcular_area(self): # Al esta ser una clase abstracta no tendra instancias asi que no podemos poner indicaciones dentro del metodo, solo haremos saber que las clases hijas deben de contar con este metodo.
        pass

class Rectangulo(FiguraGeometrica):
    def __init__(self,  ancho, alto):
        FiguraGeometrica.__init__(self, ancho, alto)

    def calcular_area(self): # Si comentamos estas lineas, podemos darnos cuenta de que nos dara un error el cual se provoca por que la clase hija no tendra el metodo abstracto que indica la clase padre y esta debe de ser obligatoria en las clases hijas de una clase abstracta
        return f'El area es: {self._ancho * self._alto}'
    
FiguraGeometrica.variable2 = 'Hola'
print(FiguraGeometrica.variable2)
Rectangulo1 = Rectangulo(6,11)
print(Rectangulo1.calcular_area())
Rectangulo1.alto = 12
print(Rectangulo1.calcular_area())