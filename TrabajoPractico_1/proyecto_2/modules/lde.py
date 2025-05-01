class Nodo:
    def __init__(self, p_item, p_anterior=None, p_siguiente=None):
        self.__elemento = p_item
        self.__anterior = p_anterior
        self.__siguiente = p_siguiente

    def __str__(self):
        return str(self.__elemento)

    @property
    def elemento(self):
        return self.__elemento

    @property
    def siguiente(self):
        return self.__siguiente

    @property
    def anterior(self):
        return self.__anterior

    def _establecer_siguiente(self, p_elemento):
        self.__siguiente = p_elemento

    def _establecer_anterior(self, p_elemento):
        self.__anterior = p_elemento

    def _intercambiar_punteros(self):
        self.__anterior,self.__siguiente = self.__siguiente,self.__anterior

class ListaDobleEnlazada:
    def __init__(self):
        self.__cantidad_elementos = 0
        self.__cabeza = None
        self.__cola = None

    def __len__(self):
        return self.__cantidad_elementos

    def __add__(self,p_lista):
        return ListaDobleEnlazada().concatenar(self).concatenar(p_lista)

    def __str__(self):
        cadena = 'lista sin elementos'
        if self.__cantidad_elementos > 0:
            puntero = self.__cabeza
            elementos = list()
            while puntero is not None:
                elementos.append(f"{puntero.elemento}")
                puntero = puntero.siguiente
            cadena = ' - '.join(elementos)
        return cadena

    @property
    def _nodo_cabeza(self):
        return self.__cabeza

    def esta_vacia(self) -> bool:
        return self.__cantidad_elementos == 0

    def agregar_al_inicio(self, item):
        self.insertar(item,0)

    def agregar_al_final(self, item):
        self.insertar(item,-1)

    def insertar(self, item, posicion=-1):   # valor negativo inserta al final
        if not isinstance(posicion, int):
            raise TypeError()
        if posicion > self.__cantidad_elementos:
            raise IndexError()
        uno = Nodo(item)
        if posicion == 0:   # insertar al comienzo
            cabeza_anterior = self.__cabeza
            uno._establecer_siguiente(self.__cabeza)
            self.__cabeza = uno
            self.__cantidad_elementos += 1
            if self.__cantidad_elementos == 1:
                self.__cola = uno
            else:
                cabeza_anterior._establecer_anterior(uno)
        elif posicion < 0 or posicion == self.__cantidad_elementos:   # insertar al final
            cola_anterior = self.__cola
            uno._establecer_anterior(self.__cola)
            self.__cola = uno
            self.__cantidad_elementos += 1
            if self.__cantidad_elementos == 1:
                self.__cabeza = uno
            else:
                cola_anterior._establecer_siguiente(uno)
        else:   # insertar en el lugar indicado
            puntero = self.__cabeza
            for _ in range(posicion):
                puntero = puntero.siguiente
            uno = Nodo(item, puntero.anterior, puntero)
            puntero.anterior._establecer_siguiente(uno)
            puntero._establecer_anterior(uno)
            self.__cantidad_elementos += 1

    def extraer(self, posicion=-1) -> str:   # valor negativo extrae '__cola'
        if not isinstance(posicion, int):
            raise TypeError()
        if posicion >= self.__cantidad_elementos:
            raise IndexError()
        uno = None
        if posicion == 0:   # extraer '__cabeza'
            uno = self.__cabeza
            self.__cabeza = uno.siguiente
            self.__cabeza._establecer_anterior(None)
        elif posicion < 0 or posicion == self.__cantidad_elementos-1:   # extraer '__cola'
            uno = self.__cola
            self.__cola = uno.anterior
            self.__cola._establecer_siguiente(None)
        else:
            uno = self.__cabeza
            for _ in range(posicion):
                uno = uno.siguiente
            uno.anterior._establecer_siguiente(uno.siguiente)
            uno.siguiente._establecer_anterior(uno.anterior)
        self.__cantidad_elementos -= 1
        return uno.elemento

    def copiar(self):
        lista_nueva = ListaDobleEnlazada()
        if self.__cantidad_elementos > 0:
            puntero = self.__cabeza
            for _ in range(self.__cantidad_elementos):
                lista_nueva.insertar(puntero.elemento)
                puntero = puntero.siguiente
        return lista_nueva

    def invertir(self):
        if self.__cantidad_elementos > 1:
            self.__cabeza,self.__cola = self.__cola,self.__cabeza
            puntero = self.__cabeza
            for _ in range(self.__cantidad_elementos):
                puntero._intercambiar_punteros()
                puntero = puntero.siguiente   # antes era 'Nodo.__anterior'

    def concatenar(self, p_lista):
        if not p_lista.esta_vacia():
            puntero = p_lista._nodo_cabeza
            for _ in range(len(p_lista)):
                self.agregar_al_final(puntero.elemento)
                puntero = puntero.siguiente
        return self

if __name__ == "__main__":
    print('*** ENSAYOS ***')
    print('* INICIO')
    lista = ListaDobleEnlazada()
    if lista.esta_vacia():
        print('lista sin elementos')
    lista.agregar_al_final('abc')
    lista.agregar_al_final('xyz')
    lista.agregar_al_final('rst')
    lista.agregar_al_final('00')
    lista.agregar_al_inicio('ini')
    lista.insertar('qqq',2)
    print('cantidad de elementos:', len(lista))
    print('elementos:', lista)
    print('extraer la cola:', lista.extraer())
    print('extraer la cabeza:', lista.extraer(0))
    print('cantidad de elementos:', len(lista))
    print('elementos:', lista)
    lista.invertir()
    print('lista invertida:', lista)
    print('extraer tercer elemento', lista.extraer(2))
    print('final', lista)
    otra_lista = ListaDobleEnlazada()
    otra_lista.agregar_al_final('chuchu')
    otra_lista.agregar_al_final('zucuzucu')
    otra_lista.agregar_al_final('pikipiki')
    print('otra lista:', otra_lista)
    print('listas sumadas:', lista+otra_lista)
    print('* FIN')