class Persona:
    pass


print(type(Persona))

class Nombres:
    pass


Victor = Nombres()
Luis = Nombres()

Victor.edad = 20
Luis.edad = 24

print(Victor.edad)

# Uso de init
class Persona2:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


persona = Persona2('Luis', 23)
print(persona.nombre)
print(persona.edad)
