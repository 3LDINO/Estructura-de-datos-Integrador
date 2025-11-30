# clase


class NodoArbol:
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
        self.personaje = personaje
        self.izquierda = None
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

    def insertar(self, personaje):
        """
        Inserta un personaje en el arbol

        MECANISMO:
        Llama a una funcion recursiva
        que encuentra su lugar correcto
        """
        self.raiz = self._insertar(self.raiz, personaje)

    def _insertar(self, nodo, personaje):
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

        # Si llegamos a una hoja vacía
        if nodo is None:
            return NodoArbol(personaje)

        # Comparación según poder
        if personaje.get_poder() < nodo.personaje.get_poder():
            nodo.izquierda = self._insertar(nodo.izquierda, personaje)
        else:
            nodo.derecha = self._insertar(nodo.derecha, personaje)
        return nodo

    def inorden(self, nodo):
        """
        Recorrido Inorden (izquierda - raiz - derecha)

        RESULTADO:
        Imprime los personajes ordenados por poder

        FUNCION:
        Mostrar personajes desde menor a mayor poder

        COMPLEJIDAD:
        O(n) - visita todos los nodos
        """
        if nodo:
            self.inorden(nodo.izquierda)
            print(f"{nodo.personaje.nombre} - Poder {nodo.personaje.get_poder()}")
            self.inorden(nodo.derecha)

    # PREORDEN
    def preorden(self, nodo):
        """
        Recorrido Preorden (raiz - izquierda - derecha)
        """
        if nodo:
            print(nodo.personaje.nombre)
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)

    # POSTORDEN
    def postorden(self, nodo):
        """
        Recorrido Postorden (izquierda - derecha - raiz)
        """
        if nodo:
            self.postorden(nodo.izquierda)
            self.postorden(nodo.derecha)
            print(nodo.personaje.nombre)

    def buscar(self, nodo, nombre):
        """
        Busca un personaje por su nombre
        """
        if nodo is None:
            return None
        if nodo.personaje.nombre == nombre:
            return nodo.personaje

        encontrado = self.buscar(nodo.izquierda, nombre)
        if encontrado:
            return encontrado
        return self.buscar(nodo.derecha, nombre)

    def buscar(self, poder, nodo):
        """
        Busca un personaje según nivel de poder

        FUNCION:
        Búsqueda típica de árbol binario
        """

        if nodo is None:
            return None

        if poder == nodo.personaje.get_poder():
            return nodo.personaje

        elif poder < nodo.personaje.get_poder():
            return self.buscar(poder, nodo.izquierda)
        else:
            return self.buscar(poder, nodo.derecha)
