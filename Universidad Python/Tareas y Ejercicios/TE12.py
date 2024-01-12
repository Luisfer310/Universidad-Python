mesnum = int(input('Indicame el mes del 1 al 12: '))
estacion = None
mes = None

if mesnum == 1:
    estacion = 'Invierno'
    mes = 'Enero'
elif mesnum == 2:
    estacion = 'Invierno'
    mes = 'Febrero'
elif mesnum == 3:
    estacion = 'Invierno'
    mes = 'Marzo'
elif mesnum == 4:
    estacion = 'Primavera'
    mes = 'Abril'
elif mesnum == 5:
    estacion = 'Primavera'
    mes = 'Mayo'
elif mesnum == 6:
    estacion = 'Primavera'
    mes = 'Junio'
elif mesnum == 7:
    estacion = 'Verano'
    mes = 'Julio'
elif mesnum == 8:
    estacion = 'Verano'
    mes = 'Agosto'
elif mesnum == 9:
    estacion = 'Verano'
    mes = 'Septiembre'
elif mesnum == 10:
    estacion = 'Otoño'
    mes = 'Octubre'
elif mesnum == 11:
    estacion = 'Otoño'
    mes = 'Noviembre'
elif mesnum == 12:
    estacion = 'Otoño'
    mes = 'Diciembre'
else:
    print('No existe el mes')
print(f'El mes {mesnum} es el mes {mes} y su estación es {estacion}.')