import random 

def ordenamientoRapido (lista, primero, ultimo):
    if primero<ultimo:
         p = particion (lista, primero, ultimo)
         ordenamientoRapido (lista, primero, p - 1)
         ordenamientoRapido (lista, p + 1, ultimo)
def particion (lista, primero, ultimo):
     pivote = lista[ultimo]
     i = primero - 1
     for j in range (primero, ultimo): #recore desde primero hasta antes del pivote
         if lista [j] <= pivote:       #si el elemento el menor o igual al pivote, lo intercambiamos hacia la izq
              i = i + 1
              lista [i], lista [j] = lista [j], lista [i]
     lista [i + 1], lista [ultimo] = lista [ultimo], lista [i + 1]
     return i + 1 #posicion final del pivote 

if __name__ == "__main__":
   ensayo = [random.randint (10000,99999) for i in range(500)]
print (ensayo) 
ordenamientoRapido (ensayo, 0, len(ensayo)- 1)
print (ensayo)


 
