from personaje import Personaje
from arbol_poder import ArbolPoder
from habilidad import Habilidad
from misiones import Mision, ColaMisiones
from grafo import Grafo
from dijkstra import dijkstra
from topologico import orden_topologico


personajes = []
arbol = ArbolPoder()
cola_misiones = ColaMisiones()
universo = Grafo()
habilidades = {}
rutas = {}


def seleccionar_personaje():
    """
    Permite elegir personaje existente
    """
    if not personajes:
        print("No hay personajes")
        return None

    for i, p in enumerate(personajes):
        print(i, p.nombre, "Poder", p.get_poder())

    idx = int(input("Seleccione indice "))
    return personajes[idx]


def crear_personaje():
    """
    Crea personaje nuevo
    """

    nombre = input("Nombre ")
    especie = input("Especie ")
    planeta = input("Planeta ")
    poder = int(input("Nivel de poder "))

    p = Personaje(nombre, especie, planeta, poder)

    personajes.append(p)
    arbol.insertar(p)

    print("Personaje creado")


def agregar_habilidad_personaje():
    """
    Agrega habilidad a personaje
    """
    p = seleccionar_personaje()
    if p is None:
        return

    h = input("Nombre habilidad ")
    p.agregar_habilidad(h)
    print("Habilidad agregada")


def eliminar_habilidad_personaje():
    """
    Elimina habilidad de personaje
    """
    p = seleccionar_personaje()
    if p is None:
        return

    h = input("Nombre habilidad ")
    p.eliminar_habilidad(h)
    print("Habilidad eliminada")


def agregar_objeto_personaje():
    """
    Agrega objeto al inventario
    """
    p = seleccionar_personaje()
    if p is None:
        return

    obj = input("Objeto ")
    p.agregar_objeto(obj)
    print("Objeto agregado")


def eliminar_objeto_personaje():
    """
    Elimina objeto del inventario
    """
    p = seleccionar_personaje()
    if p is None:
        return

    obj = input("Objeto ")
    p.eliminar_objeto(obj)
    print("Objeto eliminado")


def agregar_transformacion():
    """
    Agrega transformacion recursiva
    """
    base = seleccionar_personaje()
    if base is None:
        return

    print("Transformacion")
    nombre = input("Nombre ")
    especie = input("Especie ")
    planeta = input("Planeta ")
    poder = int(input("Nivel de poder "))

    t = Personaje(nombre, especie, planeta, poder)
    base.agregar_transformacion(t)

    print("Transformacion agregada")


def mostrar_poder_total():
    """
    Muestra poder total
    """
    p = seleccionar_personaje()
    if p:
        print("Poder total", p.poder_total())


def mostrar_inorden():
    """
    Recorrido inorden
    """
    if arbol.raiz:
        arbol.inorden(arbol.raiz)
    else:
        print("Arbol vacio")


def mostrar_preorden():
    """
    Recorrido preorden
    """
    if arbol.raiz:
        arbol.preorden(arbol.raiz)
    else:
        print("Arbol vacio")


def mostrar_postorden():
    """
    Recorrido postorden
    """
    if arbol.raiz:
        arbol.postorden(arbol.raiz)
    else:
        print("Arbol vacio")


def buscar_por_poder():
    """
    Busca personaje por poder
    """
    poder = int(input("Poder a buscar "))
    r = arbol.buscar(poder, arbol.raiz)

    if r:
        print("Encontrado", r.nombre)
    else:
        print("No existe")


def crear_habilidad():
    """
    Crea nodo raiz habilidad
    """
    nombre = input("Habilidad base ")
    habilidades[nombre] = Habilidad(nombre)
    print("Habilidad creada")


def agregar_mejora():
    """
    Agrega nodo como rama
    """
    base = input("Habilidad base ")
    nueva = input("Mejora ")

    if base in habilidades:
        m = Habilidad(nueva)
        habilidades[nueva] = m
        habilidades[base].agregar_mejora(m)
        print("Mejora agregada")
    else:
        print("No existe habilidad")


def mostrar_habilidades():
    """
    Muestra arbol general
    """
    if habilidades:
        list(habilidades.values())[0].mostrar()
    else:
        print("No hay habilidades")


