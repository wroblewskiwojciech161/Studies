
from minimal_heap import *

"""Wojciech Wroblewski lista 5 zad 1 lab """


"""implementacja kolejki priorytetowej bazujacej na 
minimalnym kopcu binarnym """


def main():
    legal_operations = ['empty', 'insert', 'top', 'pop', 'priority', 'print']

    print("Podaj liczbe operacji.")
    number = input()

    operations = []
    for i in range(int(number)):
        operations.append(input())


    format_operations = []
    for o in operations:
        list = []
        list = o.split(' ')
        format_operations.append(list)


    for o in format_operations:
        if o[0] not in legal_operations:
            print("blednie zadeklarowana funkcja")
            exit()

    queue = Queue()
    print("===================\n")
    for operation in format_operations:

        if operation[0] == 'empty':

            print(queue.empty())
        elif operation[0] == 'top':
            print(queue.top())
        elif operation[0] == 'insert':
            queue.enqueue(int(operation[1]), int(operation[2]))
        elif operation[0] == 'print':
            print(queue.print())
        elif operation[0] == 'pop':
            print(queue.pop())
        elif operation[0] == 'priority':
            queue.priority(int(operation[1]), int(operation[2]))


main()
