class Habilidad:
    """
    Clase que representa una habilidad de un pesonaje

    Cada objeto es un nodo de un arbol general
    Tiene un nombre y una lista de mejoras
    """

    def __init__(self, nombre):
        """
        Constructor del nodo habilidad

        nombre es el nombre de la habilidad
        mejoras es una lista de nodos hijos
        """
        self.nombre = nombre
        # Lista de mejoras de la habilidad
        self.mejoras = []

    def agregar_mejora(self, habilidad):
        """
        Agrega una habilidad como mejora

        Aplica estructura de arbol general
        """
        self.mejoras.append(habilidad)

    def buscar(self, nombre):
        """
        Busca una habilidad por nombre recorriendo el arbol
        """
        if self.nombre == nombre:
            return self

        for mejora in self.mejoras:
            resultado = mejora.buscar(nombre)
            if resultado:
                return resultado
        return None

    def mostrar(self, nivel=0):
        """
        Busqueda recursiva de una habilidad por nombre

        TIPO:
        DFS (Depth First Search, I.E, la busqueda de un arbol es a lo largo de cada rama antes de pasar a la siguiente bifurcacion) 

        FUNCION:
        Devuelve el nodo si lo encuentra,
        None si no existe.
        """
        print("  " * nivel + self.nombre)
        for mejora in self.mejoras:
            mejora.mostrar(nivel + 1)

    def construir_grafo(self, grafo):
        """
        Convierte el arbol en un grafo dirigido para orden topologico
        """
        if self.nombre not in grafo:
            grafo[self.nombre] = []

        for mejora in self.mejoras:
            grafo[self.nombre].append(mejora.nombre)
            mejora.construir_grafo(grafo)


class ArbolHabilidades:
    """
    TAD completo que gestiona el arbol de habilidades
    """

    def __init__(self):
        # raiz del arbol
        self.raiz = None

    def agregar_base(self, nombre):
        """
        Crea la habilidad raiz del arbol
        """
        if self.raiz is None:
            self.raiz = Habilidad(nombre)

    def agregar_mejora(self, base, nueva):
        """
        Agrega una mejora a una habilidad existente
        """
        if self.raiz is None:
            return

        nodo = self.raiz.buscar(base)
        if nodo:
            nodo.agregar_mejora(Habilidad(nueva))

    def mostrar(self):
        """
        Muestra el arbol completo
        """
        if self.raiz:
            self.raiz.mostrar()
        else:
            print("No hay habilidades")

    def buscar(self, nombre):
        """
        Busca una habilidad por nombre
        """
        if self.raiz:
            return self.raiz.buscar(nombre)
        return None

    def obtener_grafo(self):
        """
        Devuelve estructura lista para orden topologico
        """
        grafo = {}

        if self.raiz:
            self.raiz.construir_grafo(grafo)

        return grafo
