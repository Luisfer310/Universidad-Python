# Tienda de libros
print('Proporcione los siguientes datos del libro: ')
nombre = input('Proporcione el nombre: ')
idLibro = int(input('Proporcione el ID del libro: '))
precio = float(input('Proporcione el precio: '))
envio = input('Indica si el envio es gratuito (True/False): ')

print(f'Nombre: {nombre}')
print(f'ID: {idLibro}')
print(f'Precio: {precio}')
if envio == 'True':
    print('El envio es gratuito?: True')
elif envio == 'False':
    print('El envio es gratuito?: False')
else:
    print('Dato erroneo, dame un dato correcto')
