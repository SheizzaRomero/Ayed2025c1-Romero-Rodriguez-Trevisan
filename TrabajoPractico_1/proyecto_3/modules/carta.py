# -*- coding: utf-8 -*-
"""
Created on Tue Aug  9 16:51:54 2022

@author: Cátedra de Algoritmos y Estructura de Datos
"""

class Carta:
    
    def __init__(self, valor='', palo=''):
        self.__valor = valor
        self.__palo = palo
        self.__visible = False
        
    @property
    def visible(self):
        return self.__visible
        
    @visible.setter
    def visible(self, visible):
        self.__visible = visible
        
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor
        
    @property
    def palo(self):
        return self.__palo
    
    @palo.setter
    def palo(self, palo):
        self.__palo = palo  
    
    def _valor_numerico(self):
        salida = 0
        valores = ['J','Q','K','A']
        if self.__valor in valores:
            idx = valores.index(self.__valor)
            salida = 11 + idx
        else:
            salida = int(self.__valor)
        return salida

    def __gt__(self, otra):
        """2 cartas deben compararse por su valor numérico"""
        return self._valor_numerico() > otra._valor_numerico()
        
    def __str__(self):
        salida = '-X'
        if self.__visible:
            salida = self.__valor + self.__palo
        return salida
    
    def __repr__(self):
        return str(self)
    
    
if __name__ == "__main__":
    carta = Carta("♣", "3")
    print(carta)
    carta.visible = True
    print(carta)