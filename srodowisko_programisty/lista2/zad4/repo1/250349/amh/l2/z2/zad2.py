# -*- coding: utf-8 -*-
"""zad 2 lista 2 lab algorytmy metaheurystyczne Wojciech Wróblewski """
from __future__ import print_function
import random
import time
import math
import sys
from sys import stdin
in_data = input().split()
time_set = int(in_data[0])
r=int(in_data[1])
c=int(in_data[2])
k=int(in_data[3])

matrix=[]
lines = stdin.readlines()
iterator=0
for line in lines:
    temp=[]
    line.split(" ")
    for i in range(0,len(line)-1):
        if line[i] != " ":
            temp.append(int(line[i]))
    matrix.append(temp)

"""pomocnicze rysowanie macierzy"""

def print_matrix(m,r,c):
    for i in range(r):
        for j in range(c):
            print(m[i][j],end= " ",file=sys.stderr)
        print("\n",file=sys.stderr)

"""zdefiniowana funkcja odległości"""

def distance(matrix1,matrix2,N,M):
   return (1.0 / (N * M)) * sum(sum((matrix1[i][j] - matrix2[i][j]) ** 2
                                                       for j in range(M)) for i in range(N))
"""funkcja tworzy macierz sektorów z odpowiednimi wartościami dla danego bloku
    np.
    [[0,32,128],
    [32,64,128],
    [160,255,64]]
"""
def create_sectors(r,c,k):
    sep_x = r // k
    sep_y = c // k
    last_x = r - r // k
    last_y = c - c // k
    sectors = []
    solution = []
    for i in range(sep_x):
        sectors.append([])
    for i in range(sep_x):
        for j in range(sep_y):
            sectors[i].append(random.choice([0, 32, 64, 128, 160, 192, 223, 255]))
    return sectors


"""funkcja zwraca bazową  początkową macierz """
def create_base(r,c,k,sectors):
    solution=[]
    for i in range (r):
        solution.append([])
    y=0
    for i in range (r):
        x=0
        if i>0 and i%k ==0 and y+1 <len(sectors):
            y+=1
        for j in range (c):
            if j>0 and j%k ==0 and x+1 < len(sectors[0]):
                x +=1
            solution[i].append(sectors[y][x])

    return solution

def get_random_permutation(n):
    arr=[i for i in range (0,n)]
    random.shuffle(arr)
    return arr

"""funkcja tworząca macierz sektorów dla nowego kandydata na rozwiązanie
   Jako przestrzeń rozwiązań - sąsiedztwo traktujamy zamianę wartości w poszczególnych blokach 
   na liczby pozycyjnie mniejszą lub większą z tabeli v
    """
def neighbourhood_1(sector,r,c,k):

    for i in range(r//k):
        for j in range(c//k):
            if sector[i][j] == 0:
                sector[i][j] = random.choice([32, 255])
            elif sector[i][j] == 160:
                sector[i][j] = random.choice([128, 192])
            elif sector[i][j] == 64:
                sector[i][j] = random.choice([128, 32])
            elif sector[i][j] == 32:
                sector[i][j] = random.choice([64, 0])
            elif sector[i][j] == 128:
                sector[i][j] = random.choice([64, 160])
            elif sector[i][j] == 192:
                sector[i][j] = random.choice([160, 223])
            elif sector[i][j] == 223:
                sector[i][j] = random.choice([192, 255])
            elif sector[i][j] == 255:
                sector[i][j] = random.choice([223, 0])

    v=[0, 32, 64, 128, 160, 192, 223,255]

    return sector



initial_temperature=1000
t=initial_temperature # początkowa temperatura

n=1
# początkowy bazowy sektor zawierający wartości dla macierzy M'
b_s =create_sectors(r,c,k)
counter =0
#ustawiamy best na wartość odległośi dla początkowego kandydata
best=distance(create_base(r,c,k,b_s),matrix,r,c)
greatest_sector=b_s.copy()

t_end = time.time() + time_set
while time.time() < t_end:
    counter +=1
    # model w którym temperaturę zmieniamy co 30 iteracji
    while counter% 30 !=0:

        # na podstawie bazowego sektora b_s i danych początkowych tworzymy macierz kandydata w danej iteracji
        sector = neighbourhood_1(b_s,r,c,k)
        m=create_base(r,c,k,sector)
        E = abs(distance(m,matrix,r,c) - best)

        if counter == 1:
            EA=E
        # gorszy kandydat
        if distance(m,matrix,r,c) > best :
            p = math.exp(-abs(E) /t)
            # jeśli p jest odpowiednie to akceptujemy gorszego kandydata
            if p > random.uniform(0,1):
                #sektor z którego generujemy kolejne rozwiazania ustawiamy na zaakceptowane gorsze rozwiązanie
                b_s =sector.copy()
        # nowy najlepszy
        if distance(m,matrix,r,c) < best :
            best =distance(m,matrix,r,c)
            #najlepszy sektor liczb
            greatest_sector=sector.copy()
            # sektor z którego generujemy kolejne rozwiazania ustawiamy na najlepszy
            b_s=sector.copy()
            EA = (EA * (n - 1) + E) / n
            n+=1
        counter+=1
    t = t * 0.99


print(best)
m=create_base(r,c,k,greatest_sector)
print_matrix(m,r,c)











