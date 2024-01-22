# Definición de la clase con los atributos ancho, alto y profundidad
class Cubo:
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho * self.alto * self.profundidad


ancho1 = float(input('Ingrese el valor del ancho: '))
alto1 = float(input('Ingrese el valor del alto: '))
profundidad1 = float(input('Ingrese el valor de profundidad: '))
cubo1 = Cubo(ancho1, alto1, profundidad1)
print(cubo1.calcular_volumen())
