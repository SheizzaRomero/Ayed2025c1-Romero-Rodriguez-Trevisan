import csv
from modules.grafo import Grafo
from modules.lib import prim

print('\n*** INICIO')

mapa = Grafo()

with open('data/aldeas.txt', encoding='utf-8') as archivo:
    datos = csv.reader(archivo)
    for dato in datos:
        mapa.agregarArista(dato[0].strip(), (dato[1]).strip(), int(dato[2]))   # origen, destino, distancia
print('+ datos cargados')

print('\n----------')
print('+ aldeas ordenadas alfabeticamente:')
lista = list(mapa.obtenerVertices())
lista.sort()
print(lista)

print('\n----------')
print('+ listado de aldeas con su predecesora')
prim(mapa, 'Peligros')
distancia_total = 0
for nombre in lista:
    aldea = mapa.obtenerVertice(nombre)
    distancia = aldea.obtenerDistancia()
    if distancia == 0:
        print(f'{nombre} es el punto de partida')
    else:
        print(f'{nombre} recibe de {aldea.obtenerPredecesor()}')
        distancia_total += distancia

print('\n----------')
print('+ listado de aldeas y sus conexiones')
for nombre in lista:
    print(f'* {nombre} puede enviar a:')
    for conexion in mapa.obtenerVertice(nombre).obtenerConexiones():
        print(f'\t{conexion}')

print('\n----------')
print('+ la suma de todas las distanicas recorridas por las palomas es', distancia_total, ';)')

print('\n*** FIN')