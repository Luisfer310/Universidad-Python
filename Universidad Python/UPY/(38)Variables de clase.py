class Persona:
    variable = 'Hola persona'

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

    @staticmethod
    def metodo_estatico():
        return Persona.variable
    
    @classmethod
    def metodo_clase(cls):
        return cls.variable

Persona1 = Persona('Luis', 23)
print(Persona1.variable)
print(Persona.variable)
Persona.variable2 = 'Hola Persona 2' # Creacion de una variable de clase al vuelo
print(Persona.variable2)
print(Persona1.variable2)
print(Persona.metodo_estatico())
print(Persona.metodo_clase())
print(Persona1.metodo_clase())