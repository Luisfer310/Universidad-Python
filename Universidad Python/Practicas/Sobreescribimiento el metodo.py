# Sobreescritura de un metodo, ayudara en que enseñar si el objeto se llama solo por su nombre y no se pasa ningun metodo. Sin este metodo se sobreescritura solo nos mostraria el espacio de la memoria donde se almacena la clase
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def detalles(self):
        return f'El usuario {self._nombre} tiene {self._edad} años'
    
    def __str__(self):
        return f'Nombre {self._nombre}, edad {self._edad}'
    
Persona1 = Persona('Luis', 23)
print(Persona1)

# Si queremos heredar los atributos de esta clase a una clase hija, y la clase tiene un atributo propio, el metodo de sobreescritura no del padre no lo tendra por lo cual lo no pintara. Para esto debemos heredar este metodo al hijo, pero agregando el atributo adicional
class Empleado(Persona):
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)
        self._puesto = puesto
    
    def detalles(self):
        return f'El usuario {self._nombre} tiene {self._edad} años y es empleado en el puesto {self._puesto}' # Debo de investigar mas sobre esto de las herencias, pero parece ser que cuando quiero llamar los atributos hederados se debe de especificar la clase en el llamado del atributo (esto sera solo si los atributos se encapsulan con doble guin bajo)
    
    def __str__(self):
        return f'{super().__str__()} {self._puesto}'
    
Empleado1 = Empleado('Luis', 23, 'Desarollador back-end')
print(Empleado1)
print(Empleado1.detalles())

# class Persona:
# 	def __init__(self, nombre, edad):
# 		self._nombre = nombre
# 		self._edad = edad

# 	def __str__(self):
# 		return f'Persona: Nombre {self._nombre}, Edad {self._edad}.'

# class Empleado(Persona):
# 	def __init__(self, nombre, edad, sueldo):
# 		super().__init__(nombre, edad)
# 		self._sueldo = sueldo

# 	def __str__(self):
# 		return f'{super().__str__()} y tiene un sueldo de {self._sueldo}'

# Empleado0 = Empleado('Jose', 34, 6000)
# print(Empleado0)