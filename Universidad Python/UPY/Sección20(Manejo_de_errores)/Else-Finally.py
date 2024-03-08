resultado = None

try:
    num1 = int(input('Dame el primer numero para la operacion: '))
    num2 = int(input('Dame el segundo numero para la operacion: '))

    resultado = num1 / num2

except ZeroDivisionError as zde:
    print(f'No se puede dividir por 0. (Tipo de error: {zde})')
except TypeError as te:
    print(f'El dato ingresado no es numerico. (Tipo de error: {te})')
except Exception as e:
    print(f'Ocurrio un error inesperado. (Tipo de error: {e})')
else:
    print('El codigo se ejecuto sin errores.')
finally:
    print('Finalizo el codigo de excepciones.')

print(f'El resultado es: {resultado}')