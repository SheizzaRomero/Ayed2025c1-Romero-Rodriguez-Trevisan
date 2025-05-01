# mazo.py

from modules.LDE import ListaDobleEnlazada

class DequeEmptyError(Exception):
    """Excepción para indicar que el mazo está vacío."""
    pass


class Mazo(ListaDobleEnlazada):
    """Representa un mazo de cartas como una lista doblemente enlazada."""

    def poner_carta_arriba(self, carta):
        """Inserta una carta en el inicio del mazo (arriba)."""
        self.insertar_primero(carta)

    def poner_carta_abajo(self, carta):
        """Inserta una carta al final del mazo (abajo)."""
        self.insertar_ultimo(carta)

    def sacar_carta_arriba(self, mostrar=False):
        """Quita y devuelve la carta de arriba del mazo. Puede mostrarla."""
        if self.esta_vacia():
            raise DequeEmptyError("El mazo está vacío")
        carta = self.eliminar_primero()
        if mostrar:
            carta.visible = True
        return carta

    def __str__(self):
        return " ".join([str(carta) for carta in self])
