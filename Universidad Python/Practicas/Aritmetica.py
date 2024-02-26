# Se creara una clase con el nombre 'Aritmetica', la cual realizara las operaciones de sumar, restar, etc.
class Aritmetica:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def sumar(self):
        return self.a + self.b
    
    def restar(self):
        return self.a - self.b
    
    def multiplicar(self):
        return self.a * self.b
    
    def dividir(self):
        return self.a / self.b
    
Objeto1 = Aritmetica(27,5)
print(Objeto1.sumar())
print(Objeto1.restar())
print(Objeto1.multiplicar())
print(Objeto1.dividir()) # En este metodo, habra ocaciones que nos mostrara demasiados daecimilas, pero nosotros podemos indicar cuantos puntos floants queremos que nos muestre
print(f'{Objeto1.dividir():.2f}') # Asi podemos indicar cuantos decimales nos muestre