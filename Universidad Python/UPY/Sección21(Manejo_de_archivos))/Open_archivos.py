try:
    archivo = open('NuevoArchivo.txt', 'w')

    archivo.write('Nueva linea de información en el archivo\n')
    archivo.write('Otra linea')

except Exception as e:
    print(f'Error: {e}')
finally:
    archivo.close()