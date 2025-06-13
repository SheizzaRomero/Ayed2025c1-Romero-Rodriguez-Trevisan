
from modules.AVL import ArbolBinarioBusqueda_AVL
from datetime import datetime, timedelta


class Temperaturas_DB:
    def __init__(self):
        self.arbol = ArbolBinarioBusqueda_AVL()

    def guardar_temperatura(self, temperatura, fecha):
        self.arbol[fecha] = temperatura

    def devolver_temperatura(self, fecha):
        try:
            return self.arbol[fecha]
        except KeyError:
            return None  # O lo que quieras devolver si no existe la fecha
    

    def max_temp_rango(self, fecha1, fecha2):
        maximo = -1000
        fecha = fecha1
        while fecha <= fecha2:
            if fecha in self.arbol:
                temp = self.arbol [ fecha ]
                if temp > maximo:
                    maximo = temp
            fecha = fecha + timedelta (1)
        return maximo 


    def min_temp_rango(self, fecha1, fecha2):
        minimo = 1000
        fecha = fecha1
        while fecha <= fecha2:
            if fecha in self.arbol:
                temp = self.arbol [fecha]
                if temp < minimo:
                    minimo = temp
            fecha = fecha + timedelta (1)
        return minimo 
    

    def temp_extremos_rango (self, fecha1, fecha2):
        return ( self.min_temp_rango(fecha1, fecha2), self.max_temp_rango (fecha1, fecha2))


    # Opcional: si querés borrar una temperatura
    def borrar_temperatura(self, fecha):
        try:
            del(self.arbol[fecha])
        except KeyError:
            pass

    def devolver_temperaturas (self, fecha1, fecha2):
        resultados = []
        fecha = fecha1
        while fecha <= fecha2:
            if fecha in self.arbol:
                temp = self.arbol[fecha]
                resultados.append(fecha.strftime("%d/%m/%Y") + f":{temp} °C ")
            fecha += timedelta(1)
        return resultados

    def cantidad_muestras (self):
        return len (self.arbol)
    
    def __delitem__(self, clave):
        self.arbol.remover( self.arbol._obtener(clave, self.arbol.raiz) )