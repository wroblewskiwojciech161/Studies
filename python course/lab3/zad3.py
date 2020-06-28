#zad3
def get_sum(path):
    file = open(path, "r")
    tab = [int(line.split(" ")[-1]) for line in file.readlines()]
    print(sum(tab))


get_sum("/home/sparrovsky/Desktop/python_labs/lab3/plik.txt")

