# En una estructura mas robusta, veremos en los argumentos datos de cualquier tipo
class Persona:
    def __init__(self, nombre, apellido, edad, *args, **kwargs):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def metodo(self):
        print(f'Persona {self.nombre} {self.apellido} con la edad de {self.edad} años, agrego una tupla {self.args} y '
              f'un diccionario {self.kwargs}')


nombre0 = input('Ingrese su nombre por favor: ')
apellido0 = input('Ingrese su apellido por favor: ')
edad0 = input('Ingrese su edad: ')
Persona0 = Persona(nombre0, apellido0, edad0, 35, 67, 'Hola mundo', m='Manzana', p='Pera')
Persona0.metodo()
