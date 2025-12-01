# clase


class NodoPoder:
    """
    Nodos del Arbol Binario

    Cada nodo representa un personaje y posee:
    - Un valor principal (personaje)
    - Un hijo izquierdo
    - Un hijo derecho
    """

    def __init__(self, personaje):
        """
        Constructor del nodo

        PARAMETRO:
        personaje (Personaje): Objeto de clase Personaje

        FUNCION:
        Crear una unidad basica del árbol
        """

        # personaje almacenado
        self.personaje = personaje

        # hijo izquierdo menor poder
        self.izquierda = None

        # hijo derecho mayor poder
        self.derecha = None


class ArbolPoder:
    """
    Clase que representa un Arbol Binario de Búsqueda 
    (el arbol donde los nodos izquierdos son menores a la raiz y los derechos son mayores a la raiz)
    organizado según el nivel de poder del personaje

    ORGANIZACION:
    - Izquierda: menor poder
    - Derecha: mayor o igual poder
    """

    def __init__(self):
        """
        Inicia el arbol vacío
        """
        self.raiz = None

    def agregar_personaje(self, personaje):
        """
        Inserta personaje segun nivel de poder
        """
        nodo = NodoPoder(personaje)

        if self.raiz is None:
            self.raiz = nodo
        else:
            self._insertar(self.raiz, nodo)

    def _insertar(self, actual, nuevo):
        """
        Inserción recursiva dentro del arbol

        PARAMETROS:
        nodo (que viene de la clase NodoArbol): raiz del subarbol
        personaje (Personaje)

        FUNCION:
        - Si no hay nodo → se crea uno nuevo.
        - Si es menor → va a izquierda.
        - Si es mayor o igual → va a derecha.
            (es un arbol de busqueda despues de todo)
        """

        if nuevo.personaje.poder < actual.personaje.poder:
            if actual.izquierda is None:
                actual.izquierda = nuevo
            else:
                self._insertar(actual.izquierda, nuevo)
        else:
            if actual.derecha is None:
                actual.derecha = nuevo
            else:
                self._insertar(actual.derecha, nuevo)

    def buscar_por_poder(self, poder):
        """
        Busca personaje usando el arbol
        """
        return self._buscar(self.raiz, poder)

    def _buscar(self, actual, poder):
        """
        Busqueda recursiva
        """
        if actual is None:
            return None

        if actual.personaje.poder == poder:
            return actual.personaje

        if poder < actual.personaje.poder:
            return self._buscar(actual.izquierda, poder)
        else:
            return self._buscar(actual.derecha, poder)

    def mostrar(self):
        """
        Muestra personajes ordenados por poder
        """
        self._inorden(self.raiz)

    def _inorden(self, actual):
        """
        Recorrido inorden
        """
        if actual:
            self._inorden(actual.izquierda)
            print(actual.personaje)
            self._inorden(actual.derecha)

    def preorden(self):
        """
        Recorrido preorden
        """
        self._preorden(self.raiz)

    def _preorden(self, actual):
        """
        Recorrido previo a hijos
        """
        if actual:
            print(actual.personaje)
            self._preorden(actual.izquierda)
            self._preorden(actual.derecha)

    def postorden(self):
        """
        Recorrido postorden
        """
        self._postorden(self.raiz)

    def _postorden(self, actual):
        """
        Recorrido posterior a hijos
        """
        if actual:
            self._postorden(actual.izquierda)
            self._postorden(actual.derecha)
            print(actual.personaje)
