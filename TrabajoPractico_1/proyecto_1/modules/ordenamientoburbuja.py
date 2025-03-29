import random

def ordenamientoBurbuja(unaLista):
    for pasada in range(len(unaLista)-1, 0, -1):
        for i in range(pasada):
            if unaLista[i] > unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp

if __name__ == "__main__": 
    ensayo = []
    for i in range(500): 
        ensayo.append(random.randint(10000,99999))
    print(ensayo)
    ordenamientoBurbuja(ensayo)
    print(ensayo)