import csv
import heapq
import os

from modules.grafo import Grafo

def leer_datos_aldeas(ruta_archivo, grafo_mapa):
    nombres_aldeas_unicas = set()
    try:
        with open(ruta_archivo, encoding="utf-8") as archivo:
            lector_csv = csv.reader(archivo)
            for i, fila in enumerate(lector_csv):
                fila_limpia = [celda.strip() for celda in fila if celda.strip()]

                if len (fila_limpia) == 3:
                    origen, destino, dist_str = fila_limpia[0], fila_limpia[1], fila_limpia[2]
                    try:
                        distancia = int(dist_str)
                        if distancia <= 0:
                            print (f"Advertencia: Distancia no positiva en linea {i+1}: {fila}. Se omite")
                            continue
                        grafo_mapa.agregarArista(origen, destino, distancia)
                        nombres_aldeas_unicas.add(origen)
                        nombres_aldeas_unicas.add(destino)
                    except ValueError:
                        print(f"Advertencia: Distancia inválida en línea {i+1}: {fila}. Se omite")
                elif len(fila_limpia) == 1:
                    nombre_aldea = fila_limpia[0]
                    if nombre_aldea not in grafo_mapa:
                        grafo_mapa.agregarVertice(nombre_aldea)
                    nombres_aldeas_unicas.add(nombre_aldea)
                elif fila_limpia:
                    print(f"Advertencia: Linea mal formada o incompleta {i+1}: {fila}. Se omite")
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo de datos en '{ruta_archivo}'.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo {e}")
        return None
    return nombres_aldeas_unicas   

def encontrar_mst_prim(grafo_mapa, aldea_inicio):
    if aldea_inicio not in grafo_mapa:
        print(f"Error: La aldea de inicio '{aldea_inicio}' no existe el mapa.")
        return None, None, 0
    
    padres = {}
    hijos = {nombre: [] for nombre in grafo_mapa.obtenerVertices()}
    distancias_mst = {}

    visitados = set()
    cola_prioridad = []

    distancia_total_mst = 0

    # Iniciar desde la aldea_inicio
    visitados.add(aldea_inicio)
    vertice_actual_obj = grafo_mapa.obtenerVertice(aldea_inicio)

    if not vertice_actual_obj:
        print(f"Error: No se pudo obtener el objeto vértice para '{aldea_inicio}'.")
        return None, None, 0
    
    for vecino_obj in vertice_actual_obj.obtenerConexiones():
        peso = vertice_actual_obj.obtenerPonderacion(vecino_obj)
        heapq.heappush(cola_prioridad, (peso, vecino_obj.obtenerId(), aldea_inicio))
    
    while cola_prioridad and len(visitados) < len(grafo_mapa):
        costo, aldea_actual_id, aldea_previa_id = heapq.heappop(cola_prioridad)
    
        if aldea_actual_id in visitados:
            continue

        visitados.add(aldea_actual_id)
        padres[aldea_actual_id] = aldea_previa_id
        distancias_mst[aldea_actual_id] = costo
        if aldea_previa_id in hijos:
            hijos[aldea_previa_id].append(aldea_actual_id)
        distancia_total_mst += costo

        vertice_actual_obj = grafo_mapa.obtenerVertice(aldea_actual_id)
        if vertice_actual_obj:
            for vecino_obj in vertice_actual_obj.obtenerConexiones():
                if vecino_obj.obtenerId() not in visitados:
                    peso = vertice_actual_obj.obtenerPonderacion(vecino_obj)
                    heapq.heappush(cola_prioridad, (peso, vecino_obj.obtenerId(), aldea_actual_id))
    
    for aldea in hijos:
        hijos[aldea].sort()
    
    if len(visitados) < len(grafo_mapa.obtenerVertices()):
        print("Advertencia: No todas las aldeas fueron alcanzadas. El grafo podría estar desconectado.")
        aldeas_mapa = set(grafo_mapa.obtenerVertices())
        no_visitadas = aldeas_mapa - visitados
        if no_visitadas:
            print(f"Aldeas no alcanzadas: {sorted(list(no_visitadas))}")
    
    return padres, hijos, distancia_total_mst

def main():
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo_aldeas = os.path.join(directorio_actual, 'data', 'aldeas.txt')

mapa_aldeas = Grafo()
nombres_aldeas = leer_datos_aldeas(ruta_archivo_aldeas, mapa_aldeas)

if nombres_aldeas is None or not mapa_aldeas.obtenerVertices:
        print("No se pudieron cargar los datos de las aldeas. Abortando.")
        return

print('Cantidad de vertices en el mapa:', len(mapa_aldeas.obtenerVertices()))
print('Aldeas en el mapa:', sorted(list(mapa_aldeas.obtenerVertices())))

print("\nDetalle de conexiones:")

for aldea in mapa_aldeas.obtenerVertices():
        print(f'{aldea} conectado a:')
        vertex_obj = mapa_aldeas.obtenerVertice(aldea)
        if vertex_obj:
            for cnx in vertex_obj.obtenerConexiones():
                print(f'\t- {cnx.obtenerId()} (distancia: {vertex_obj.obtenerPonderacion(cnx)})')
        else:
            print(f'\t- No se pudo obtener el objeto vértice para {aldea}') # Should not happen if loaded correctly

print("---")

aldea_origen_noticias = "Peligros"

if aldea_origen_noticias not in mapa_aldeas.obtenerVertices():
        print(f"Error: La aldea de origen '{aldea_origen_noticias}' no se encuentra en los datos.")
        # Verificar si el nombre está en la lista general de nombres por si no se añadió al grafo
        if nombres_aldeas and aldea_origen_noticias not in nombres_aldeas:
             print(f"'{aldea_origen_noticias}' tampoco fue encontrada en las listas de conexiones.")
        return

print(f"Calculando la ruta de distribución más eficiente desde: {aldea_origen_noticias}")
print(f"Total de aldeas en el sistema: {len(mapa_aldeas.obtenerVertices())}")
print("---")

padres_mst, hijos_mst, distancia_total = encontrar_mst_prim(mapa_aldeas, aldea_origen_noticias)

if padres_mst is None:
    print("No se pudo calcular la ruta de distribución. Verifique el origen o la conectividad del grafo.")
    return

lista_aldeas_ordenada = sorted(list(mapa_aldeas.obtenerVertices()))
print("## Lista de Aldeas (Total: " + str(len(lista_aldeas_ordenada)) + ")")
for i, nombre_aldea in enumerate(lista_aldeas_ordenada):
        print(f"{i+1}. {nombre_aldea}")
print("---")

print("## Plan de Distribución de Noticias")
for aldea in lista_aldeas_ordenada:
    print(f"Aldea: {aldea}")

    recibe_de = "Origen de la noticia"
    if aldea == aldea_origen_noticias:
            recibe_de = "Es la fuente original (Peligros)"
    elif aldea in padres_mst:
            recibe_de = padres_mst[aldea]
    else:
            recibe_de = "No recibe (posiblemente no alcanzada por la ruta de distribución)"

    print(f"  Recibe de: {recibe_de}")

    envia_a_lista = hijos_mst.get(aldea, [])
    if envia_a_lista:
            print(f"  Envía réplicas a: {', '.join(envia_a_lista)}")
    else:
            print("  Envía réplicas a: Nadie (es un punto final en esta ruta de distribución o no tiene hijos en el MST)")
    print() # Espacio entre aldeas
print("---")

print("## Eficiencia del Envío")
print(f"Suma total de las distancias recorridas por las palomas (en leguas): {distancia_total}")
print("---")

if __name__ == '__main__':
    main()