def buscar_habilidad():
    """
    Busca en arbol general
    """
    nombre = input("Buscar habilidad ")
    for h in habilidades.values():
        r = h.buscar(nombre)
        if r:
            print("Habilidad encontrada", r.nombre)
            return
    print("No encontrada")


def agregar_mision():
    """
    Inserta en cola de prioridad
    """
    nombre = input("Mision ")
    prioridad = int(input("Prioridad "))

    cola_misiones.agregar(Mision(nombre, prioridad))
    print("Mision agregada")


def atender_mision():
    """
    Extrae mision
    """
    if cola_misiones.cola:
        m = cola_misiones.atender()
        print("Atendiendo", m.nombre)
    else:
        print("No hay misiones")


def agregar_nodo():
    """
    Inserta planeta
    """
    n = input("Nodo ")
    universo.agregar_nodo(n)

    if n not in rutas:
        rutas[n] = []

    print("Nodo agregado")


def agregar_ruta():
    """
    Crea arista con peso
    """
    o = input("Origen ")
    d = input("Destino ")
    c = int(input("Costo "))

    universo.agregar_arista(o, d)
    rutas[o].append((d, c))

    print("Ruta creada")


def ejecutar_bfs():
    """
    Recorrido amplitud
    """
    i = input("Inicio ")
    print(universo.bfs(i))


def ejecutar_dfs():
    """
    Recorrido profundidad
    """
    i = input("Inicio ")
    print(universo.dfs(i))


def buscar_camino():
    """
    Dijkstra
    """
    i = input("Inicio ")
    print(dijkstra(rutas, i))


def plan_entrenamiento():
    """
    Ordenamiento topologico
    """
    g = {}
    for h in habilidades.values():
        g[h.nombre] = [m.nombre for m in h.mejoras]

    print(orden_topologico(g))


def menu():
    """
    Menu principal
    """

    while True:
        print("\n--- UNIVERSO ---")
        print("1 Crear personaje")
        print("2 Agregar habilidad a personaje")
        print("3 Eliminar habilidad")
        print("4 Agregar objeto")
        print("5 Eliminar objeto")
        print("6 Agregar transformacion")
        print("7 Ver poder total")
        print("8 Inorden arbol poder")
        print("9 Preorden arbol poder")
        print("10 Postorden arbol poder")
        print("11 Buscar por poder")
        print("12 Crear habilidad")
        print("13 Agregar mejora")
        print("14 Mostrar habilidades")
        print("15 Buscar habilidad")
        print("16 Agregar mision")
        print("17 Atender mision")
        print("18 Agregar nodo")
        print("19 Agregar ruta")
        print("20 BFS")
        print("21 DFS")
        print("22 Dijkstra")
        print("23 Plan habilidades")
        print("0 Salir")

        op = input("Opcion ")

        if op == "1":
            crear_personaje()
        elif op == "2":
            agregar_habilidad_personaje()
        elif op == "3":
            eliminar_habilidad_personaje()
        elif op == "4":
            agregar_objeto_personaje()
        elif op == "5":
            eliminar_objeto_personaje()
        elif op == "6":
            agregar_transformacion()
        elif op == "7":
            mostrar_poder_total()
        elif op == "8":
            mostrar_inorden()
        elif op == "9":
            mostrar_preorden()
        elif op == "10":
            mostrar_postorden()
        elif op == "11":
            buscar_por_poder()
        elif op == "12":
            crear_habilidad()
        elif op == "13":
            agregar_mejora()
        elif op == "14":
            mostrar_habilidades()
        elif op == "15":
            buscar_habilidad()
        elif op == "16":
            agregar_mision()
        elif op == "17":
            atender_mision()
        elif op == "18":
            agregar_nodo()
        elif op == "19":
            agregar_ruta()
        elif op == "20":
            ejecutar_bfs()
        elif op == "21":
            ejecutar_dfs()
        elif op == "22":
            buscar_camino()
        elif op == "23":
            plan_entrenamiento()
        elif op == "0":
            print("Fin del programa")
            break
        else:
            print("Opcion invalida")


menu()
