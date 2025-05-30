import csv
from modules.grafo import Grafo

mapa = Grafo()

with open('data/aldeas.txt', encoding='utf-8') as archivo:
    lista = csv.reader(archivo)
    for fila in lista:
        print(', '.join(fila))
        mapa.agregarArista(fila[0].strip(), (fila[1]).strip(), int(fila[2]))

print('cantidad de vertices:', len(mapa))
lista = mapa.obtenerVertices()
print(sorted(lista))

for aldea in mapa.obtenerVertices():
    print(f'{aldea} puede recibir de:')
    for cnx in mapa.obtenerVertice(aldea).obtenerConexiones():
        print(f'\t{cnx}')
