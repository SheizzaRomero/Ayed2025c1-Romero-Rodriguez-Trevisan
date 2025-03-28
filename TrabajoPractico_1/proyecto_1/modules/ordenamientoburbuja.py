# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
import random
def ordenamientoBurbuja(unalista):
    for pasada in range (len (unalista)-1, 0, -1):
        for i in range (pasada):
            if unalista [i]>unalista[i+1]:
                temp = unalista [i]
                unalista[i]= unalista [i+1]
                unalista [i+1]=temp
if __name__== "main": 
    unalista = [ ] 
    for i in range (500): 
        unalista.append (random.randint(10000,99999))
    print (unalista)
    ordenamientoBurbuja (unalista)
    print (unalista)
