class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} tiene {self.edad} años.')


Persona1 = Persona('Luis', 23)
Persona2 = Persona('Mara', 20)
Persona.mostrar_detalle(Persona1)

# Agregar atributos
Persona1.telefono = '6672919394'
print(Persona1.telefono)
# print(Persona2.telefono) en el caso de esta linea nos dara error por que el atributo solo se
# creo para el objeto persona1
