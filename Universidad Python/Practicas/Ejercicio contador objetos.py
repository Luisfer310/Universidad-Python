class Persona:
    contador_persona = 0
    def __init__(self, nombre, edad):
        self._id = self._generar_valor() # Anteriormente en lugar de este atributo, lo que hacia era hacer una suma de unidades a la variable de clase: Persona.contador_persona += 1
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @staticmethod
    def metodo_estatico():
        return Persona.contador_persona
    
    @classmethod
    def metodo_clase(cls):
        return f'{cls.contador_persona} son las personas que se crearon'
    
    @classmethod
    def _generar_valor(cls): # Defini este metodo de clase supliendo a la incrementacion en el constructor de objeto al principio del codigo, de esta forma cuando lo llame hara un incremento y no solo cuando cree una instancia
        cls.contador_persona += 1 # Aqui se genera el incremento
        return cls.contador_persona # Y aqui se retorna el valor total despues del incremento de la variable

    def __str__(self):
        return(f'El ID para el usuario {self._nombre} de {self._edad} años, es el ID: {self._id}')
    
Persona1 = Persona('Luis', 23)
Persona2 = Persona('Mara', 20)
print(Persona.metodo_estatico())
print(Persona1.metodo_clase())
print(Persona2)