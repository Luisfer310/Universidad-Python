from DispositivoEntrada import *

class Raton(DispositivoEntrada):
    contador_ratones = 0

    def __init__(self, tipo_entrada, marca):
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones
        super().__init__(marca, tipo_entrada)

        def __str__(self):
            return f'El {self.tipo_entrada} es de la marca {self.marca}'
