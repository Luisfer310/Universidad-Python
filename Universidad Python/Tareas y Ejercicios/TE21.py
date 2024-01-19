# Crear una función para sumar los valores recibidos de tipo numérico, utilizando argumentos variables como parámetro de
# la función y regresar como resultado la suma de todos los valores pasados como argumentos.

# Esta primera forma seria usando el recorrido de los argumentos y creando una variable en la que se
# ira sumando cada numero.
def suma(*numeros):
    suma_num = 0
    for num in numeros:
        suma_num += num
    return suma_num


print(suma(1, 2, 3, 4, 5, 6, 7, 8, 9))

# En esta otra forma la descubri mientras estaba haciendo la forma anterior.
def suma2(*numeros):
    return sum(numeros)  # Esta funcion hace la funcion de sumar todo lo que este dentro de los parentesis, esto lo
    # vere mas adelante pero es usar funciones dentro de funciones.


print(suma2(1, 2, 3, 4, 5, 6, 7, 8, 9))
