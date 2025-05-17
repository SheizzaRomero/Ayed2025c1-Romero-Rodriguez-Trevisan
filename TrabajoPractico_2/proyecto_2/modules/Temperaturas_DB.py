
from modules.AVL import ArbolBinarioBusqueda_AVL

class Temperaturas_DB:
    def __init__(self):
        self.arbol = ArbolBinarioBusqueda_AVL()

    def guardar_temperatura(self, temperatura, fecha_obj):
        self.arbol[fecha_obj] = temperatura

    def obtener_temperatura(self, fecha_obj):
        try:
            return self.arbol[fecha_obj]
        except KeyError:
            return None  # O lo que quieras devolver si no existe la fecha

    # Opcional: si querés borrar una temperatura
    def borrar_temperatura(self, fecha_obj):
        try:
            del self.arbol[fecha_obj]
        except KeyError:
            pass
