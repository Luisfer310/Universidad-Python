# Lectura del archivo
try:
    archivo = open('NuevoArchivo.txt', 'r')
    print(archivo.read())

except Exception as e:
    print(f'Error en el archivo: {e}')
finally:
    archivo.close()

# Lectura por numero de caracteres
try:
    archivo1 = open('NuevoArchivo.txt', 'r')
    print(archivo1.read(5))
    print(archivo1.read(7))

except Exception as e:
    print(f'Error en el archivo: {e}')
finally:
    archivo1.close()

# Lectura por lineas
try:
    archivo2 = open('NuevoArchivo.txt', 'r')
    print(archivo2.readline())

except Exception as e:
    print(f'Error en el archivo: {e}')
finally:
    archivo2.close()

# Iteracion de lineas
try:
    archivo3 = open('NuevoArchivo.txt')
    for linea in archivo3:
        print(linea)

except Exception as e:
    print(f'Error en el archivo: {e}')
finally:
    archivo3.close()

# Lineas en una lista
try:
	archivo = open('NuevoArchivo.txt')
	print(archivo.readlines()[1])
except Exception as e:
		print(f'Error en el archivo: {e}')
finally:
		archivo.close() 

# Copiar en contenido de un archivo en otro
try:
    archivo = open('NuevoArchivo.txt', 'r')
    copia = open('copia.txt', 'a')
    copia.write(archivo.read())

except Exception as e:
    print(f'Error en el archivo: {e}')