from priority_queue import *
from collections import defaultdict
from timeit import default_timer as timer
import sys

"""ustalenie zmiiennej o wysokej wartosci utozsamianej jako inf"""
maxint = sys.maxsize


def printArr(dist, n):
    print("-------------------------------------------------")
    print("wierzcholek\t Odleglosc od wierzcholka startowego")
    print("-------------------------------------------------")
    for i in range(n):
        print("%d\t\t%f" % (i, dist[i]))


"""prosta implementacje stuktury grafu"""
"""przechowywanie liczby wierzchlkow oraz slownik relacji krawedzi"""


class Graph():

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, src, dest, weight):

        newNode = [dest, weight]
        self.graph[src].insert(0, newNode)

    def dijkstra(self, src):
        V = self.V
        dist = []
        predecisor = list()
        for i in range(self.V):
            predecisor.append(-1)

        queue = Queue()

        """dla kazdego wierzcholka poza startowym dodaj wartosc odleglosc jako inf"""

        for v in range(0, self.V):
            if v == src:
                dist.append(0.0)
                queue.insert(v, 0.0)
            else:
                dist.append(maxint)
                queue.insert(v, dist[v])

        dist[src] = 0.0
        queue.decrease_key(tuple([src, 0.0]), dist[src])

        while queue.size > 0:

            node = queue.extract_min()
            u = node[0]

            for e in self.graph[u]:
                v = e[0]

                temp = dist[v]

                if queue.check_if_in_heap(v) and dist[u] != maxint and \
                        e[1] + dist[u] < dist[v]:
                    dist[v] = e[1] + dist[u]

                    predecisor[v] = u
                    queue.decrease_key(tuple([v, temp]), dist[v])

        printArr(dist, V)
        print("-------------------------------------------------")
        print("sciezki wraz z wagami.")
        print("-------------------------------------------------")

        for i in range(self.V):
            if i != src:
                self.printPath(dist, predecisor, i)
                print(file=sys.stderr)

    def printPath(self, dist, parent, j):

        if parent[j] == -1:
            print(j, end=' ', file=sys.stderr)
            return
        self.printPath(dist, parent, parent[j])
        print("%.2f %d" % (dist[j] - dist[parent[j]], j,), end=' ', file=sys.stderr)


def main():

    nodes = int(input())
    edges = int(input())
    graph = Graph(nodes)

    for e in range(edges):
        edge = input().split(" ")
        u, v, weight = int(edge[0]), int(edge[1]), float(edge[2])
        graph.addEdge(u, v, weight)

    start_node = int(input())


    start_time = timer()
    time = 0
    graph.dijkstra(start_node)

    time = timer()
    time -= start_time
    print("-------------------------------------------------")
    print("time")
    print("-------------------------------------------------")
    print(time,' seconds', file=sys.stderr)


main()
