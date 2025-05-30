class Vertice:
    def __init__(self, clave):
        self.__id = clave 
        self.__conectadoA = {}

    def agregarVecino (self, vecino, ponderacion = 0):
        self.__conectadoA [vecino] = ponderacion 
    
    def __str__ (self):
        return str(self.__id)
        # return str (self.__id) + ' conectada a: ' + str ([x.__id for x in self.__conectadoA])
    
    def obtenerConexiones (self):
        return self.__conectadoA.keys()
    
    def obtenerId (self):
        return self.__id
    
    def obtenerPonderacion (self, vecino):
        return self.__conectadoA [vecino]
    
class Grafo:
    def __init__(self):
        self.listaVertices = {}
        self.numVertices = 0

    def __len__(self):
        return self.numVertices

    def agregarVertice(self, clave):
        self.numVertices = self.numVertices + 1
        nuevoVertice = Vertice(clave)
        self.listaVertices[clave] = nuevoVertice
        return nuevoVertice

    def obtenerVertice(self, n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None
        
    def __contains__(self, n):
        return n in self.listaVertices
    
    def agregarArista(self, desde, hasta, costo=0):
        if desde not in self.listaVertices:
            nv = self.agregarVertice(desde)
        if hasta not in self.listaVertices:
            nv = self.agregarVertice(hasta)
        self.listaVertices[desde].agregarVecino(self.listaVertices[hasta],costo)

    def obtenerVertices(self):
        """Devuelve una lista con las claves (aldeas)"""
        return self.listaVertices.keys()
    
    def __iter__(self):
        return iter(self.listaVertices.values())
    
if __name__ == '__main__':
    g = Grafo()
    for i in range(6):
        g.agregarVertice(i)
    print(g.listaVertices)

