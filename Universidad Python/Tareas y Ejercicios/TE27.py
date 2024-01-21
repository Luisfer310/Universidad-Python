# Crear una clase para el objeto de la resta
class Operandos:
    def __init__(self, operando_a, operando_b):
        self.operando_a = operando_a
        self.operando_b = operando_b

    def resta(self):
        return self.operando_a - self.operando_b


# En este caso le agregue un input para hacerlo mas interactivo
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
OperacionResta = Operandos(numero1, numero2)
print(OperacionResta.resta())
