# Para que no aparezca el llamado de la hoja principal en la hoja donde importamos el modulo se usara una estructura
# condicional de __name__
from Persona import Persona

print('Importación del modulo principal'.center(45, '-'))
Persona1 = Persona('Fernando', 25)
print(Persona1.mostrar_detalle())

print('Destructor del objeto'.center(45, '-'))
del Persona1
# print(Persona1)
