import random
import timeit
import matplotlib.pyplot as plt
from modules.burbuja import ordenamientoBurbuja

print("* INICIO")

enes = list(range(250,5001,250))
tiempos = []   # lista para guardar los tiempos medidos para cada 'n'
for n in enes:
    numeros = [random.randint(10000,99999) for i in range(n)]
    medidor = timeit.Timer("ordenamientoBurbuja(numeros)","from __main__ import ordenamientoBurbuja,numeros")
    tiempo = medidor.timeit(number=1)
    tiempos.append(tiempo)
    print('n: %(ene)4d - %(tiempo)d s' % {'ene':n,'tiempo':tiempo})   # simple salida por pantalla

# Gráfico con los pares (n,tiempo) obtenidos
figura,ejes = plt.subplots()
ejes.plot(enes,tiempos,'bo')
ejes.set_title ("Tiempo de ejecución del ordenamiento burbuja")
ejes.set_xlabel ("Cantidad de elementos (n)")
ejes.set_ylabel("Tiempo (s)")
plt.grid()
plt.show()

print("* FIN")