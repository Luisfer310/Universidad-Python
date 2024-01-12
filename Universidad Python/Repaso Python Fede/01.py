# Ejercicios de Random

from random import *
numero_random = randint(1,10)
print(numero_random)

numeros = [1, 2, 3, 4, 5, 6]
numeros = choice(numeros)
print(numeros)

baraja = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
shuffle(baraja)
print(baraja)

numerox = random()
print(numerox)
