# mazo.py

from .LDE import ListaDobleEnlazada
from .carta import Carta

class DequeEmptyError(Exception):
    def __init__(self):
        super().__init__('Mazo sin cartas')

class Mazo(ListaDobleEnlazada):
    def __init__(self):
        super().__init__()

    def poner_carta_arriba(self, p_carta):
        if not isinstance(p_carta, Carta):
            raise TypeError()
        self.agregar_al_inicio(p_carta)

    def sacar_carta_arriba(self, mostrar=False):
        if self.esta_vacia():
            raise DequeEmptyError()
        carta = self.extraer(0)
        if mostrar:
            carta.visible = True
        return carta

    def poner_carta_abajo(self, p_carta):
        if not isinstance(p_carta, Carta):
            raise TypeError()
        self.agregar_al_final(p_carta)