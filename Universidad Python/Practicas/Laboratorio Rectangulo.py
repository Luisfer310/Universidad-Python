# Crear un programa que pida al usuario una altura y una base para un rectangulo y crear la clase del rectangulo que tenga el metodo de calcular el area
altura = int(input('Dame la altura: '))
base = int(input('Dame la base: '))

class Rectangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return f'El area es: {self.base * self.altura}'
    
Rectangulo1 = Rectangulo(altura, base)
print(Rectangulo1.calcular_area())