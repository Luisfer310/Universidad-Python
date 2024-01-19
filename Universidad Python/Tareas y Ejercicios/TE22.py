# Crear una función para multiplicar los valores recibidos de tipo numérico, utilizando argumentos variables como
# parámetro de la función y regresar como resultado la multiplicación de todos los valores pasados como argumentos.

# Usando la iteracion de los argumentos
def multiplicacion(*numeros):
    resultado = 1  # Importante: Si es multiplicacion se debe de inicar en uno para que al multiplicar el primer arg de
    # como resultado este mismo, por que si es en 0 el resultado sera 0. 
    for numero in numeros:
        resultado *= numero
    return resultado


print(multiplicacion(2, 3, 2))
