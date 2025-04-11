import random
import timeit
import matplotlib.pyplot as plt
from modules.burbuja import ordenamientoBurbuja, ordenamientoBurbujacorta
from modules.quicksort import ordenamientoRapido

print("* INICIO")

enes = list(range(250,5001,250))
tiempos = []  # lista para guardar los tiempos medidos para cada 'n'
tiempos_quicksort = [] 
tiempos_burbujacorta = []
numeros = [random.randint(10000,99999) for _ in range(5000)]
for n in enes:
    numero_burbuja  = numeros[0:n].copy ( )
    medidor = timeit.Timer("ordenamientoBurbuja(numero_burbuja)","from __main__ import ordenamientoBurbuja,numero_burbuja")
    tiempo = medidor.timeit(number=1)
    tiempos.append(tiempo)
    print('n: %(ene)4d - %(tiempo)f s' % {'ene':n,'tiempo':tiempo}, end= '     ' )   # simple salida por pantalla


    numero_burbujacorta  = numeros[0:n].copy ( )
    medidor = timeit.Timer("ordenamientoBurbujacorta(numero_burbujacorta)","from __main__ import ordenamientoBurbujacorta,numero_burbujacorta")
    tiempo = medidor.timeit(number=1)
    tiempos_burbujacorta.append(tiempo)
    print(' %(tiempo)f s' % {'tiempo':tiempo}, end= '     ' )   # simple salida por pantalla


    numero_quicksort = numeros[0:n].copy ()
    medidor = timeit.Timer("ordenamientoRapido(numero_quicksort)","from __main__ import ordenamientoRapido,numero_quicksort")
    tiempo = medidor.timeit(number=1)
    tiempos_quicksort.append (tiempo)
    print (" %(tiempo)f s" % {'tiempo':tiempo})


# Gráfico con los pares (n,tiempo) obtenidos
figura,ejes = plt.subplots()
ejes.plot(enes,tiempos,'bo-' , enes, tiempos_quicksort, 'go-', enes, tiempos_burbujacorta, 'mx-')
ejes.set_title ("Comparación de tiempos de ordenamiento")
ejes.legend (["Burbuja", "Quicksort","BurbujaCorta"])
ejes.set_xlabel ("Cantidad de elementos (n)")
ejes.set_ylabel("Tiempo (s)")
plt.grid()
plt.show()

print("* FIN")
