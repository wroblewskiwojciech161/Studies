from bst import *
from rbt import *
from hash_t import *
import timeit
import sys
import time
import re


def print_output(output):
    print("-----------------------------")
    print("wyniki")
    for o in output:
        print(o, "\n")
    print("-----------------------------")


def count_operations(operations, name):
    total_operations = 0
    for o in operations:
        if o[0] == name:
            total_operations += 1
    return total_operations


def main():
    # zacznij liczyć czas
    t_start = time.time()

    # pobierz z listy argumentów ten który określa typ struktury
    type = sys.argv[2]

    with open(sys.argv[3], 'r') as f:
        x = f.readlines()
    temp = []
    for e in range(0, len(x)):
        x[e] = x[e][:-1]
        temp.append(x[e])
    x = temp.copy()

    number_of_operations = int(x[0])

    """wyodrębnij listę operacji do wykonania """

    operations = x[1:].copy()
    output = []
    legal = ['insert', 'delete', 'successor', 'load', 'max', 'min', 'inorder', 'find']

    temp_2 = []
    for x in operations:
        temp_2.append(x.split())
    operations = temp_2.copy()

    """sprawdz czy input zawiera wszystkie poprawne funkcje"""

    for x in operations:
        if x[0] not in legal:
            # print(x[0])
            print("wrong operation declaration.Try again")
            sys.exit()

    """WYkonaj zadane operacje dla danej struktury"""

    if type == "bst":
        binary_search_tree = BinarySearchTree()
        for o in operations:
            if o[0] == "insert":
                binary_search_tree.insert(o[1])
            elif o[0] == "delete":
                binary_search_tree.delete(o[1])
            elif o[0] == "load":
                binary_search_tree.load(o[1])
            elif o[0] == "max":
                output.append(binary_search_tree.max())
            elif o[0] == "min":
                output.append(binary_search_tree.min())
            elif o[0] == "find":
                output.append(binary_search_tree.find(o[1]))
            elif o[0] == "successor":
                output.append(binary_search_tree.successor(o[1]))
            elif o[0] == "inorder":
                output.append(binary_search_tree.inorder())

        print_output(output)
        t_end = time.time()
        print("czas dzialania : ", t_end - t_start, file=sys.stderr)
        print("insert: ", count_operations(operations, "insert") + binary_search_tree.number_of_loaded_elements,
              file=sys.stderr)
        print("delete:", count_operations(operations, "delete"), file=sys.stderr)
        print("find:", count_operations(operations, "find"), file=sys.stderr)
        print("load", count_operations(operations, "load"), file=sys.stderr)
        print("max", count_operations(operations, "max"), file=sys.stderr)
        print("min", count_operations(operations, "min"), file=sys.stderr)
        print("inorder", count_operations(operations, "inorder"), file=sys.stderr)
        print("max liczba elementow:", binary_search_tree.max_numer_of_elements, file=sys.stderr)
        print("koncowa liczba elementow:", binary_search_tree.current_number_of_elements, file=sys.stderr)


    elif type == "rbt":
        red_black_tree = RBT()
        for o in operations:
            if o[0] == "insert":
                red_black_tree.insert(o[1])
            elif o[0] == "delete":
                red_black_tree.delete(o[1])
            elif o[0] == "load":
                red_black_tree.load(o[1])
            elif o[0] == "max":
                output.append(red_black_tree.max(red_black_tree.get_root()))
            elif o[0] == "min":
                output.append(red_black_tree.min(red_black_tree.get_root()))
            elif o[0] == "find":
                output.append(red_black_tree.find(o[1]))
            elif o[0] == "successor":
                output.append(red_black_tree.successor(o[1]))

            elif o[0] == "inorder":
                s=""
                for i in red_black_tree.inorder():
                    s += i+" "
                output.append(s)

        print_output(output)
        t_end = time.time()
        print("czas dzialania : ", t_end - t_start, file=sys.stderr)
        print("insert: ", count_operations(operations, "insert") + red_black_tree.number_of_loaded_elements,
              file=sys.stderr)
        print("delete:", count_operations(operations, "delete"), file=sys.stderr)
        print("find:", count_operations(operations, "find"), file=sys.stderr)
        print("load", count_operations(operations, "load"), file=sys.stderr)
        print("max", count_operations(operations, "max"), file=sys.stderr)
        print("min", count_operations(operations, "min"), file=sys.stderr)
        print("inorder", count_operations(operations, "inorder"), file=sys.stderr)
        print("max liczba elementow:", red_black_tree.max_numer_of_elements, file=sys.stderr)
        print("koncowa liczba elementow:", red_black_tree.current_number_of_elements, file=sys.stderr)

    elif type == "hmap":
        hash_table = HashTable(100)
        for o in operations:
            if o[0] == "insert":
                hash_table.insert(o[1])
            elif o[0] == "delete":
                hash_table.remove(o[1])
            elif o[0] == "load":
                hash_table.load(o[1])
            elif o[0] == "find":
                output.append(hash_table.find(o[1]))

        print_output(output)
        t_end = time.time()
        print("czas dzialania : ", t_end - t_start, file=sys.stderr)
        print("insert: ", count_operations(operations, "insert") + hash_table.number_of_loaded_elements,
              file=sys.stderr)
        print("delete:", count_operations(operations, "delete"), file=sys.stderr)
        print("find:", count_operations(operations, "find"), file=sys.stderr)
        print("load", count_operations(operations, "load"), file=sys.stderr)
        print("max", count_operations(operations, "max"), file=sys.stderr)
        print("min", count_operations(operations, "min"), file=sys.stderr)
        print("inorder", count_operations(operations, "inorder"), file=sys.stderr)
        print("max liczba elementow:", hash_table.max_numer_of_elements, file=sys.stderr)
        print("koncowa liczba elementow:", hash_table.current_number_of_elements, file=sys.stderr)




main()
