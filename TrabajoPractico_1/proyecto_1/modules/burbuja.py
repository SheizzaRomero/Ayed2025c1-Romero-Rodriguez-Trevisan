import random

def ordenamientoBurbuja(unaLista):
    for pasada in range(len(unaLista)-1, 0, -1):
        for i in range(pasada):
            if unaLista[i] > unaLista[i+1]:
                unaLista[i],unaLista[i+1] = unaLista[i+1],unaLista[i]
def ordenamientoBurbujacorta(unaLista):
    intercambios = True
    numero_pasada = len (unaLista)-1
    while numero_pasada > 0 and intercambios:
        intercambios = False

    for i in range(numero_pasada):
            
        if unaLista[i] > unaLista[i+1]:
            intercambios = True
            unaLista[i],unaLista[i+1] = unaLista[i+1],unaLista[i]               

if __name__ == "__main__": 
    ensayo = [random.randint(10000,99999) for i in range(500)]
    print(ensayo)
    ordenamientoBurbuja(ensayo)
    print(ensayo)