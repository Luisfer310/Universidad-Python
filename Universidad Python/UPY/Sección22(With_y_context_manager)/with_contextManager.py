class ManejoArchivo:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        print('Obteniendo recursos...'.center(50, '-'))
        self.nombre = open(self.nombre, 'r')
        return self.nombre
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Cerrando los recursos...'.center(50, '-'))
        if self.nombre: # Se sentencia esta condicion para indicar que el archivo se cerrara solo si esta abierto
            self.nombre.close()