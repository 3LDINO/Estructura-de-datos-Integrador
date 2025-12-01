from collections import deque


def orden_topologico(grafo):
    """
    Ordena nodos respetando dependencias
    """

    # calcular grados de entrada
    grado = {}

    for nodo in grafo:
        grado[nodo] = 0

    for origen in grafo:
        for destino in grafo[origen]:
            grado[destino] += 1

    # nodos sin dependencias
    cola = deque()

    for nodo in grado:
        if grado[nodo] == 0:
            cola.append(nodo)

    resultado = []

    while cola:

        actual = cola.popleft()
        resultado.append(actual)

        for vecino in grafo.get(actual, []):
            grado[vecino] -= 1
            if grado[vecino] == 0:
                cola.append(vecino)

    return resultado
