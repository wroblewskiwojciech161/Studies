from rbt import *
from bst import *
import re

"""klasa definiująca węzeł"""


class Node(object):
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


INITIAL_CAPACITY = 50
"""klasa implementująca strukturę tablicy haszującej metodą łańcuchową z wykorzysteniem RBT"""


class HashTable:

    def __init__(self, s):
        self.capacity = s
        self.size = 0
        self.buckets = [None] * self.capacity
        self.max_numer_of_elements = 0
        self.current_number_of_elements = 0
        self.number_of_loaded_elements = 0
        self.find_compares = 0

    """implementacja funkcji hashującej"""

    def hash(self, key):
        hashsum = 0

        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)
            hashsum = hashsum % self.capacity

        return hashsum

    """funkcja realizująca dodanie nowej wartości do tablicy hashującej"""

    def insert(self, value):

        """aktualizacja pól"""
        self.current_number_of_elements += 1
        if self.current_number_of_elements > self.max_numer_of_elements:
            self.max_numer_of_elements = self.current_number_of_elements

        value = str(value)
        index = self.hash(value)

        if self.buckets[index] is None:
            self.buckets[index] = RBT()
            self.buckets[index].insert(value)
            self.size += 1
        else:
            self.buckets[index].insert(value)
            self.size += 1

    """funkcja realizująca dodanie nowej wartości do tablicy hashującej"""

    def find(self, value):
        value = str(value)
        index = self.hash(value)
        # 2. Go to first node in list at bucket
        node = self.buckets[index]
        # 3. Traverse the linked list at this node
        if node == None:
            return False
        else:
            return node.find(value)

    """funkcja realizująca usunięcie  wartości kluczowej z tablicy hashującej"""


    def remove(self, value):

        if self.find(value) == 1:
            self.current_number_of_elements -= 1

        value = str(value)
        index = self.hash(value)
        node = self.buckets[index]
        if node != None:
            return node.delete(value)

    def min(self):
        return

    def max(self):
        return

    def successor(self):
        return

    def inorder(self):
        return

    """funkcja realizująca load czyli wielokrotnie dodanie klucza z pliku"""

    def load(self, name):
        huge_list = []
        huge_list2 = []
        with open(name, "r") as f:
            for line in f:
                huge_list.extend(line.split())
        # delete commas ans dots
        self.number_of_loaded_elements += len(huge_list)
        for e in huge_list:
            self.insert(e)
