class Persona:
    def __init__(self, nombre, edad, color):
        self.__nombre = nombre
        self.__edad = edad
        self.__color = color

    def mostrar_detalles(self):
        return f'{self.__nombre} tiene {self.__edad} años y le gusta el color {self.__color}'
    
if __name__ == '__main__': # Esta condicional se ejecuta solo si se encuentra en el modulo principal, para que en otros modulos que llamen a este no se ejecute las llamadas y objetos de esta hoja
    Persona1 = Persona('Luis', 23, 'Azul')
    print(Persona1.mostrar_detalles())