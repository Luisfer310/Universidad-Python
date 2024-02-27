class Carro:
    def __init__(self, marca, modelo, color, rines):
        self.__modelo = modelo
        self.__color = color
        self.__marca = marca
        self.__rines = rines

    # Encapsulamiento de los atributos
    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def colors(self, color):
        self.__color = color

    @property
    def marca(self):
        return self.__marca
    
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def rines(self):
        return self.__rines
    
    @marca.setter
    def rines(self, rines):
        self.__marca = rines

    def mostrar_detalles(self):
        return f'El {self.__marca} modelo {self.__modelo} es color {self.__color} y tiene rines de {self.__rines}"'

# Accediendo a los atributos atraves de get y set
Carro1 = Carro('Ferrari', 'Spyder', 'Rojo', 36)
print(Carro1.mostrar_detalles())
modelo = Carro1.modelo
print(modelo)
color = Carro1.color
print(f'El color del carro es {color}')
