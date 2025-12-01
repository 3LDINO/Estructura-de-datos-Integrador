from personaje import Personaje
from arbol_poder import ArbolPoder
from habilidad import ArbolHabilidades
from misiones import Mision, ColaMisiones
from grafo import Grafo
from dijkstra import dijkstra
from topologico import orden_topologico


def menu():
    """
    Control principal del sistema
    """

    arbol_poder = ArbolPoder()
    arbol_habilidades = ArbolHabilidades()
    cola_misiones = ColaMisiones()
    universo = Grafo()
    rutas = {}

    while True:

        print("\n--- UNIVERSO DE PERSONAJES ---")
        print("1 Crear personaje")
        print("2 Mostrar personajes por poder")
        print("3 Crear habilidad base")
        print("4 Agregar mejora")
        print("5 Mostrar habilidades")
        print("6 Agregar mision")
        print("7 Atender mision")
        print("8 Agregar planeta")
        print("9 Agregar ruta")
        print("10 BFS del universo")
        print("11 DFS del universo")
        print("12 Buscar ruta optima")
        print("13 Plan de entrenamiento")
        print("0 Salir")

        opcion = input("Opcion ")

        if opcion == "1":

            nombre = input("Nombre ")
            especie = input("Especie ")
            planeta = input("Planeta ")
            poder = int(input("Nivel de poder "))

            personaje = Personaje(nombre, especie, planeta, poder)
            arbol_poder.agregar_personaje(personaje)

        elif opcion == "2":

            arbol_poder.mostrar()

        elif opcion == "3":

            nombre = input("Nombre habilidad ")
            arbol_habilidades.agregar_base(nombre)

        elif opcion == "4":

            base = input("Habilidad base ")
            mejora = input("Nueva mejora ")
            arbol_habilidades.agregar_mejora(base, mejora)

        elif opcion == "5":

            arbol_habilidades.mostrar()

        elif opcion == "6":

            nombre = input("Nombre mision ")
            prioridad = int(input("Prioridad "))
            cola_misiones.agregar(Mision(nombre, prioridad))

        elif opcion == "7":

            mision = cola_misiones.atender()
            print(mision.nombre if mision else "No hay misiones")

        elif opcion == "8":

            planeta = input("Nombre planeta ")
            universo.agregar_nodo(planeta)
            rutas[planeta] = []

        elif opcion == "9":

            origen = input("Origen ")
            destino = input("Destino ")
            costo = int(input("Costo "))
            universo.agregar_arista(origen, destino)
            rutas[origen].append((destino, costo))

        elif opcion == "10":

            inicio = input("Planeta inicial ")
            print(universo.bfs(inicio))

        elif opcion == "11":

            inicio = input("Planeta inicial ")
            print(universo.dfs(inicio))

        elif opcion == "12":

            origen = input("Planeta origen ")
            print(dijkstra(rutas, origen))

        elif opcion == "13":

            print(orden_topologico(arbol_habilidades.obtener_grafo()))

        elif opcion == "0":

            print("Programa finalizado")
            break

        else:

            print("Opcion invalida")


if __name__ == "__main__":
    menu()
