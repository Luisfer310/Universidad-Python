class FiguraGeometrica:
    def __init__(self, alto, ancho):
        if 0 < ancho < 10:
            self._ancho = ancho
        else:
            self._ancho = 0
        if 0 < alto < 10:
            self._alto = alto
        else:
            self._alto = 0

    def __str__(self):
        return f'La figura tiene un alto de {self._alto} y un ancho de {self._ancho}'

    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self, alto):
        if 0 < alto < 10:
            self._alto = alto

    @property
    def ancho(self):
        return self._ancho
    
    @ancho.setter
    def ancho(self, ancho):
        if 0 < ancho < 10:
            self._ancho = ancho

class Color:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
        
    def area(self):
        return self._ancho * self._alto
    
    def __str__(self):
        return f'Los valores son: Lado {self._alto}'
    
class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)
        
    def area(self):
        return self._ancho * self._alto
    
    def __str__(self):
        return f'Los valores son: alto({self._alto}), ancho({self._ancho})'
    
Cuadrado1 = Cuadrado(5, 'Verde')
print(Cuadrado1)
Rectangulo1 = Rectangulo(5,10, 'Azul')
print(Rectangulo1)

print('Calcular area'.center(40, '-'))

print(f'Area del cuadrado: {Cuadrado1.area()}')
print(f'Area del rectangulo: {Rectangulo1.area()}')