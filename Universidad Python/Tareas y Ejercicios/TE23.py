# Imprimir numeros de 5 a 1 de manera descendente usando funciones rcursivas.
# Puede ser cualquier tipo de valor positivo.
def numeros_desc(numero):
    if numero >= 1:
        print(numero)
        numeros_desc(numero - 1)


numeros_desc(5)
