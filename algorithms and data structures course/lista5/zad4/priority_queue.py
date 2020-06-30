import math


class Queue(object):
    """
    Klasa realizujaca kolejke prioretytowa
    Kolejka jest oparta na binary heap
    """
    def __init__(self):
        self.elements = list()
        self.size = 0

    def is_empty(self):
        return bool(self.size)

    def insert(self, el, priority):
        """
        W tablcy elements elementy sa przychowywane jako krotki (node_idx, priority)
        :param el:
        :param priority:
        :return:
        """
        new = tuple([el, priority])
        i = self.size
        self.size += 1
        self.elements.append(new)
        while i > 0:
            parent_idx = math.floor((i-1)/2)
            if not self.elements[parent_idx][1] > priority:
                break
            self.elements[i] = self.elements[parent_idx]
            i = parent_idx
        self.elements[i] = new

    def decrease_key(self, element, new_prior):
        """
        Elementem jest krotka (value, priority)
        :param new_prior: nowy priorytet
        :param element: (value, priority)
        :return:
        """
        i = self.elements.index(element)
        self.elements[i] = tuple([element[0], new_prior])
        temp = self.elements[i]
        while i > 0:
            parent_idx = math.floor((i - 1) / 2)
            if not self.elements[parent_idx][1] > temp[1]:
                break
            self.elements[i] = self.elements[parent_idx]
            i = parent_idx
        self.elements[i] = temp

    def extract_min(self):
        if self.size == 0:
            return None
        else:
            min_el = self.elements[0]
            self.elements[0] = self.elements[self.size-1]
            self.size -= 1
            del(self.elements[self.size])
            self.heapify(0)
            return min_el

    def heapify(self, x_loc):
        """
        Funkcja przywraca wlasnosc kopca
        :param x_loc:
        :return:
        """
        min_idx = x_loc
        # Obliczenie pozycji lewego i prawego syna
        left = 2*x_loc + 1
        right = 2*x_loc + 2

        if left < self.size and self.elements[left][1] < self.elements[min_idx][1]:
            min_idx = left
        if right < self.size and self.elements[right][1] < self.elements[min_idx][1]:
            min_idx = right

        # Zamiana wierzcholkow
        if min_idx != x_loc:
            self.swap_nodes(min_idx, x_loc)
            self.heapify(min_idx)

    def swap_nodes(self, u, v):
        self.elements[u], self.elements[v] = self.elements[v], self.elements[u]

    def priority(self, value, new_prior):
        for e in self.elements:
            if e[0] == value and e[1] > new_prior:
                self.decrease_key(e, new_prior)

    def enqueue(self, value, priority):
        self.insert(value,priority)

    def empty(self):
        if self.is_empty() == True:
            return "1"
        else:
            return "0"

    def pop(self):

        if len(self.elements) > 0:
            return self.extract_min()
        else:
            return ""

    def top(self):
        if len(self.elements) > 0:
            return self.elements
        else:
            return ""

    def print(self):
        return self.elements

    def check_if_in_heap(self, object):
        for e in self.elements:
            if e[0] == object:
                return True
        else:
            return False



"""
q = Queue()

q.insert(4, 2)
q.insert(4, 0)
q.insert(4, 7)
q.insert(4, 5)
q.insert(1, 1)
q.insert(1, 5)

print(q.elements)
print(q.extract_min())
print(q.elements)
q.priority(4,1)
print(q.elements)
"""

