import heapq


def dijkstra(grafo, inicio):
    """
    Algoritmo de Dijkstra

    Calcula la distancia minima desde el nodo inicial
    """

    # Diccionario de distancias
    # Cada nodo inicia con infinito
    distancias = {n: float("inf") for n in grafo}

    # La distancia al origen es cero
    distancias[inicio] = 0

    # Cola de prioridad usando heap
    cola = [(0, inicio)]

    while cola:
        distancia_actual, nodo = heapq.heappop(cola)

        # Si la distancia es mayor no se procesa
        if distancia_actual > distancias[nodo]:
            continue

        # Se recorren los vecinos del nodo actual
        for vecino, costo in grafo[nodo]:
            nueva = distancia_actual + costo

            # Si se encuentra una mejor ruta se actualiza
            if nueva < distancias[vecino]:
                distancias[vecino] = nueva
                heapq.heappush(cola, (nueva, vecino))

    # Se devuelve el diccionario de distancias
    return distancias
