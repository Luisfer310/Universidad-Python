# En este programa se bloqueara los atributos de la clase para que no se pueda acceder a ellos desde afuera
class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.__nombre = nombre
        self.__edad = edad  # Poniendo 2 guiones bajos despues del punto, 'bloqueamos' los atributos, de esta forma encapsulamos las clases
        self.__ciudad = ciudad

    def mostrar_detalles(self):
        return f'{self.__nombre} de {self.__edad} años, vive en {self.__ciudad}'
    
Persona1 = Persona('Luis', 23, 'Culiacán')
print(Persona1.mostrar_detalles())

# A pesar de lo que queremos es bloquear las clases para que no se tenga acceso a ellas fuera de estas, se puede agregar nuevos atributos a una clase fuera de esta, pero solo se agregara en el objeto en el que se indico
Persona2 = Persona('Mara', 20, 'Mazatlan')
Persona1.__telefono = 6672919394
print(Persona2.mostrar_detalles())
print(Persona1.__telefono)
# print(Persona2.__telefono) # Como el atributo se creo en el objeto de persona1, en este objet o no existe, asi que lanzara error

class Persona1:
    def __init__(self, nombre, edad, color):
        self.__nombre = nombre
        self.__edad = edad
        self.__color = color

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def mostrar_perosona(self):
        return f'La persona {self.__nombre} tiene {self.__edad} años y le gusta el color {self.__color}'
    
PersonaA = Persona1('Luis', 23, 'Verde')
print(PersonaA.mostrar_perosona())
print(PersonaA.nombre) # Muy importante recoradar que al querer acceder a nuestros metodos get y set no se debe de poner los parentesis, al contrario como lo hariamos en otros metodos, por ejemplo en el anterior.
PersonaA.nombre = 'Fernando' # En este accesara al metodo de set, para poder cambiar un atributo
print(PersonaA.nombre)

# Podemos hacer que un atributo sea solo lectura y no modificarlo, es sencillo, se debe solo de escribir el metodo get, sin el setter.
class Persona2:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre
    
    def mostrar_detalles(self):
        return f'El usuario {self.__nombre} tiene {self.__edad} años'
    
PersonaB = Persona2('Luis', 23)
print(PersonaB.mostrar_detalles())
print(PersonaB.nombre)