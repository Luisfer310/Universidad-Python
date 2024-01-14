# La forma anterior en la que usaba el if con una condición simple
condicion = True

if condicion == True:
    print("Condición valida")
else:
    print("No valida")

# Forma simplificada de la condición simple
condicion2 = True

if condicion2:
    print("Condicion valida")
else:
    print("No valida")

# Uso el elif
calificacion = 8

if calificacion == 10: # and calificacion <= 10: (Esto se usara si no usamos el segundo elif, ya que si lo ponemos como
    # else y en la variable tenemos un valor arriba de 10 no podremos poner que tiene un error.)
    print("Exentaste")
elif (calificacion >= 6) and (calificacion <= 9):
    print('Aprobaste')
elif (calificacion >= 0) and (calificacion < 6):
    print('Reprobaste')
else:
    print('Error')

# Sintaxis simplificada
condicion3 = 6
if condicion3 >= 6 and condicion3 <= 10: # En este podemos observar que le paso las 2 condiciones llamando 2 veces a la
    # variable, por lo cual la linea es un poco mas larga que de la otra forma.
    print('Aprobaste')
else:
    print('Reprobaste')


if 6 <= condicion3 <= 10: # En esta sintaxis se usara una sola la vez la variable y podemos ver que se usa como si fuera
    # la sentencia and. Puedes leer mas de esto en Notion, seccion 6 de Universidad Python.
    print('Aprobaste')
else:
    print('Reprobaste')
