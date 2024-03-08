# Diseña una clase llamada Forma con un método calcular_area() y un método calcular_perimetro(). Luego, crea subclases como Cuadrado, Círculo y Triángulo, implementando los métodos correspondientes
# para cada forma geométrica.

from abc import ABC, abstractclassmethod

class Forma(ABC):
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho
    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto
    @alto.setter
    def alto(self, alto):
        self._alto = alto

    @abstractclassmethod
    def calcular_area(self):
        pass

class Cuadrado(Forma):
    def __init__(self, lado):
        super().__init__(lado, lado)
        self._lado = lado

    @property
    def lado(self):
        return self._lado
    @lado.setter
    def lado(self, lado):
        self._lado = lado

    def calcular_area(self):
        area = self._lado * self._lado
        return area
    
class Rectangulo(Forma):
    def __init__(self, ancho, alto):
        super().__init__(ancho, alto)
        self._ancho = ancho
        self._alto = alto

    def calcular_area(self):
        area = self._ancho * self._alto
        return area

Cuadrado1 = Cuadrado(5)
print(Cuadrado1.calcular_area())

Rectangulo1 = Rectangulo(5, 10)
print(Rectangulo1.calcular_area())