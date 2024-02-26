# # En una estructura mas robusta, veremos en los argumentos datos de cualquier tipo
# class Persona:
#     def __init__(self, nombre, apellido, edad, *args, **kwargs):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.edad = edad
#         self.args = args
#         self.kwargs = kwargs

#     def metodo(self):
#         print(f'Persona {self.nombre} {self.apellido} con la edad de {self.edad} años, agrego una tupla {self.args} un diccionario {self.kwargs}')


# nombre0 = input('Ingrese su nombre por favor: ')
# apellido0 = input('Ingrese su apellido por favor: ')
# edad0 = input('Ingrese su edad: ')
# Persona0 = Persona(nombre0, apellido0, edad0, 35, 67, 'Hola mundo', m='Manzana', p='Pera')
# Persona0.metodo()

class Persona:
    def __init__(self, nombre, apellido, edad, *args, **kwargs):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__args = args
        self.__kwargs = kwargs
    
    def mostrar_detalles(self):
        return f'El usuario {self.__nombre} {self.__apellido}, con {self.__edad} años agrego la tupla: {self.__args} y un diccionario: {self.__kwargs}'
    
nombre = input('Agrega tu nombre: ')
apellido = input('Dame tu apellido: ')
edad = input('¿Cuantos años tienes? ')

Persona0 = Persona(nombre,apellido, edad, 24, 31, 'Hola', 'Manzana', a=1, b=2) # Python sabe cuando ya se pasaron los parametros duros (en este caso es nombre, apellido, edad) y despues de estos tomara como *args
# todos los valores que no tengan sintaxis de diccionario, pero una vez encuentre un valor en sintaxis de diccionario este pasara al parametro **kwargs, la sintaxis de estos aqui cambia un poco, en lugar de
# separar las claves de valores con dos puntos se hara con un signo de asignacion y la clave no debe de llevar comillas
print(Persona0.mostrar_detalles())