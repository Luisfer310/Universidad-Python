from DispositivoEntrada import *

class Teclado(DispositivoEntrada):
    contador_teclados = 0

    def __init__(self, tipo_entrada, marca):
        Teclado.contador_teclados += 1
        self._id_teclado = Teclado.contador_teclados
        super().__init__(marca, tipo_entrada)

        def __str__(self):
            return f'El {self.tipo_entrada} es de la marca {self.marca}'
