# class Persona:
#     def __init__(self, nombre, edad):
#         self._nombre = nombre
#         self._edad = edad
#
#     def __str__(self):
#         return f'Persona: (Nombre: {self._nombre}, Edad: {self._edad})'
#
#
# Persona0 = Persona('Jose',25)
# print(Persona0)

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def __str__(self):
        return f'Persona: Nombre {self._nombre}, Edad {self._edad}.'

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo
    def __str__(self):
        return f'{super().__str__()} y tiene un sueldo de {self._sueldo}'

Empleado0 = Empleado('Jose', 34, 6000)
print(Empleado0)
