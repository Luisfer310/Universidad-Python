from abc import ABC, abstractclassmethod
class Persona(ABC):
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @abstractclassmethod
    def mostrar_detalles(self):
        pass

    def __str__(self):
        return f'{self._nombre} tiene {self._edad} años'
    
class Empleado(Persona):
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)
        self._puesto = puesto

    @property
    def puesto(self):
        return self._puesto
    @puesto.setter
    def puesto(self, puesto):
        self._puesto = puesto

    def mostrar_detalles(self):
        return f'{super().__str__()} y tiene el puesto de {self._puesto}'
    
    def __str__(self):
        return f'Puesto: {self._puesto}'

def imprimir_detalles(objeto):
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Empleado):
        print('Este objeto, viene de la clase Empleado')

objeto1 = Empleado('Luis', 23, 'Developer')
imprimir_detalles(objeto1)
print(objeto1)

