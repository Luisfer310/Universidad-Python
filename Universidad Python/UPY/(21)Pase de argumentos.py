# Definir una función con argumentos sin usarlos
def mi_funcion(nombre, apellido):
    print('Saludos desde mi función')


# Llamar a la funcion sin pasar argumentos
# mi_funcion()
# Llamar funcion pasando los argumentos y no se usaran
mi_funcion('Luis', 'Osuna')


# Definir funcion usando los argumentos
def mi_funcion2(nombre, apellido):
    print(f'Saludos {nombre} {apellido}')


# Llamando funcion sin pasar argumentos
# mi_funcion2()
# Llamando funcion pasando los argumentos
mi_funcion2('Luis', 'Osuna')
