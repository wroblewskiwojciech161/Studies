from priority_queue import *
from collections import defaultdict
import sys

"""implementacja algorutmy Kruskala oraz Prima"""


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def check_if_in_heap(self, q, v):
        for e in q.elements:
            if e[0] == v:
                return True
        else:
            return False

    def apply_union(self, parent, rank, x, y):
        x_r = self.find(parent, x)
        y_r = self.find(parent, y)
        if rank[x_r] < rank[y_r]:
            parent[x_r] = y_r
        elif rank[x_r] > rank[y_r]:
            parent[y_r] = x_r
        else:
            parent[y_r] = x_r
            rank[x_r] += 1

    def add_un_edge(self, src, dest, weight):

        self.is_directed = False
        node = [dest, weight]
        self.graph[src].insert(0, node)
        node = [src, weight]
        self.graph[dest].insert(0, node)



    """implementacja algorytmu Prima"""

    def prim(self):

        V = self.V
        src = 1
        dist = []
        pred = list()
        for i in range(self.V):
            pred.append(-1)
        queue = Queue()
        for v in range(0, self.V):
            if v == src:
                dist.append(0.0)
                queue.insert(v, 0.0)
            else:
                dist.append(sys.maxsize)
                queue.insert(v, dist[v])
        tree_sum = 0
        spanning_tree = list()
        spanning_tree.append(src)

        print("---------------------------------------")
        print("Prim's algorytm")
        print("---------------------------------------")
        print("krawedzie drzewa rozpinajacego z wagami")

        while queue.size > 0:

            """pop element o najistotniejszym priorytecie """

            node = queue.extract_min()
            u = node[0]

            for walk in self.graph[u]:

                v = walk[0]
                temp = dist[v]
                if self.check_if_in_heap(queue, v) and dist[u] != sys.maxsize and \
                        walk[1] + dist[u] < dist[v]:
                    dist[v] = walk[1] + dist[u]

                    pred[v] = u
                    if v not in spanning_tree:
                        spanning_tree.append(v)
                        tree_sum += dist[v] - dist[u]
                        print('krawedz(', u, ',', v, ')  :', dist[v] - dist[u])

                    queue.decrease_key(tuple([v, temp]), dist[v])

        print("------------------------------------")
        print("ostateczna waga drzewa rozpinajacego ", tree_sum, "\n")

    """implementacja algorytmu Kruskala"""

    def kruskal(self):
        graph = [[n, v[0], v[1]] for n in self.graph for v in self.graph[n]]

        result = []
        i, e = 0, 0
        graph = sorted(graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        weight_sum = 0

        print("------------------------------------")
        print("Kruskal algorithm")
        print("------------------------------------")
        print("krawedzie drzewa rozpinajacego z wagami")

        for u, v, weight in result:
            weight_sum += float(weight)
            print('krawedz(', u, ',', v, ')  :', float(weight))

        print("------------------------------------")
        print("ostateczna waga drzewa rozpinajacego", weight_sum, "\n")
