class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalles(self):
        return f'Persona: {self._nombre} {self._apellido} {self._edad}'


Persona0 = Persona('Luis', 'Osuna', 23)
Persona0.nombre = 'Fernando'
print(Persona0.nombre)
print(Persona0.mostrar_detalles())


# De esta forma usaremos el atributo read-only
class Persona1:
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    @property
    def nombre(self):
        return self._nombre

    def mostrar_detalles(self):
        print(f'Persona: {self._nombre} {self._apellido}')


Persona0 = Persona1('Jose', 'Olivas')
Persona0.mostrar_detalles()
