class Forma:
    def __init__(self, color, textura):
        self.__color = color
        self.__textura = textura

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def textura(self):
        return self.__textura
    
    @textura.setter
    def textura(self, textura):
        self.__textura = textura

    def caracteristicas(self):
        return f'Tu forma es de color {self.__color} con una textura de {self.__textura}'
    
class Cuadro(Forma):
    def __init__(self, color, textura, lado):
        super().__init__(color, textura)
        self.__lado = lado

    @property
    def lado(self):
        return self.__lado
    
    @lado.setter
    def lado(self, lado):
        self.__lado = lado

    def calcular_area(self):
        return f'Area del cuadrado: {self.__lado * self.__lado}'
    
Cubo1 = Cuadro('Rojo', 'Madera', 5)
print(Cubo1.calcular_area())
print(Cubo1.caracteristicas())