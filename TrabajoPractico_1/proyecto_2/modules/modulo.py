class Nodo:
    def __init__(self, p_item, p_anterior=None, p_siguiente=None):
        self.__elemento = p_item
        self.__anterior = p_anterior
        self.__siguiente = p_siguiente

    @property
    def elemento(self):
        return self.__elemento

    @property
    def siguiente(self):
        return self.__siguiente

    @siguiente.setter
    def _establecer_siguiente(self, p_elemento):
        self.__siguiente = p_elemento

    @property
    def anterior(self):
        return self.__anterior

    @anterior.setter
    def _establecer_anterior(self, p_elemento):
        self.__anterior = p_elemento

    def _intercambiar_punteros(self):
        self.__anterior,self.__siguiente = self.__siguiente,self.__anterior

class ListaDobleEnlazada:
    def __init__(self):
        self.__cantidad_elementos = 0
        self.__cabeza = None
        self.__cola = None

    def esta_vacia(self):
        salida = False
        if self.__cantidad_elementos == 0:
            salida = True
        return salida

    def __len__(self):
        return self.__cantidad_elementos

    def agregar_al_inicio(self, item):
        uno = Nodo(item,p_siguiente=self.__cabeza)
        self.__cabeza = uno
        self.__cantidad_elementos += 1

    def agregar_al_final(self, item):
        uno = Nodo(item,p_anterior=self.__cola)
        self.__cola = uno
        self.__cantidad_elementos += 1

    def insertar(self, item, posicion=-1):
        if posicion == 0:
            self.agregar_al_inicio(item)
        elif posicion < 0:
            self.agregar_al_final(item)
        else:   # OJO: falta controla si 'posicion' >> '__cantidad_elementos'
            puntero = self.__cabeza
            for _ in range(posicion):
                puntero = puntero.siguiente
            uno = Nodo(item, puntero, puntero.siguiente)
            puntero._establecer_siguiente(uno)
            puntero.siguiente._establecer_anterior(uno)
            self.__cantidad_elementos += 1

    def extraer(self, posicion=-1):
        uno = None
        if posicion == 0:
            uno = self.__cabeza
            self.__cabeza = uno.siguiente
            self.__cantidad_elementos -= 1
        elif posicion < 0:
            uno = self.__cola
            self.__cola = uno.anterior
            self.__cantidad_elementos -= 1
        return uno.elemento   # OJO: falta mucho por implementar

    def copiar(self):
        lista_nueva = ListaDobleEnlazada()
        puntero = self.__cabeza
        while puntero is not None:
            lista_nueva.insertar(puntero.elemento)
            puntero = puntero.siguiente
        return lista_nueva

    def invertir(self):
        if self.__cantidad_elementos > 1:
            self.__cabeza = self.__cola
            puntero = self.__cabeza
            while puntero.anterior is not None:
                puntero._intercambiar_punteros()
                puntero = puntero.siguiente
            else:
                puntero._intercambiar_punteros()
            self.__cola = puntero

    def concatenar(p_lista):
        pass