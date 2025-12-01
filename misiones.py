import heapq


class Mision:
    """
    Clase que representa una mision

    Cada objeto tiene un nombre y un nivel de prioridad
    Menor valor significa mayor prioridad
    """

    def __init__(self, nombre, prioridad):
        """
        Constructor de la mision

        nombre es el nombre de la mision
        prioridad define que misiones tienen prioridad sobre otras
        """
        self.nombre = nombre
        self.prioridad = prioridad

    def __lt__(self, otra):
        """
        Metodo de comparacion entre misiones

        Permite que el heap ordene por prioridad
        """
        return self.prioridad < otra.prioridad


class ColaMisiones:
    """
    Clase que representa una cola de prioridad

    Usa un heap como estructura interna
    """

    def __init__(self):
        """
        Inicializa la cola vacia
        """
        self.cola = []

    def agregar(self, mision):
        """
        Agrega una mision a la cola

        Usa heap para mantener el orden
        """
        heapq.heappush(self.cola, mision)

    def atender(self):
        """
        Devuelve mision mas prioritaria
        """
        if self.cola:
            return heapq.heappop(self.cola)
        return None

    def esta_vacia(self):
        """
        Verifica si existen misiones pendientes
        """
        return len(self.cola) == 0
