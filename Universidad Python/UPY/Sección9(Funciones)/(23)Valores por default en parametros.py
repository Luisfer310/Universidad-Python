# Definir una fn con parametros por default sin pasar argumentos
def suma(num1=0, num2=0):
    return num1 + num2


print(suma())

# Ahora se pasaran argumentos que funcionaria normal aun que le pongamos parametros por default
print(suma(3, 7))
