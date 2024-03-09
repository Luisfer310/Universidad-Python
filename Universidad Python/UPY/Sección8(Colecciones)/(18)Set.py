# Nuevo metodo aprendido en la clase de Set pero se puede aplicar tambien a las listas. Este metodo nos permite
# verificar si un elemento de encuntra dentro de la coleccion y nos retorna un bool.
miSet = {'Venus', 'Tierra', 'Marte'}
print('Tierra' in miSet)

miSet = {'Venus', 'Tierra', 'Marte'}
print('Jupiter' in miSet)

# Demostracion de que los set no tienen un acomodo, por lo cual cada que imprima el set tendra un orden diferente
print(miSet)

# Y tampoco acepta duplicados, por lo cual si se quiere agregar un elemento y este esta duplicado no lo agregara pero no
# arrojara error, solo no ejecuta la accion de agregar.
miSet.add('Tierra')  # Podemos observar que a diferencia de las listas para agregar elementos no usamos el metodo append
# si no el metodo add.

# El que si es igual al de las listas, es el de eliminar un elemento el cual es el metodo remove.
miSet.remove('Marte')
print(miSet)

# Pero tenemos uno mas para eliminar el cual es el de discard, con este podemos eliminar un valor, pero este nos
# permitira que si nos equivocamos a la hora de poner el nombre del elemento no nos retorne un error, sino que solo
# ignore la sentencia.
miSet.discard('Venuss')  # En este no dara error
print(miSet)
miSet.remove('Venu')  # Pero en este si
print(miSet)
