"""lista 4 zad3  Wojciech Wroblewski """

import random


class Node(object):

    def __init__(self, value):
        self.value = value
        self.children = list([])

    def insert_child(self, child):
        self.children.append(child)


"""funkcja przechodzenia po drzewie bfs i dfs w zaleznsci od typu"""


def traverse(root, type):
    if type == "bfs":
        switch = 0
    else:
        switch = -1
    queue = [root]
    while len(queue) > 0:
        current_node = queue.pop(switch)
        yield current_node.value
        for child in current_node.children:
            queue.append(child)


"""funkcja zwraca node i potem jego potomkow
funkcja pomocnia sprawdzajaca poprawnosc generowania drzewa"""


def tree_children(root):
    if len(root.children) != 0:
        print(root.value)
        print("children: ")
        for child in root.children:
            print(child.value)
        print("\n")
    for child in root.children:
        tree_children(child)


"""funkcja generujaca drzewo
przyjmuje wartosci <node bazowy>,<wysokosc oczekiwana>,<max liczba potomkow dla jednego node'a>,<wartosci dla node>"""


def tree(root, k, x, values):
    if k > 0:
        for i in range(0, random.randint(1, x)):
            root.insert_child(Node(values.pop(0)))
        for child in root.children:
            tree(child, k - 1, x, values)


"""wysokosc drzewa"""

k = 2
"""max liczba potomkow dla jednego node'a"""

x = 3
"""deklarujemy values zeby nie zabraklo wartosci w pesymistycznym przypadku"""

values = [n + 1 for n in range(0, x ** (k + 1))]
root = Node(values.pop(0))
tree(root, k, x, values)

type = "dfs"
print("DFS\n")
print(list(traverse(root, type)))

print("\nBFS \n")
type = "bfs"
print(list(traverse(root, type)))

""" wywolanie pomocne w celu sprawdzenia poprawnosci generowanego drzewa"""
#print(tree_children(root))
