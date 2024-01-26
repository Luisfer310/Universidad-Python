class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def mostrar_detalle(self):
        return f'Nombre: {self._nombre} \nEdad: {self._edad}'


# Para que no aparezca el llamado de la hoja principal en la hoja donde importamos el modulo se usara una estructura
# condicional de __name__
if __name__ == '__main__':
    Persona0 = Persona('Juan', 23)
    print(Persona0.mostrar_detalle())