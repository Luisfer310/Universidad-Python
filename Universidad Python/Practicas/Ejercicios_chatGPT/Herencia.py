# Herencia:
# Crea una clase base llamada Vehiculo con propiedades como marca, modelo y año, y métodos como obtener_informacion. Luego, crea subclases como Automovil y Motocicleta, que hereden de Vehiculo y tengan propiedades
# y métodos específicos.

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self._marca = marca
        self._modelo = modelo
        self._año = año

    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    @property
    def año(self):
        return self._año
    @año.setter
    def año(self, año):
        self._año = año

    def obtener_informacion(self):
        print(f'El vehiculo {self._marca} {self._modelo} es del año {self._año}')

carro = Vehiculo('Ferrari', 'Enzo', 2023)
carro.obtener_informacion()