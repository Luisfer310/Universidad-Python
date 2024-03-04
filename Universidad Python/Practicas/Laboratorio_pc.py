class DispositivoEntrada:
    def __init__(self, marca):
        self._marca = marca
    @property
    def marca(self):
        return self._marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    def __str__(self):
        return f'Marca {self._marca}'
    
class Raton(DispositivoEntrada):
    contadorRatones = 0
    def __init__(self, marca):
        super().__init__(marca)
        self.contadorRatones += 1
        self._idRaton = Raton.contadorRatones
        self._marcaRaton = marca

    @property
    def marcaRaton(self):
        return self._marcaRaton
    @marcaRaton.setter
    def marcaRaton(self, marcaRaton):
        self._marcaRaton = marcaRaton

    def __str__(self):
        return f'Marca del raton {self._marcaRaton}'

class Teclado(DispositivoEntrada):
    contadorTeclados = 0
    def __init__(self, marca):
        super().__init__(marca)
        self.contadorTeclados += 1
        self._id = self.contadorTeclados
        self._marcaTeclado = marca

    @property
    def marcaTeclado(self):
        return self._marcaTeclado
    @marcaTeclado.setter
    def marcaTeclado(self, marcaTeclado):
        self._marcaTeclado = marcaTeclado

    def __str__(self):
        return f'Teclado marca {self._marcaTeclado}'
    
class Monitor(DispositivoEntrada):
    contadorMonitor = 0
    def __init__(self, marca):
        super().__init__(marca)
        Monitor.contadorMonitor += 1
        self._idMonitor = self.contadorMonitor
        self._marcaMonitor = marca

    @property
    def marcaMonitor(self):
        return self._marcaMonitor
    @marcaMonitor.setter
    def marcaMonitor(self, marcaMonitor):
        self._marcaMonitor = marcaMonitor

    @property
    def tamaño(self):
        return self._tamaño
    @tamaño.setter
    def tamaño(self, tamaño):
        self._tamaño = tamaño

    @property
    def idMonitor(self):
        return self._idMonitor
    @idMonitor.setter
    def idMonitor(self, idMonitor):
        self._idMonitor = idMonitor


    def __str__(self):
        return f'Marca del monitor: {self._marcaMonitor}'
    

    
if __name__ == '__main__':
    marcaR = input('Dame la marca del Raton: ')
    raton = Raton(marcaR)
    print(raton)

    marcaT = input('Dame la marca del teclado: ')
    teclado = Teclado(marcaT)
    print(teclado)

    marcaM = input('Dame la marca del monitor: ')
    monitor = Monitor(marcaM)
    print(monitor)
    print(monitor.idMonitor)