class Vertice:
    def __init__(self, clave):
        self.__id = clave
        self.__conexiones = {}

    def agregarVecino(self, vecino, ponderacion = 0):
        self.__conexiones[vecino] = ponderacion

    def __str__(self):
        return str(self.__id)
        # return str (self.__id) + ' conectada a: ' + str ([x.__id for x in self.__conectadoA])

    def obtenerConexiones(self):
        return self.__conexiones.keys()

    def obtenerId(self):
        return self.__id

    def obtenerPonderacion(self, vecino):
        return self.__conexiones[vecino]

class Grafo:
    def __init__(self):
        self.__vertices = {}

    def __len__(self):
        return len(self.__vertices)

    def agregarVertice(self, clave):
        nuevo = Vertice(clave)
        self.__vertices[clave] = nuevo
        return nuevo

    def obtenerVertice(self, n):
        if n in self.__vertices:
            return self.__vertices[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.__vertices

    def agregarArista(self, desde, hasta, ponderacion = 0):
        if desde not in self.__vertices:
            nv = self.agregarVertice(desde)
        if hasta not in self.__vertices:
            nv = self.agregarVertice(hasta)
        self.__vertices[desde].agregarVecino(self.__vertices[hasta],ponderacion)

    def obtenerVertices(self):
        """Devuelve una lista con las claves (aldeas)"""
        return self.__vertices.keys()

    def __iter__(self):
        return iter(self.__vertices.values())
    
if __name__ == '__main__':
    g = Grafo()
    for i in range(6):
        g.agregarVertice(i)
    print(g.obtenerVertices())