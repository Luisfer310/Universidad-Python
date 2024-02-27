class Color:
    def __init__(self, color):
        self._color = color

class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

class Cuadrado(Color, FiguraGeometrica):
    def __init__(self, color, lado):
        Color.__init__(self, color)
        FiguraGeometrica.__init__(self, lado, lado)
        
    def calcular(self):
        return self._ancho * self._alto
    
Cuadro1 = Cuadrado('Azul', 5)
print(Cuadro1.calcular())