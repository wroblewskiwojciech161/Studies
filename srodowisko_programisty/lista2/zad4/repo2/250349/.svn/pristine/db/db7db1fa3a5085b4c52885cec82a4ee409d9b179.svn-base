import math

"""implementacje minimalnego kopca binarnego oraz funkcji
   kolejki priorytetowej na podstwie kopca"""

class Queue(object):

    def __init__(self):
        self.elements = list()
        self.size = 0

    def is_empty(self):
        return bool(self.size)

    """inplementacja funkcji dodajacej wartosc z priorytetem do kopca"""

    def insert(self, el, priority):

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

    """funkcja implementujaca zmiane klucza dla elementu o zadanej wartosci """

    def decrease_key(self, element, new_prior):

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

    """ ekstraktowanie elementu o najmniejszym (przy min heap najbardziej istotnym)
        priorytecie z kopca i zwracanie go"""

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

    """ funkcja realizuje przywracanie wlasnosci kopca"""

    def heapify(self, x_loc):

        min_idx = x_loc

        left = 2*x_loc + 1
        right = 2*x_loc + 2

        if left < self.size and self.elements[left][1] < self.elements[min_idx][1]:
            min_idx = left
        if right < self.size and self.elements[right][1] < self.elements[min_idx][1]:
            min_idx = right


        if min_idx != x_loc:
            self.swap_nodes(min_idx, x_loc)
            self.heapify(min_idx)


    def swap_nodes(self, u, v):
        self.elements[u], self.elements[v] = self.elements[v], self.elements[u]

    """funkcja kolejki priorytetowej zamieniajaca priorytet elementow o
        wskazanej wartosci """

    def priority(self, value, new_prior):
        for e in self.elements:
            if e[0] == value and e[1] > new_prior:
                self.decrease_key(e, new_prior)

    """dodawanie elementu do kolejki """

    def enqueue(self, value, priority):
        self.insert(value,priority)

    """sprawdzanie czy kolejka jest pusta"""

    def empty(self):
        if len(self.elements) > 0:
            return "0"
        else:
            return "1"

    """usuwanie elementu o najbardziej istotnym kluczu o zwracenie go"""

    def pop(self):

        if len(self.elements) > 0:
            return self.extract_min()[0]
        else:
            return ""

    """ zwracaie wartosci elementu o najbardziej istotnym kluczu"""

    def top(self):
        if len(self.elements) > 0:
            return self.elements[0][0]
        else:
            return ""

    """obrazowanie elementow w kolejce"""

    def print(self):
        return self.elements

    """sprawdzanie czy wartosc wystepuje w kolejce"""

    def check_if_in_heap(self, object):
        for e in self.elements:
            if e[0] == object:
                return True
        else:
            return False

