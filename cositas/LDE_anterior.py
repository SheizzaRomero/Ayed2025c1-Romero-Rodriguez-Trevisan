# modules/LDE.py

class Nodo:
    def __init__(self, dato, anterior=None, siguiente=None):
        self.dato = dato
        self.anterior = anterior
        self.siguiente = siguiente


class ListaDobleEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self._tamano = 0

    def esta_vacia(self):
        return self._tamano == 0

    def insertar_primero(self, dato):
        nuevo = Nodo(dato, None, self.primero)
        if self.primero is not None:
            self.primero.anterior = nuevo
        self.primero = nuevo
        if self.ultimo is None:
            self.ultimo = nuevo
        self._tamano += 1

    def insertar_ultimo(self, dato):
        nuevo = Nodo(dato, self.ultimo, None)
        if self.ultimo is not None:
            self.ultimo.siguiente = nuevo
        self.ultimo = nuevo
        if self.primero is None:
            self.primero = nuevo
        self._tamano += 1

    def eliminar_primero(self):
        if self.esta_vacia():
            raise IndexError("La lista está vacía")
        dato = self.primero.dato
        self.primero = self.primero.siguiente
        if self.primero is not None:
            self.primero.anterior = None
        else:
            self.ultimo = None
        self._tamano -= 1
        return dato

    def eliminar_ultimo(self):
        if self.esta_vacia():
            raise IndexError("La lista está vacía")
        dato = self.ultimo.dato
        self.ultimo = self.ultimo.anterior
        if self.ultimo is not None:
            self.ultimo.siguiente = None
        else:
            self.primero = None
        self._tamano -= 1
        return dato

    def __len__(self):
        return self._tamano

    def __iter__(self):
        actual = self.primero
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente
