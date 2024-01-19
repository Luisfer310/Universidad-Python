def iterar_diccionario(**n):
    for clave, valor in n.items():  # Importante: Recordar que como usamos diccionarios, debemos de agregar el metodo de
        # items, keys o values dependiendo el caso
        print(f'{clave}: {valor}')


diccionario = {'IDE': 'Integrated Development Environment'}
iterar_diccionario(**diccionario)  # En el caso de los *args no necesite poner los asteriscos pero en los **kwargs si
# lo tuve que poner al crear el diccionario por fuera pero el profesor creo el diccionario dentro de la llamada de la
# funcion y no necesito poner los 2 asteriscos, seria asi...
iterar_diccionario(IDE='Integrated Development Environment')  # En este podemos notar que la clave no ira entre comillas
# y en lugar de usar los 2 puntos usaremos el signo de igual para dar el valor
