# Break. Este nos ayudara romper el ciclo. Tomaremos como ejemplo que quiero imprimir solo la primera 'r' de la palabra
# 'Frustrar', si no usamos el break seria este resulado...
frase = 'Frustrar'
for letra in frase:
    if letra == 'r':
        print(letra)
else:
    print('Fin del ciclo while')

# Pero si a nuestro codigo le agregamos el break despues de pintar la letra entonces se rompera y solo los pintara una r
for letra in frase:
    if letra == 'r':
        print(letra)
        break
else:
    print('Fin del ciclo')  # Podremos notar en consola que este print no se pintara ya quue con el break saldra de esta
    # estructura pero si este print lo movemos fuera de la estructura nos debe de dejar
print('Fin del ciclo')