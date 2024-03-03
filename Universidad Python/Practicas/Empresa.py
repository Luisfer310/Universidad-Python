# from abc import ABC, abstractclassmethod
# class Persona(ABC):
#     def __init__(self, nombre, edad):
#         self._nombre = nombre
#         self._edad = edad

#     @property
#     def nombre(self):
#         return self._nombre
#     @nombre.setter
#     def nombre(self, nombre):
#         self._nombre = nombre

#     @property
#     def edad(self):
#         return self._edad
#     @edad.setter
#     def edad(self, edad):
#         self._edad = edad

#     def __str__(self):
#         return f'La persona {self._nombre} tiene {self._edad} años'
    
#     @abstractclassmethod
#     def mostrar_detalles(self):
#         pass

# class Puesto(ABC):
#     def __init__(self, puesto):
#         self._puesto = puesto

#     @property
#     def puesto(self):
#         return self._puesto
#     @puesto.setter
#     def puesto(self, puesto):
#         self._puesto = puesto

#     def __str__(self):
#         return f'El puesto {self._puesto}'
    
    
#     @abstractclassmethod
#     def mostrar_empleo(self):
#         pass

# class Empleado(Persona, Puesto):
#     contador = 0
#     def __init__(self, nombre, edad, puesto, sueldo):
#         Persona.__init__(self, nombre, edad)
#         Puesto.__init__(self, puesto)
#         self._sueldo = sueldo
#         Empleado.contador += 1

#     @property
#     def sueldo(self):
#         return self._sueldo
#     @sueldo.setter
#     def sueldo(self, sueldo):
#         self._sueldo = sueldo

#     def mostrar_detalles(self):
#         print(f'El empleado {self._nombre} tiene {self._edad} años y tiene el puesto de {self._puesto} con una paga de {self._sueldo}')

#     def mostrar_empleo(self):
#         print(f'Tienes el empleo de {self._puesto}')

# Empleado1 = Empleado('Luis', 23, 'Developer web', 2500)
# Empleado1.mostrar_detalles()
# Empleado1.mostrar_empleo()
# print(Empleado.contador)

from abc import ABC, abstractmethod
class Miclase(ABC):
		variable = 'Hola'

		def __init__(self, nombre, ciudad):
				self._nombre = nombre
				self._ciudad = ciudad

		@property
		def nombre(self):
				return self._nombre
		@nombre.setter
		def nombre(self, nombre):
				self._nombre = nombre

		@property
		def ciudad(self):
				return self._ciudad
		@ciudad.setter
		def ciudad(self, ciudad):
				self._ciudad = ciudad

		@staticmethod
		def saludo():
				print('Hola')

		@classmethod
		def saludo_clase(cls):
				print(f'Ingresando a variable desde classmethod: {cls.variable}')

		def metodo_instancia(self):
				self.saludo()
				self.saludo_clase()
				print(self.variable)
				
objeto = Miclase('Luis', 'Maza')
objeto.metodo_instancia()
objeto.saludo()
objeto.saludo_clase()