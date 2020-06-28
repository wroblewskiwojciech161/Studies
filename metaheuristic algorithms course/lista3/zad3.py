from __future__ import print_function
import random
from sys import stdin
import time
import sys

"""zad3 lista 3 amh Wojciech Wroblewski"""

in_data = input().split()
t = int(in_data[0])
n = int(in_data[1])
m = int(in_data[2])
s = int(in_data[3])
p = int(in_data[4])

lines = stdin.readlines()
map = []
routes = []
for i in range(0, n):
    temp = [char for char in lines[i]]
    temp = temp[0:-2]
    temp = [int(x) for x in temp]
    map.append(temp)
for i in range(n, n + s):
    temp = [char for char in lines[i]]
    temp = temp[0:-2]
    routes.append(temp)

"""funkcja sortujaca ze wzgledu na 2 argument """


def Sort(sub_li):
    sub_li.sort(key=lambda x: x[1])
    return sub_li


"""funkcja pomocnicza w mutacji- zamiana znakow w stringu"""


def change_char(s, p, r):
    return s[:p] + r + s[p + 1:]


"""klasa symulujaca algorytm genetyczny"""


class Genetic:
    def __init__(self, max_population_size, initial_routes, n, m, map, time):
        self.map = map
        self.max_population_size = max_population_size
        self.initial_routes = initial_routes
        self.n = n
        self.m = m
        self.time = time
        self.start = self.find_start()
        self.best = None
        self.best_route = None
        self.directions = ['U', 'R', 'D', 'L']
        self.vector = []

    deal = []

    """funkcja zwraca wartosci trasy, jesli wychodzi poza skale zwraca pusta liste"""

    def get_route(self, path):
        start = self.find_start()
        coordinates = self.convert_chars_to_cordinates(path, start)
        route = []

        for c in coordinates:
            if 0 <= c[0] < self.n and 0 <= c[1] < self.m:
                route.append(self.map[c[0]][c[1]])
            else:
                return []
        return route

    """tworzenie populacji porzatkowej"""

    def create_population(self):
        population = self.initial_routes.copy()
        return population

    """funkcja zamienia droge zadaną we współrzędnych w drogę znaków z tresci zadania"""

    def convert_coordinates_to_char(self, path):
        way = []
        for i in range(0, len(path) - 1):
            if (path[i][0] - path[i + 1][0] > 0):
                way.append('U')
            elif (path[i][0] - path[i + 1][0] < 0):
                way.append('D')
            elif (path[i][1] - path[i + 1][1] > 0):
                way.append('L')
            elif (path[i][1] - path[i + 1][1] < 0):
                way.append('R')
        return way

    """funkcja zamienia drogę znaków na droge współrzędnych"""

    def convert_chars_to_cordinates(self, way, initial):
        out = []
        out.append([initial[0], initial[1]])
        temp = initial
        for c in way:
            if c == 'U':
                temp[0] -= 1
                out.append([temp[0], temp[1]])
            elif c == 'D':
                temp[0] += 1
                out.append([temp[0], temp[1]])
            elif c == 'L':
                temp[1] -= 1
                out.append([temp[0], temp[1]])
            elif c == 'R':
                temp[1] += 1
                out.append([temp[0], temp[1]])
        return out

    """szukanie poczatkowych wspolrzadnych agenta"""

    def find_start(self):
        for i in range(0, self.n):
            for j in range(0, self.m):
                if map[i][j] == 5:
                    return [i, j]
        return None

    """funkcja realizujaca selekcje"""

    def selection(self, population):

        out = []
        selection = []

        for p in population:

            touple = []
            temp = []
            temp = self.get_route(p).copy()

            if len(temp) > 0 and temp.count(1) == 0 and temp.count(8) > 0 and temp[0] == 5:  # jest ok
                idx = temp.index(8)

                touple.append(p[:idx])
                touple.append(len(touple[0]))
                selection.append(touple)

                if len(p[:idx]) <= self.best:
                    out.append(p[:idx])
                    self.best = len(p[:idx])
                    self.best_route = p[:idx].copy()
            else:
                touple.append(p)
                touple.append(len(touple[0]))
                selection.append(touple)

        Sort(selection)

        if len(out) > self.max_population_size // 2:
            out = out[:self.max_population_size // 2]


        else:
            i = 0
            while len(out) < self.max_population_size // 2:
                if selection[i][0] not in out:
                    out.append(selection[i][0])
                i += 1

        return out

    """cross over"""

    def cross_over(self, population):

        to_reproduce = self.max_population_size - len(population)

        i = 0
        children = []
        while i < to_reproduce:

            r_1 = random.randint(0, len(population) - 1)

            if r_1 >= len(population) - 1:
                r_2 = r_1 - 1
            else:
                r_2 = r_1 + 1

            parent_1 = population[r_1]
            parent_2 = population[r_2]

            slice1 = random.randint(0, len(parent_1) - 1)
            slice2 = random.randint(0, len(parent_2) - 1)

            value = parent_1[0:slice1] + parent_2[slice2:]

            children.append(value)
            i += 1

        temp = self.mutation(children).copy()

        for t in temp:
            population.append(t)

        return population

    """mutacja"""

    def mutation(self, population):

        out = []

        for p in population:
            r = random.uniform(0, 1)
            if r < 0.1:

                temp = p
                if len(temp) > 1:
                    if 0 < r < 0.03:

                        temp.insert(random.randint(0, len(temp) - 1), random.choice(self.directions))

                    elif 0.03 < r < 0.07:
                        del temp[random.randint(0, len(temp) - 1)]
                        temp.insert(random.randint(0, len(temp) - 1), random.choice(self.directions))
                    elif 0.07 < r < 0.01:
                        del temp[random.randint(0, len(temp) - 1)]

                    out.append(temp)
            else:
                out.append(p)

        return out

    """glowna funkcja reprezentujaca algorytm genetyczny"""

    def process(self):
        population = self.create_population().copy()

        for p in self.initial_routes:
            temp = self.get_route(p).copy()
            if len(temp) > 0 and temp.count(1) == 0 and temp.count(8) > 0 and temp[0] == 5:  # jest ok
                idx = temp.index(8)
                self.best_route = p[:idx].copy()
                self.best = len(self.best_route)
                break

        t_end = time.time() + self.time

        while time.time() < t_end:
            population = self.selection(population).copy()
            # cross and mutation
            population = self.cross_over(population).copy()

        print(self.best)
        print(self.best_route, file=sys.stderr)


g = Genetic(p, routes, n, m, map, t)

g.process()