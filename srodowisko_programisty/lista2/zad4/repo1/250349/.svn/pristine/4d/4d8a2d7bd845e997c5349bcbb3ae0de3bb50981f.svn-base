
from bst import *
from rbt import *
from hash_t import *
import timeit
import sys
import time
import re

def count_operations(operations, name):
    total_operations = 0
    for o in operations:
        if o[0] == name:
            total_operations += 1
    return total_operations

def print_output(output):
    print("-----------------------------")
    print("wyniki")
    for o in output:
        print(o, "\n")
    print("-----------------------------")

def main():
    t_start = time.time()



    type = sys.argv[2]



    with open(sys.argv[3], 'r') as f:
        x = f.readlines()
    temp = []
    for e in range(0, len(x)):
        x[e] = x[e][:-1]
        temp.append(x[e])
    x = temp.copy()

    number_of_operations = int(x[0])


    """get list of operation"""

    operations = x[1:].copy()
    output = []
    legal = ['insert', 'delete', 'successor', 'load', 'max', 'min', 'inorder', 'find']

    temp_2 = []
    for x in operations:
        temp_2.append(x.split())
    operations = temp_2.copy()

    """check if input has all proper commands"""



    """prezentacja czasowych osiągów operacji dla  danych z pliku"""

    if type == "bst":
        timer_insert=0
        timer_delete=0
        timer_find =0
        timer_inorder=0
        timer_max =0
        timer_min =0
        timer_load=0


        binary_search_tree = BinarySearchTree()
        for o in operations:
            if o[0] == "insert":
                start=time.time()
                binary_search_tree.insert(o[1])
                end = time.time()
                timer_insert += (end-start)
            elif o[0] == "delete":
                start = time.time()
                binary_search_tree.delete(o[1])
                end = time.time()
                timer_delete += (end - start)
            elif o[0] == "load":
                start = time.time()
                binary_search_tree.load(o[1])
                end = time.time()
                timer_load += (end - start)
            elif o[0] == "max":
                start = time.time()
                output.append(binary_search_tree.max())
                end = time.time()
                timer_max += (end - start)

            elif o[0] == "min":
                start = time.time()
                output.append(binary_search_tree.min())
                end = time.time()
                timer_min += (end - start)
            elif o[0] == "find":
                start = time.time()
                output.append(binary_search_tree.find(o[1]))
                end = time.time()
                timer_find += (end - start)

                # file.write(str(binary_search_tree.find(o[1]))+'\n')
            elif o[0] == "successor":
                output.append(binary_search_tree.successor(o[1]))


            elif o[0] == "inorder":
                start = time.time()
                output.append(binary_search_tree.inorder())
                end = time.time()
                timer_inorder += (end - start)

        print("BST")
        print("insert average time :",timer_insert/(binary_search_tree.number_of_loaded_elements + count_operations(operations,"insert")))
        print("delete average time :",timer_delete/(count_operations(operations,"delete")))
        print("find average time :", timer_find / (count_operations(operations, "find")))
        print("max average time :", timer_max / (count_operations(operations, "max")))
        print("min average time :", timer_min / (count_operations(operations, "min")))
        print("inorder average time :", timer_inorder / (count_operations(operations, "inorder")))
        print("load average time :", timer_load / (count_operations(operations, "load")))



    elif type == "rbt":

        timer_insert = 0
        timer_delete = 0
        timer_find = 0
        timer_inorder = 0
        timer_max = 0
        timer_min = 0
        timer_load = 0

        red_black_tree = RBT()
        for o in operations:
            if o[0] == "insert":
                start = time.time()
                red_black_tree.insert(o[1])
                end = time.time()
                timer_insert += (end - start)
            elif o[0] == "delete":
                start = time.time()
                red_black_tree.delete(o[1])
                end = time.time()
                timer_delete += (end - start)
            elif o[0] == "load":
                start = time.time()
                red_black_tree.load(o[1])
                end = time.time()
                timer_load += (end - start)
            elif o[0] == "max":
                start = time.time()
                output.append(red_black_tree.max(red_black_tree.get_root()))
                end = time.time()
                timer_max += (end - start)
            elif o[0] == "min":
                start = time.time()
                output.append(red_black_tree.min(red_black_tree.get_root()))
                end = time.time()
                timer_min += (end - start)
            elif o[0] == "find":
                start = time.time()
                output.append(red_black_tree.find(o[1]))
                end = time.time()
                timer_find += (end - start)
            elif o[0] == "successor":
                output.append("suc"+red_black_tree.successor(o[1]))

            elif o[0] == "inorder":
                start = time.time()
                output.append(red_black_tree.inorder())
                end = time.time()
                timer_inorder += (end - start)
        print("RBT")
        print("insert average time :",
              timer_insert / (red_black_tree.number_of_loaded_elements + count_operations(operations, "insert")))
        print("delete average time :", timer_delete / (count_operations(operations, "delete")))
        print("find average time :", timer_find / (count_operations(operations, "find")))
        print("max average time :", timer_max / (count_operations(operations, "max")))
        print("min average time :", timer_min / (count_operations(operations, "min")))
        print("inorder average time :", timer_inorder / (count_operations(operations, "inorder")))
        print("load average time :", timer_load / (count_operations(operations, "load")))



    elif type == "hmap":

        timer_insert = 0
        timer_delete = 0
        timer_find = 0
        timer_load = 0


        hash_table = HashTable(100)
        for o in operations:
            if o[0] == "insert":
                start = time.time()
                hash_table.insert(o[1])
                end = time.time()
                timer_insert += (end - start)
            elif o[0] == "delete":
                start = time.time()
                hash_table.remove(o[1])
                end = time.time()
                timer_delete += (end - start)
            elif o[0] == "load":
                start = time.time()
                hash_table.load(o[1])
                end = time.time()
                timer_load += (end - start)
            elif o[0] == "find":
                start = time.time()
                output.append(hash_table.find(o[1]))
                end = time.time()
                timer_find += (end - start)
        print("HashTable ")
        print("insert average time :",
              timer_insert / (hash_table.number_of_loaded_elements + count_operations(operations, "insert")))
        print("delete average time :", timer_delete / (count_operations(operations, "delete")))
        print("find average time :", timer_find / (count_operations(operations, "find")))
        print("load average time :", timer_load / (count_operations(operations, "load")))



main()

"""
a=main("rbt","dict1.txt")
b=main("rbt","dict2.txt")
c=main("rbt","dict3.txt")
output=[]
output.append(str(max(a,b,c)))
output.append(str(min(a,b,c)))
if str(a) not in output:
    output.append(str(a))
if str(b) not in output:
    output.append(str(b))
if str(c) not in output:
    output.append(str(c))

print("rbt")
print(output[0] +","+output[1]+","+output[2])


a=main("bst","dict1.txt")
b=main("bst","dict2.txt")
c=main("bst","dict3.txt")
output=[]
output.append(str(max(a,b,c)))
output.append(str(min(a,b,c)))
if str(a) not in output:
    output.append(str(a))
if str(b) not in output:
    output.append(str(b))
if str(c) not in output:
    output.append(str(c))
print("bst")
print(output[0] +","+output[1]+","+output[2])
"""