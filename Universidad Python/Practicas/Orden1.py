from Laboratorio_pc import *

class Orden(Computadora):
    contador_ordenes = 0
    listaComputadoras = list()
    def __init__(self):
        super().__init__()