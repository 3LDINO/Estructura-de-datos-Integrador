from collections import deque


def orden_topologico(grafo):
    """
    Algoritmo de ordenamiento topologico

    Sirve para ordenar nodos segun dependencias
    """

    # Diccionario de grados de entrada
    grado = {nodo: 0 for nodo in grafo}

    # Se calculan los grados de entrada
    for nodos in grafo.values():
        for destino in nodos:
            grado[destino] += 1

    # Cola inicial con nodos sin dependencia
    cola = deque([n for n in grado if grado[n] == 0])
    orden = []

    while cola:
        actual = cola.popleft()
        orden.append(actual)

        # Se reducen los grados de los vecinos
        for vecino in grafo[actual]:
            grado[vecino] -= 1
            if grado[vecino] == 0:
                cola.append(vecino)

    # Resultado final del ordenamiento
    return orden
