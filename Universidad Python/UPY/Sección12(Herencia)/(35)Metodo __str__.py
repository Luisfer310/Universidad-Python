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

# Metodo __str__ con encapsulamiento 'basico' (_)
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

# Metodo __str__ con encapsulamiento bloqueo (__)
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    def __str__(self):
        return f'Persona: Nombre {self._nombre}, Edad {self._edad}.'
    
    def detalles(self):
        return f'{self._nombre} tiene {self._edad} años'
    
class Empleado(Persona):
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)
        self._puesto = puesto

    def __str__(self):
        return f'{super().__str__()} {self._puesto}'
    
Empleado1 = Empleado('Luis', 23, 'Desarrollador web')
print(Empleado1)