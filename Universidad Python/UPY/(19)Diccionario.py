# Declaracion de diccionario.
miDic = {'IDE': 'Integrated Development Environment', 'OOP': 'Object Oriented Programming'}
print(miDic)
# Acceder a al valor de una llave.
print(miDic['IDE'])
# Verificar si un elemento se encuentra dentro de el diccionario.
print('IDE' in miDic)  # Se podria usar la funcion .keys(), pero por defecto buscara primero en las claves.
# Verificar si un elemento se encuentra dentro de el diccionario en los valores.
print('Object Oriented Programming' in miDic.values())
# Evitar que me arroje el error al querer imprimir una calve
print(miDic.get('IA', 'No existe en el diccionario'))
# Recorrer las claves del diccionario
for calve in miDic.keys():
    print(calve)
# Recorrer los valores del diccionario
for valor in miDic.values():
    print(valor)
# Recorrer claves y valores por separados con el metodo .items()
for clave, valor in miDic.items():
    print(clave)
    print(valor)
# Ahora los 2 en una sola linea
for clave, valor in miDic.items():
    print(clave, valor)
# Modificacion de los valores
miDic['IDE'] = 'integrated development environment'
print(miDic)
# Agregar elemento a diccionario
miDic['PK'] = 'Primary Key'
print(miDic)
# Eliminar elemento de diccionario
miDic.pop('IDE')
print(miDic)
# Clear
miDic.clear()
print(miDic)
# Eliminar
del miDic
print(miDic)
