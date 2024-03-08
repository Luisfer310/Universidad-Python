# Crea una clase llamada Calculadora con métodos estáticos para sumar, restar, multiplicar y dividir. También puedes implementar un método de clase para realizar cálculos más complejos.

class Calculadora:
    def __init__(self, *args):
        self._numeros = args
        self._resultado = 0

    def sumar(self):
        for numero in self._numeros:
            self._resultado += numero
        return self._resultado
    
    def restar(self):
        for numero in self._numeros:
            self._numeros -= numero
            return self._resultado
        return self._resultado
    
    def multiplicar(self):
        for numero in self._numeros:
            self._numeros *= numero
            return self._resultado
        return self._resultado
    
operacion = Calculadora(5,10,15,20)
print(operacion.sumar())