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

    def mostrar(self, nivel=0):
        """
        Busqueda recursiva de una habilidad por nombre

        TIPO:
        DFS (Depth First Search, I.E, la busqueda de un arbol es a lo largo de cada rama antes de pasar a la siguiente bifurcacion) 

        FUNCION:
        Devuelve el nodo si lo encuentra,
        None si no existe.
        """
        print(" " * nivel + self.nombre)
        for m in self.mejoras:
            m.mostrar(nivel + 2)
