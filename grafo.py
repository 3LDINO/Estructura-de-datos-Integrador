class Grafo:
    """
    Clase que representa un grafo

    Usa diccionario con listas adyacentes
    """

    def __init__(self):
        """
        Inicializa el grafo vacio
        """
        self.grafo = {}

    def agregar_nodo(self, nodo):
        """
        Agrega un nodo al grafo si no existe
        """
        if nodo not in self.grafo:
            self.grafo[nodo] = []

    def agregar_arista(self, origen, destino):
        """
        Agrega una arista dirigida al grafo
        """
        self.grafo[origen].append(destino)

    def bfs(self, inicio):
        """
        Recorrido en amplitud BFS

        Uso de cola con lista
        """
        visitados = []
        cola = [inicio]

        while cola:
            actual = cola.pop(0)
            if actual not in visitados:
                visitados.append(actual)
                cola.extend(self.grafo[actual])
        return visitados

    def dfs(self, inicio, visitados=None):
        """
        Recorrido en profundidad DFS

        Implementacion recursiva
        """
        if visitados is None:
            visitados = []
        visitados.append(inicio)

        for v in self.grafo[inicio]:
            if v not in visitados:
                self.dfs(v, visitados)
        return visitados
