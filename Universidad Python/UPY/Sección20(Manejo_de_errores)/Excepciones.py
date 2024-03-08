try:
    numero1 = int(input('Dame el primer numero: '))
    numero2 = int(input('Dame el segundo numero: '))

    resultado = numero1 / numero2
    print(f'El resultado es {resultado}')

except ZeroDivisionError as zde:
    print(f'No se puede dividir por 0. (Tipo de error: {zde})')
except TypeError as te:
    print(f'El dato ingresado no es numerico. (Tipo de error: {te})')
except Exception as e:
    print(f'Ocurrio un error inesperado. (Tipo de error: {e})')

# Las variables, si se crean dentro del bloque de try, solo se podran usar dentro de este. Para poder usarlas fuera, se deben crear antes del bloque try fuera del bloque.
resultado1 = None

try:
    num1 = int(input('Numero 1: '))
    num2 = int(input('Numero 2: '))

    resultado1 = num1/num2
except ZeroDivisionError as zde:
    print(f'El numero 0 no es divisible. (Tipo de error: {zde})')
except TypeError as te:
    print(f'El dato ingresado no es numerico. (Tipo de error: {te})')
except Exception as e:
    print(f'Ocurrio un error inesperado. (Tipo de error: {e})')

print(resultado1)