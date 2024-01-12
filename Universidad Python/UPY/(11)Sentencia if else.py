# Condicionales Vacias y con valor
condicion = 5

if condicion:
    print('Condicion valida')
else:
    print('No condicion valida')

condicion2 = 'Hola'

if condicion2:
    print('Condicion valida')
else:
    print('No condicion valida')

condicion3 = ''

if condicion3:
    print('Condicion valida')
else:
    print('No condicion valida')

# condicion4 = 

# if condicion4:
#     print('Condicion valida')
# else:
#     print('No condicion valida')
# Al correr este programa veremos que las condiciones 1,2 y 3 correran pero solo la condicion3 se ira por la sentencia else y la condicion4 marcara error.
    
# Simplificación de la sintaxis
condicion = 5
print('Condicion valida') if condicion else print('No condicion valida')