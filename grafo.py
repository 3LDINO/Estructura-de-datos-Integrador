class Grafo:
    """
    Clase que representa un grafo

    Usa diccionario con listas adyacentes
    """

    def __init__(self):
        """
        Inicializa el grafo vacio
        """
        self.adyacencia = {}

    def agregar_nodo(self, nodo):
        """
        Agrega un nodo al grafo si no existe
        """
        if nodo not in self.adyacencia:
            self.adyacencia[nodo] = []

    def agregar_arista(self, origen, destino):
        """
        Conecta dos nodos existentes
        """
        if origen not in self.adyacencia:
            self.agregar_nodo(origen)

        if destino not in self.adyacencia:
            self.agregar_nodo(destino)

        if destino not in self.adyacencia[origen]:
            self.adyacencia[origen].append(destino)

        if origen not in self.adyacencia[destino]:
            self.adyacencia[destino].append(origen)

    def bfs(self, inicio):
        """
        Recorrido en amplitud BFS

        Uso de cola con lista
        """
        visitados = set()
        cola = [inicio]
        resultado = []

        visitados.add(inicio)

        while cola:
            actual = cola.pop(0)
            resultado.append(actual)

            for vecino in self.adyacencia.get(actual, []):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)

        return resultado

    def dfs(self, inicio):
        """
        Recorrido en profundidad
        """
        visitados = set()
        resultado = []
        self._dfs_rec(inicio, visitados, resultado)
        return resultado

    def _dfs_rec(self, actual, visitados, resultado):
        """
        DFS recursivo
        """
        if actual in visitados:
            return

        visitados.add(actual)
        resultado.append(actual)

        for vecino in self.adyacencia.get(actual, []):
            self._dfs_rec(vecino, visitados, resultado)
