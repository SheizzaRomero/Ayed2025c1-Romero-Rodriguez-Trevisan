class NodoArbol:
    def __init__(self, clave, dato, hIz=None, hDer=None, padre=None):
        self._clave = clave
        self.__carga_util = dato
        self.__hijo_izquierdo = hIz
        self.__hijo_derecho = hDer
        self._padre = padre
        self.__factor_equilibrio = 0

    def __lt__(self, otro)->bool:
        salida = False
        if self._clave < otro._clave:
            salida = True
        return salida

    @property
    def factorEquilibrio(self)->int:
        return self.__factor_equilibrio

    @factorEquilibrio.setter
    def factorEquilibrio(self, valor):
        self.__factor_equilibrio = valor

    def tieneHijoIzquierdo(self)->bool:
        salida = True
        if self.__hijo_izquierdo is None:
            salida = False
        return salida

    def tieneHijoDerecho(self)->bool:
        salida = True
        if self.__hijo_derecho is None:
            salida = False
        return salida

    def esHijoIzquierdo(self)->bool:
        salida = True
        if self._padre is None or self._padre.__hijo_izquierdo != self:
            salida = False
        return salida

    def esHijoDerecho(self)->bool:
        salida = True
        if self._padre is None or self._padre.__hijo_derecho != self:
            salida = False
        return salida

    def esRaiz(self)->bool:
        salida = False
        if self._padre is None:
            salida = True
        return salida

    def esHoja(self)->bool:
        salida = False
        if self.__hijo_izquierdo is None and self.__hijo_derecho is None:
            salida = True
        return salida

    def tieneAlgunHijo(self)->bool:
        salida = True
        if self.__hijo_izquierdo is None and self.__hiDerecho is None:
            salida = False
        return salida

    def tieneAmbosHijos(self)->bool:
        salida = True
        if self.__hijo_izquierdo is None or self.__hijo_derecho is None:
            salida = False
        return salida

class ArbolBinarioBusqueda_AVL:
    def __init__(self):
        self.__raiz = None
        self.__tamano = 0

    def __len__(self)->int:
        return self.__tamano

    def _reequilibrar(self,nodo):
        pass

    def _actualizarEquilibrio(self,nodo):
        if nodo.factorEquilibrio > 1 or nodo.factorEquilibrio < -1:
            self._reequilibrar(nodo)
        else:
            if nodo.esHijoIzquierdo():
                nodo._padre.factorEquilibrio += 1
            elif nodo.esHijoDerecho():
                nodo._padre.factorEquilibrio -= 1
            if not nodo.esRaiz():   # es hjo?
                self._actualizarEquilibrio(nodo._padre)

    def _agregar(self,clave,dato,nodoActual):
        if clave < nodoActual._clave:
            if nodoActual.tieneHijoIzquierdo():
                self._agregar(clave,dato,nodoActual.__hijo_izquierdo)
            else:
                nodoActual.__hijo_izquierdo = NodoArbol(clave,dato,padre=nodoActual)
                self._actualizarEquilibrio(nodoActual.__hijo_izquierdo)
        else:
            if nodoActual.tieneHijoDerecho():
                self._agregar(clave,dato,nodoActual.__hijo_derecho)
            else:
                nodoActual.__hijo_derecho = NodoArbol(clave,dato,padre=nodoActual)
                self._actualizarEquilibrio(nodoActual.__hijo_derecho)

    def agregar(self,clave,dato):
        if self.__raiz is None:
            self.__raiz = NodoArbol(clave,dato)
        else:
            self._agregar(clave,dato,self.__raiz)
        self.__tamano += 1

    def longitud(self)->int:
        return self.__tamano

    def __iter__(self):
        return self.__raiz.__iter__()
    

    def rotarIzquierda(self,rotRaiz):
        nuevaRaiz = rotRaiz.__hijo_derecho
        rotRaiz.__hijo_derecho = nuevaRaiz.__hijo_izquierdo
        if nuevaRaiz.__hijo_izquierdo != None:
            nuevaRaiz.__hijo_izquierdo._padre = rotRaiz
        nuevaRaiz._padre = rotRaiz._padre
        if rotRaiz.esRaiz():
            self.__raiz = nuevaRaiz
        else:
            if rotRaiz.esHijoIzquierdo():
                    rotRaiz._padre.__hijo_izquierdo = nuevaRaiz
            else:
                rotRaiz._padre.__hijo_derecho = nuevaRaiz
        nuevaRaiz.__hijo_izquierdo = rotRaiz
        rotRaiz._padre = nuevaRaiz
        rotRaiz.factorEquilibrio = rotRaiz.factorEquilibrio + 1 - min(nuevaRaiz.factorEquilibrio, 0)
        nuevaRaiz.factorEquilibrio = nuevaRaiz.factorEquilibrio + 1 + max(rotRaiz.factorEquilibrio, 0)
        
