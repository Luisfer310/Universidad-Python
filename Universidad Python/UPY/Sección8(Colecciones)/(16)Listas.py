# Definicion de una lista
variableLista = ['Luis', 'Maria', 'Juan', 'Fernando', 'Enrique', 'Karina', 'Joel']
# Imprimir la lista
print(variableLista)
# Imprimir un elemento de la lista
print(variableLista[2])
# Imprimir el ultimo elemento con negativos
print(variableLista[-1])
# Imprimir elementos de una lista en un rango
print(variableLista[1:3])
# Imprimir desde cierto indice hasta el final de la lista y no conocemos cuantos elementos tiene la lista.
print(variableLista[2:])
# Cambiar un elemento
variableLista[6] = 'Gabriel'
print(variableLista)
# Iterar lista
for n in variableLista:
      print(n)
# Saber el largo de la lista
print(len(variableLista))
# Añadir elementos a lo ultimo de la lista
variableLista.append('Jorge')
print(variableLista)
# Agregar un elemento en un indice en especifico
variableLista.insert(2, 'Marco')
print(variableLista)
#  Eliminar el ultimo valor
variableLista.pop()
print(variableLista)
# Eliminar un elemento pero no por su indice si no por el valor
variableLista.remove('Maria')
print(variableLista)
# remover un elemento en un indice indicado
del variableLista[0]
print(variableLista)
# Limpiar la lista
variableLista.clear()
print(variableLista)
# Eliminar la lista
del variableLista
print(variableLista)
