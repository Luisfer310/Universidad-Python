# Definire la clase padre
class Persona:
    def __init__(self, nombre , edad):
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
    def edad(self,edad):
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Persona: {self._nombre} tiene {self._edad} años.')

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    def mostrar_detalles(self):
        print(f'Empleado: {self._nombre} tiene {self._edad} años y ganas {self._sueldo} al mes.')


Persona0 = Persona('Jose', 23)
Empleado0 = Empleado('Jose', 23, 5000)
Persona0.mostrar_detalles()
Empleado0.mostrar_detalles()