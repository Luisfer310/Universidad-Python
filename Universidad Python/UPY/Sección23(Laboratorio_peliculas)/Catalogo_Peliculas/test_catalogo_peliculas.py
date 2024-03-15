opcion = None

while opcion != 4:
    opcion = int(input(''' 
Opciones:
1) Agregar pelicula
2) Listar peliculas
3) Eliminar archivo de peliculas
4) Salir
'''))
    
if opcion == 1:
    nombre = input('Dime la pelicula a agregar: ')
    