from graph import *

"""implementacja algorutmy Prima oraz Kruskala
   dla wyznaczanie min drzewa rozpinajacego grafu"""


def main():
    """pobierane danych """

    nodes = int(input())
    edges = int(input())
    graph = Graph(nodes)

    for e in range(edges):
        edge = input().split(" ")
        u, v, weight = int(edge[0]), int(edge[1]), float(edge[2])
        graph.add_un_edge(u, v, weight)

    """ wywolanie funkcji """

    graph.kruskal()
    graph.prim()


main()
