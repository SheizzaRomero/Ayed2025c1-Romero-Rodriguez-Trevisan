class MonticuloBinario:
    def __init__ (self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0

    def infiltrarArriba (self,i):
        while i // 2 > 0:
            if self.listaMonticulo [i] < self.listaMonticulo [i // 2]:
                tmp = self.listaMonticulo [i // 2]
                self.listaMonticulo [i // 2] =  self.listaMonticulo [i]
                self.listaMonticulo [i] =  tmp
            i = i // 2

    def __str__(self):
        lista =  []
        for cosa in self.listaMonticulo [1:]:
            lista.append (str(cosa))
        return ' - '.join (lista)
    
    def __len__ (self):
        return self.tamanoActual
    
    def __iter__(self): 
        self.__puntero = 1 
        return self
    
    def __next__(self):
        if self.__puntero == self.tamanoActual - 1:
            raise StopIteration()
        dato = self.listaMonticulo [self.__puntero]
        self.__puntero = self.__puntero + 1
        return dato
    
    def insertar (self, k):
        self.listaMonticulo.append (k)
        self.tamanoActual = self.tamanoActual + 1 
        self.infiltrarArriba (self.tamanoActual)

    def infiltrarAbajo(self,i):
         while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i] > self.listaMonticulo[hm]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm

    def hijoMin(self,i):          
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
        
    def eliminarMinimo (self):
        valorSacado = self.listaMonticulo [1]
        self.listaMonticulo [1] = self.listaMonticulo [self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop ()
        self.infiltrarAbajo (1)
        return valorSacado
    
    def construirMonticulo(self,unaLista):
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [0] + unaLista[:]
        while (i > 0):
            self.infiltrarAbajo(i)
            i = i - 1
if __name__ == "__main__": 
    pass 
