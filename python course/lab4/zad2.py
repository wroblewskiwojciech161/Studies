"""Lista4 zad2 Wojciech Wroblewski"""

import random


def generate_tree(h):
    """ustalam liczbe elementow ze wzgledu na  wysokosc drzewa"""
    end = random.randint(2 ** h, 2 ** (h + 1) - 1)
    nodes = [n + 1 for n in range(0, end)]
    return make_tree(nodes, 0)


"""funkcja tworzaca liste reprezentujaca drzewo o zadanej wysokosci"""


def make_tree(nodes_list, iterator):
    if iterator < len(nodes_list):
        way = random.randint(1, 3)
        if way == 1:
            return [nodes_list[iterator], make_tree(nodes_list, 2 * iterator + 1),
                    make_tree(nodes_list, 2 * iterator + 2)]
        elif way == 2:
            return [nodes_list[iterator], None,
                    make_tree(nodes_list, 2 * iterator + 1)]
        else:
            return [nodes_list[iterator], make_tree(nodes_list, 2 * iterator + 1), None]
    else:
        return None


def breadth_first_search(n):
    visited = []
    visited.append(n[1])
    visited.append(n[2])
    yield n[0]
    for element in visited:
        if element is not None:
            if element[0] is not None:
                yield element[0]
            if element[1] is not None:
                visited.append(element[1])
            if element[2] is not None:
                visited.append(element[2])


def depth_first_search(n):
    yield n[0]
    if n[1] is not None:
        yield from depth_first_search(n[1])
    if n[2] is not None:
        yield from depth_first_search(n[2])


tree_example = generate_tree(3)

print("Tree: ", tree_example)
print("\n")

print("BFS TRAVERSAL \n ")

print(list(breadth_first_search(tree_example)))
print("\n")

print("DFS TRAVERSAL  \n")
print(list(depth_first_search(tree_example)))
