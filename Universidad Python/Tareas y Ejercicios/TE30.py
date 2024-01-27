# Definicion de la clase padre
class Vehiculo:
    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas

    def __str__(self):
        return f'Vehiculo color {self._color}, ruedas {self._ruedas}'

# Definicion de la clase hija coche
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self._velocidad = velocidad

    def __str__(self):
        return f'{super().__str__()}, tiene una velocidad de {self._velocidad} km/hr.'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self._tipo = tipo

    def __str__(self):
        return f'{super().__str__()} es para {self._tipo}'


Vehiculo0 = Vehiculo('Azul', 'Grandes')
Coche0 = Coche('Rojo', 'Medianas',250)
Bicicleta0 = Bicicleta('Negra', 'Doble Rodado', 'Montaña')
print(Vehiculo0)
print(Coche0)
print(Bicicleta0)
