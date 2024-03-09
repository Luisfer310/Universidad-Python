# Para la creacion de clases de manejo de excepciones y errores, se recomienda que estas se creen en un modulo aparte, pero para un resumen mas corto, se definira en el mismo modulo...
class NumerosIguales(Exception):
    def __init__(self, mensaje):
        self._message = mensaje


# Ahora vamos a el codigo en el que se implementara el manejo de errores...
resultado = None

try:
    num1 = int(input('Dame el primer numero: '))
    num2 = int(input('Dame el segundo numero: '))

    if num1 == num2:
        raise NumerosIguales('Mira, los numeros son identicos')
    resultado = num1/num2

except ZeroDivisionError as zde:
    print(f'Error: {zde}, el numero 0 no es divisible')
except TypeError as te:
    print(f'Error: {te}, el valor ingresado no es numerico')
except Exception as e:
    print(f'Error: {e}')
else:
    print('El codigo se ejecuto sin errores')
finally:
    print('Fin de las excepciones')

print(f'El resultado es {resultado}')