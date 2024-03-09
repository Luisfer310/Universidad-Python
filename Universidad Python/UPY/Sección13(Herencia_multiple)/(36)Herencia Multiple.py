# En una sola clase hija, podemos tener mas de una clase padre
class FiguraGeometrica:
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

class Color:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color

class Cuadro(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcular_area(self):
        return self._ancho * self._alto
    
Cuadro1 = Cuadro(5, 'Verde')
print(Cuadro1.calcular_area())