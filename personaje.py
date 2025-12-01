"""
#Clase Personaje
Aplica Programación Orientada a Objetos (POO) y encapsulamiento.
    Cada objeto de esta clase representa una entidad del universo ficticio
    con características propias, habilidades y transformaciones.
#Datos a manejar: clase personaje (nombre, especie, planeta, nivel_poderm, habilidades, inventario, transformaciones)
# FUNCION:
    Inicializa el objeto con valores iniciales y crea
    las estructuras necesarias para habilidades y transformaciones.
"""


class Personaje:
    def __init__(self, nombre, especie, planeta, nivel_poder):
        self.nombre = nombre
        self.especie = especie
        self.planeta = planeta
        self._nivel_poder = nivel_poder  # Atributo protegido (encapsulado)
        self.habilidades = []           # Lista de habilidades del personaje
        self.inventario = []            # Lista de objetos que posee el personaje
        # Lista de transformaciones (otros personajes)
        self.transformaciones = []

    def get_poder(self):
        """
        Devuelve el nivel de poder base del personaje

        FUNCION:
        Permite leer el valor del atributo protegido sin
        acceder directamente al mismo desde el exterior
        """
        return self._nivel_poder

    def set_poder(self, valor):
        """
        Modifica el nivel de poder del personaje

        FUNCION:
        Evita valores inválidos (como negativos) controlando los datos encapsulados
        """
        if valor >= 0:
            self._nivel_poder = valor

    def agregar_habilidad(self, habilidad):
        """
        FUNCION:
        Permite agregar habilidades (duh).
        """
        self.habilidades.append(habilidad)

    def eliminar_habilidad(self, habilidad):
        """
        FUNCION:
        Permite eliminar habilidades (duh).
        """
        if habilidad in self.habilidades:
            self.habilidades.remove(habilidad)

    def agregar_objeto(self, objeto):
        """
        FUNCION:
        Administra los objetos que posee el personaje
        """
        self.inventario.append(objeto)

    def eliminar_objeto(self, objeto):
        """
        Elimina un objeto del inventario si existe.
        """
        if objeto in self.inventario:
            self.inventario.remove(objeto)

    def agregar_transformacion(self, personaje):
        """
        Agrega una transformacion al personaje (duh)
        FUNCION:
        Construye una estructura jerárquica
        similar a un arbol.
        """
        self.transformaciones.append(personaje)

    def poder_total(self):
        """
        Calcula el poder total considerando transformaciones usando funcion recursiva

        MECANISMO:
        - Caso base: nivel de poder propio.
        - Caso recursivo: suma de poderes de las transformaciones.

        ESTRUCTURA:
        Árbol implícito.
        """
        total = self._nivel_poder
        for t in self.transformaciones:
            total += t.poder_total()
        return total
