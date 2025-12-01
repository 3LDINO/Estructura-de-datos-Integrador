import heapq


def dijkstra(grafo, inicio):
    """
    Algoritmo de camino minimo
    """

    # diccionario nodo -> distancia minima
    distancias = {}

    for nodo in grafo:
        distancias[nodo] = float("inf")

    distancias[inicio] = 0

    # heap de prioridad
    cola = [(0, inicio)]

    while cola:

        distancia_actual, actual = heapq.heappop(cola)

        # si existe camino mejor se ignora
        if distancia_actual > distancias[actual]:
            continue

        # recorrer vecinos
        for vecino, costo in grafo.get(actual, []):

            nueva = distancia_actual + costo

            # mejorar distancia
            if nueva < distancias[vecino]:
                distancias[vecino] = nueva
                heapq.heappush(cola, (nueva, vecino))

    return distancias
