from timeit import default_timer as timer
from collections import defaultdict
import sys
from operator import itemgetter
import random
from priority_queue import *


class Graph:

    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, src, dest, weight):
        self.graph[src].insert(0, [dest, weight])
        self.graph[dest].insert(0, [src, weight])

    def random_traversal(self):
        distance = 0
        visited = set()
        vertex = random.choice(list(self.graph.keys()))
        visited.add(next)

        while len(visited) < self.V:
            vertex = random.choice(self.graph[vertex])[0]
            visited.add(vertex)

    def greedy_traversal(self):
        distance = 0
        visited = set()
        vertex = random.choice(list(self.graph.keys()))
        visited.add(next)

        while len(visited) < self.V:
            for vrtx in sorted(self.graph[vertex], key=itemgetter(1)):
                if vrtx[0] not in visited:
                    vertex = vrtx[0]
                    break

            visited.add(vertex)


nodes = int(input())
edges = int(input())
graph = Graph(nodes)

for e in range(edges):
    edge = input().split(" ")
    u, v, weight = int(edge[0]), int(edge[1]), float(edge[2])
    graph.addEdge(u, v, weight)

start_time = timer()
time = 0
graph.random_traversal()
time = timer()
time -= start_time
print("1.Przechodzenie losowe:", time, file=sys.stderr)

start_time = timer()
time = 0
graph.greedy_traversal()
time = timer()
time -= start_time
print("2.Przechodzenie zachlanne:", time, file=sys.stderr)
