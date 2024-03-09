class Persona:
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre=nombre
    
    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido=apellido

    def __str__(self):
        return f'{self._nombre} se apellida {self._apellido}'
    
class Empleado(Persona):
    def __init__(self, nombre, apellido, puesto):
        super().__init__(nombre, apellido)
        self._puesto = puesto

    @property
    def puesto(self):
        return self._puesto
    @puesto.setter
    def puesto(self, puesto):
        self._puesto = puesto

    def __str__(self):
        return f'{super().__str__()} y tiene el puesto de {self._puesto}'

Empleado1 = Empleado('Luis', 'Osuna', 'Developer')
print(Empleado1)