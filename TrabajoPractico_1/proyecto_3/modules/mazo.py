# mazo.py
import random
from modules.carta import Carta
class DequeEmptyError(Exception):
    """Excepción personalizada para mazos vacíos."""
    pass

class Nododato:
    """Nodo que representa una dato en una lista doblemente enlazada."""
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


class Mazo:
    """Clase que representa un mazo de datos utilizando una lista doblemente enlazada."""
    def __init__(self):
        self.mazo = self
        self.cabeza = None
        self.cola = None
        self._size = 0
        self.crear_mazo()
        

    def crear_mazo(self):
        """Genera el mazo estándar de 52 datos con 4 palos y 13 valores."""
        palos = ['♠', '♥', '♦', '♣']
        valores = Carta.valores
        for palo in palos:
            for valor in valores:
                dato = Carta(valor, palo)
                self.poner_carta_abajo(dato)
        random.shuffle(self._mazo_como_lista())  # Mezcla las datos generadas

    def _mazo_como_lista(self):
        """Convierte el mazo en una lista de datos para mezclarlas."""
        datos = []
        actual = self.cabeza
        while actual:
            datos.append(actual.dato)
            actual = actual.siguiente
        return datos

    def __len__(self):
        """Retorna el número de datos en el mazo."""
        return self._size

    def poner_carta_arriba(self, dato):
        """Coloca una dato al principio del mazo (arriba)."""
        nuevo_nodo = Nododato(dato)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self._size += 1

    def poner_carta_abajo(self, dato):
        """Coloca una dato al final del mazo (abajo)."""
        nuevo_nodo = Nododato(dato)
        if self.cola is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self._size += 1

    def sacar_carta_arriba(self):
        """Saca una dato del principio del mazo (arriba)."""
        if self.cabeza is None:
            raise DequeEmptyError("El mazo está vacío.")
        dato = self.cabeza.dato
        if self.cabeza == self.cola:
            self.cabeza = self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
        self._size -= 1
        return dato

    def sacar_dato_abajo(self):
        """Saca una dato del final del mazo (abajo)."""
        if self.cola is None:
            raise DequeEmptyError("El mazo está vacío.")
        dato = self.cola.dato
        if self.cabeza == self.cola:
            self.cabeza = self.cola = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
        self._size -= 1
        return dato

    def __str__(self):
        """Imprime las datos del mazo desde la cabeza a la cola."""
        actual = self.cabeza
        datos = []
        while actual:
            datos.append(str(actual.dato))
            actual = actual.siguiente
        return " ".join(datos)