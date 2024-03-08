# Creación de una clase básica:
# Define una clase llamada Persona con atributos como nombre, edad y sexo. Luego, instancia varios objetos de esta clase y muestra sus atributos.

class Persona:
    def __init__(self, nombre, edad, sexo):
        self._nombre = nombre
        self._edad = edad
        self._sexo = sexo

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

    @property
    def sexo(self):
        return self._sexo
    @sexo.setter
    def sexo(self, sexo):
        self._sexo = sexo

    def mostrar_atributos(self):
        return f'''
{self._nombre}
{self._edad}
{self._sexo}
'''
    
Persona1 = Persona('Luis', 23, 'Masculino')
Persona2 = Persona('Mara', 20, 'Femenino')
print(Persona1.mostrar_atributos())
print(Persona2.mostrar_atributos())