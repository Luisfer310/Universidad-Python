# Estructura de *args
def alumnos(*nombres):
    for nombre in nombres:
        print(nombre)


alumnos('Luis', 'Itzel', 'Danna', 'Karina', 'Mara')
