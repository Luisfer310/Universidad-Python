frutas = ('Manzana', 'Mango', 'Pera', 'Uva')

for n in frutas:
    if n == frutas[-1]:
        print(n, end='.')
    else:
        print(n, end=', ')

# Tuplas de un solo elemento
fruta = ('Manzana',)
print(fruta)
# Convertir tuplas en listas para modificar elementos
frutaLista = list(fruta)
print(type(frutaLista))
frutaLista.append('Pera')
fruta = tuple(frutaLista)
print(type(fruta))
print(fruta)
