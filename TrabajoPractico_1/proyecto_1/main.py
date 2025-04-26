import random
import timeit
from matplotlib import pyplot as plt 
from modules.burbuja import ordenamientoBurbuja
from modules.quicksort import ordenamientoRapido
from modules.radixsort import ordenamientoPorResiduos

CANTIDAD = 5000

print("* INICIO")

enes = list(range(250,CANTIDAD+1,250))
# listas para guardar los tiempos de ordenamiento para los distintos 'enes'
tiempos_burbuja = []
tiempos_radixsort = []
tiempos_quicksort = []
numeros = [random.randint(10000,99999) for _ in range(CANTIDAD)]
for n in enes:
    lista_burbuja = numeros[0:n].copy()
    medidor = timeit.Timer("ordenamientoBurbuja(lista_burbuja)","from __main__ import ordenamientoBurbuja,lista_burbuja")
    tiempo = medidor.timeit(number=1)
    tiempos_burbuja.append(tiempo)
    print(f'n: {n:4d} - {tiempo:.4f} s', end= '   ')


    lista_quicksort = numeros[0:n].copy()
    medidor = timeit.Timer("ordenamientoRapido(lista_quicksort)","from __main__ import ordenamientoRapido,lista_quicksort")
    tiempo = medidor.timeit(number=1)
    tiempos_quicksort.append(tiempo)
    print(f'{tiempo:.4f} s')


    lista_radixsort = numeros[0:n].copy()
    medidor = timeit.Timer("ordenamientoPorResiduos(lista_radixsort)","from __main__ import ordenamientoPorResiduos,lista_radixsort")
    tiempo = medidor.timeit(number=1)
    tiempos_radixsort.append(tiempo)
    print(f'{tiempo:.4f} s', end='   ')   

# Gráfico con los pares (n,tiempo) obtenidos
figura,ejes = plt.subplots()
ejes.plot(enes,tiempos_burbuja, 'bo-', enes, tiempos_quicksort, 'go-', enes, tiempos_radixsort, 'mx-')
ejes.set_title("Comparación de tiempos de ordenamiento")
ejes.legend(["Burbuja","Quicksort","PorResiduos"])
ejes.set_xlabel("Cantidad de elementos (n)")
ejes.set_ylabel("Tiempo (s)")
plt.grid()
plt.show()

print("* FIN")