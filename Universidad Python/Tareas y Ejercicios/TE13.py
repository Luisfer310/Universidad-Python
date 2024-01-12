edad = int(input('Ingresa tu edad y te diremos una frase sobre la etapa de la vida en la que estas: '))
frase = None

if (edad >= 0) and (edad <= 10):
    frase = 'La infancia es increíble…'
elif (edad >= 11) and (edad <= 20):
    frase = 'Muchos cambios y mucho estudio…'
elif (edad >= 21) and (edad <= 30):
    frase = 'Amor y comienza el trabajo…'
else:
    print('Etapa de vida no reconocida')

print(f'La frase asignada para tu edad ({edad}) es la siguiente: {frase}')
