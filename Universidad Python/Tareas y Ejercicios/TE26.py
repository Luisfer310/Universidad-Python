# Creacion de la clase
class Operandos:
    def __init__(self, operando_a, operando_b):
        self.OperandoA = operando_a
        self.OperandoB = operando_b

    # Crearemos el metodo el cual sumara los operandos
    def sumar(self):
        return self.OperandoA + self.OperandoB


Operacion = Operandos(25, 4)
print(Operacion.sumar())
