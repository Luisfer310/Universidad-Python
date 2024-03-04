# a = 3
# b = 7
# print(a + b)

# a = '3'
# b = '7'
# print(a + b)

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def __add__(self, otro):
        return f'{self._nombre} {otro._nombre}'
    
    def __sub__(self, otro):
        return f'{self._edad} {otro._edad}'
objeto1 = Persona('Luis', 23)
objeto2 = Persona('Mara', 45)
print(objeto1 - objeto2)
print(objeto1 + objeto2)