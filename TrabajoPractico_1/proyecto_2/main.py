# Aplicación principal
import time
import matplotlib.pyplot as plt
from modules import ListaDobleEnlazada 

def medir_tiempos(funcion, N_valores):
    tiempos = []
    for N in N_valores:
        lista = ListaDobleEnlazada()
        for i in range(N):
            lista.agregar_al_final(i)
        inicio = time.time()
        funcion(lista)
        fin = time.time()
        tiempos.append(fin - inicio)
    return tiempos
N = list(range(1000, 10001, 1000))
tiempos_len = medir_tiempos(lambda l: len(l), N)
tiempos_copiar = medir_tiempos(lambda l: l.copiar(), N)
tiempos_invertir = medir_tiempos(lambda l: l.invertir(), N)

plt.plot(N, tiempos_len, label="len")
plt.plot(N, tiempos_copiar, label="copiar")
plt.plot(N, tiempos_invertir, label="invertir")
plt.set_xlabel("Cantidad de elementos (N)")
plt.set_ylabel("Tiempo (segundos)")
plt.legend()
plt.title("Tiempo de ejecución vs N")
plt.grid(True)
plt.show()
