class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_detalles(self):
        print(f'Persona: {self.nombre} tiene {self.edad} años.')


Persona1 = Persona('Luis', 23)
Persona2 = Persona('Maria', 34)
Persona2.mostrar_detalles()