# Falta agregar el caso en que esten repetidas las claves 
    def __setitem__(self,c,v):
        self.agregar(c,v)


    def obtener(self,clave):
       if self.__raiz:
        res = self._obtener(clave,self.__raiz)
        if res:
            return res.__carga_util
        else:
            return None
       else:
            return None

    def _obtener(self,clave,nodoActual):
        if not nodoActual:
            return None
        elif nodoActual._clave == clave:
            return nodoActual
        elif clave < nodoActual._clave:
            return self._obtener(clave,nodoActual.__hijo_izquierdo)
        else:
            return self._obtener(clave,nodoActual.__hijo_derecho)

    def __getitem__(self,clave):
        return self.obtener(clave)
    

    def __contains__(self,clave):
        if self._obtener(clave,self.__raiz):
            return True
        else:
            return False
        
      
    def eliminar(self,clave):
        if self.tamano > 1:
            nodoAEliminar = self._obtener(clave,self.__raiz)
            if nodoAEliminar:
                self.remover(nodoAEliminar)
                self.tamano = self.tamano-1
            else:
                raise KeyError('Error, la clave no está en el árbol')
        elif self.tamano == 1 and self.__raiz._clave == clave:
            self.__raiz = None
            self.tamano = self.tamano - 1
        else:
            raise KeyError('Error, la clave no está en el árbol')
    def __delitem__(self,clave):
        self.eliminar(clave)


    def remover(self, nodoActual):
        # Caso 1: el nodo es una hoja (sin hijos)
        if nodoActual.esHoja():
            if nodoActual == nodoActual._padre.__hijo_izquierdo:
                nodoActual._padre.__hijo_izquierdo = None
            else:
                nodoActual._padre.__hijo_derecho = None

        # Caso 2: el nodo tiene un solo hijo
        elif nodoActual.tieneUnHijo():
            if nodoActual.tieneHijoIzquierdo():
                if nodoActual == nodoActual._padre.__hijo_izquierdo:
                    nodoActual._padre.__hijo_izquierdo = nodoActual.__hijo_izquierdo
                else:
                    nodoActual._padre.__hijo_derecho = nodoActual.__hijo_izquierdo
                nodoActual.__hijo_izquierdo._padre = nodoActual._padre
            else:
                if nodoActual == nodoActual._padre.__hijo_izquierdo:
                    nodoActual._padre.__hijo_izquierdo = nodoActual.__hijo_derecho
                else:
                    nodoActual._padre.__hijo_derecho = nodoActual.__hijo_derecho
                nodoActual.__hijo_derecho._padre = nodoActual._padre

        # Caso 3: el nodo tiene dos hijos
        else:
            sucesor = nodoActual.encontrarSucesor()
            nodoActual._clave = sucesor._clave
            nodoActual.__carga_util = sucesor.__carga_util
            self.remover(sucesor)  # El sucesor será un caso 1 o 2

 
    def encontrarSucesor(self):
        suc = None
        if self.tieneHijoDerecho():
            suc = self.__hijo_derecho.encontrarMin()
        else:
            if self._padre:
                if self.esHijoIzquierdo():
                    suc = self._padre
                else:
                    self._padre.__hijo_derecho = None
                    suc = self._padre.encontrarSucesor()
                    self._padre.__hijo_derecho = self
        return suc

    def encontrarMin(self):
        actual = self
        while actual.tieneHijoIzquierdo():
            actual = actual.__hijo_izquierdo
        return actual

    def empalmar(self):
        if self.esHoja():
            if self.esHijoIzquierdo():
                self._padre.__hijo_izquierdo = None
            else:
                self._padre.__hijo_derecho = None
        elif self.tieneAlgunHijo():
            if self.tieneHijoIzquierdo():
                if self.esHijoIzquierdo():
                    self._padre.__hijo_izquierdo = self.__hijo_izquierdo
                else:
                    self._padre.__hijo_derecho = self.__hijo_izquierdo
                self.__hijo_izquierdo._padre = self._padre
            else:
                if self.esHijoIzquierdo():
                    self._padre.__hijo_izquierdo = self.__hijo_derecho
                else:
                    self._padre.__hijo_derecho = self.__hijo_derecho
                self.__hijo_derecho._padre = self._padre
    
    def __iter__(self):
        if self.tieneHijoIzquierdo():
           for elem in self.__hijo_izquierdo:
                yield elem
        yield self._clave
        if self.tieneHijoDerecho():
            for elem in self.__hijo_derecho:
                yield elem