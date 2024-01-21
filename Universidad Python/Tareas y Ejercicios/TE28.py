# Laboratorio rectangulo
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


base1 = float(input('Ingrese la medida de la base del rectangulo: '))
altura2 = float(input('Ingrese la medida de la altura del rectangulo: '))
AreaRectangulo = Rectangulo(base1, altura2)
print(AreaRectangulo.calcular_area())
