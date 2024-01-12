# Valor dentro del rango
valor = int(input('Dame el valor entre 0 y 5: '))
valorMaximo = 5
valorMinimo = 0

dentroRango = (valor <= valorMaximo) and (valor >= valorMinimo)

if dentroRango:
    print('El valor esta dentro del rango')
else:
    print('El valor esta fuera del rango')