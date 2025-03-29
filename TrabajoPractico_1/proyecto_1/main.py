import random,time
import matplotlib.pyplot as plt
from modules.ordenamientoburbuja import ordenamientoBurbuja

print("* INICIO")

enes = [1,50,100,250,500,750,1000,2500]   # lista con los distintos 'n' a probar
tiempos = []   # lista para guardar los tiempos medidos para cada 'n'
for n in enes:
    numeros = [random.randint(10000,99999) for i in range(n)]   # lista con 'n' valores de cinco cifras
    # llamada a la rutina de ordenamiento entre dos 'thread_time_ns'
    inicio = time.thread_time_ns()
    ordenamientoBurbuja(numeros)
    fin = time.thread_time_ns()
    diferencia = fin - inicio
    tiempos.append(diferencia)   # tiempo transcurrido se agrega a la lista
    print('n: %(ene)4d - %(tiempo)d ns' % {'ene':n,'tiempo':diferencia})   # simple salida por pantalla

# dibujito con los pares (n,tiempo) obtenidos
figura,ejes = plt.subplots()
ejes.plot(enes,tiempos,'bo')
plt.show()

print("* FIN")