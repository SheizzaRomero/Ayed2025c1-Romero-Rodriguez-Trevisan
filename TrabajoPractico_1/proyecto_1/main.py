import random,time
from modules.ordenamientoburbuja import ordenamientoBurbuja

print("* INICIO")

enes = [1,50,100,250,500,750,1000]
for n in enes:
    numeros = [random.randint(10000,99999) for i in range(n)]
    inicio = time.thread_time_ns()
    ordenamientoBurbuja(numeros)
    fin = time.thread_time_ns()
    print('n: %(ene)4d - %(tiempo)d ns' % {'ene':n,'tiempo':fin-inicio})

print("* FIN")