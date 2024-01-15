frutas = ('Manzana', 'Mango', 'Pera', 'Uva')

for n in frutas:
    if n == frutas[-1]:
        print(n, end='.')
    else:
        print(n, end=', ')
