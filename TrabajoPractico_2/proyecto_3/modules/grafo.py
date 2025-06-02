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
        return list(self.__conexiones.keys())

    def obtenerId(self):
        return self.__id

    def obtenerPonderacion(self, vecino):
        return self.__conexiones.get(vecino)

class Grafo:
    def __init__(self):
        self.__vertices = {}

    def __len__(self):
        return len(self.__vertices)

    def agregarVertice(self, clave):
        if clave not in self.__vertices:
            nuevo_vertice = Vertice(clave)
            self.__vertices[clave] = nuevo_vertice
        return self.__vertices[clave]

    def obtenerVertice(self, clave):
        return self.__vertices.get(clave)

    def __contains__(self, clave):
        return clave in self.__vertices

    def agregarArista(self, desde_clave, hasta_clave, ponderacion = 0):
        if desde_clave not in self.__vertices:
            self.agregarVertice(desde_clave)
        if hasta_clave not in self.__vertices:
            self.agregarVertice(hasta_clave)
        vertice_desde = self.__vertices[desde_clave]
        vertice_hasta = self.__vertices[hasta_clave]

    def obtenerVertices(self):
        """Devuelve una lista con las claves (aldeas)"""
        return list(self.__vertices.keys())

    def __iter__(self):
        return iter(self.__vertices.values())
    
if __name__ == '__main__':
    g = Grafo()
    for i in range(6):
        g.agregarVertice(i)
    print(g.obtenerVertices())