"""zadanie 3 lista 2 lab algorytmy metaheurystyczna Wojciech Wróblewski"""
# -*- coding: utf-8 -*-
from __future__ import print_function
import random
import time
import math
import sys
from sys import stdin
in_data = input().split()
t = int(in_data[0])
n=int(in_data[1])
m=int(in_data[2])

input=[]
lines = stdin.readlines()

iterator=0
for line in lines:
	line.split()
	temp=[]
	for i in range(0,len(line)-1):
		temp.append(int(line[i]))
	input.append(temp)

def find_initial(input,n,m):
    for i in range (n):
        for j in range(m):
            if input[i][j] == 5 :
                return [i,j]

# współrzędne początkowe agenta
initial = find_initial(input,n,m)


def print_matrix(m,r,c):
	for i in range(r):
		for j in range(c):
			print(m[i][j],end=" ")
		print("\n")


""" funkcja get_repeats, get_indexes, shorten - to funkcje
pomocnicze przy usuwaniu cykli """
def get_repeats(path):
    repeats=[]
    visited=[]
    for p in path:
        if p not in visited:
            visited.append(p)
        else :
            repeats.append(p)

    return repeats
def get_indexes(path,value):
    duplicates=[]
    index=0
    for p in path:
        if p == value:
            duplicates.append(index)
        index+=1
    return duplicates

def shorten (path,duplicates):
   x=duplicates[0]
   y=duplicates[1]
   del path[x:y]
   return  path


"""funkcja zamienia droge zadaną we współrzędnych w drogę znaków z tresci zadania"""

def convert_coordinates_to_char(path):
    way=[]
    for i in range(0,len(path)-1):
        if(path[i][0]-path[i+1][0]>0):
            way.append('U')
        elif (path[i][0] - path[i + 1][0] < 0):
            way.append('D')
        elif (path[i][1] - path[i+1][1] > 0):
            way.append('L')
        elif (path[i][1] - path[i+1][1] < 0):
            way.append('R')
    return way

"""funkcja zamienia drogę znaków na droge współrzędnych"""

def convert_chars_to_cordinates(way,initial):
    out=[]
    out.append([initial[0],initial[1]])
    temp=initial
    for c in way:
        if c == 'U':
            temp[0]-=1
            out.append([temp[0],temp[1]])
        elif c == 'D':
            temp[0]+=1
            out.append([temp[0],temp[1]])
        elif c=='L':
            temp[1]-=1
            out.append([temp[0],temp[1]])
        elif c=='R':
            temp[1]+=1
            out.append([temp[0],temp[1]])
    return out

"""funkcja pomocnicza zwracająca ostatni krok przed wyściem z labiryntu"""

def get_last_step(input,position):
    x=position[0]
    y=position[1]
    if input[x+1][y]==8:
        return [x+1,y]
    elif input[x-1][y]==8:
        return [x-1,y]
    elif input[x][y+1]==8:
        return [x,y+1]
    elif input[x][y-1]==8:
        return [x,y-1]
    else:
        return None

"""funkcja pomocnicza zwracająca kolejne wybierane kroki podczas szukania przykładowej poprawnej drogi"""

def get_next_step(input,position,visited):
    x=position[0]
    y=position[1]
    possibilities=[]
    if input[x+1][y]!=1 and [x+1,y] not in visited:
        possibilities.append([x+1,y])
    if input[x-1][y]!=1 and [x-1,y] not in visited:
        possibilities.append([x-1,y])
    if input[x][y+1]!=1 and [x,y+1] not in visited:
        possibilities.append([x,y+1])
    if input[x][y-1]!=1 and [x,y-1] not in visited:
        possibilities.append([x,y-1])

    if(len(possibilities)>0):
        a = random.randint(0,len(possibilities)-1)
        return possibilities[a]
    for v in visited:
        if v == position:
            temp=visited.index(v)
    return visited[temp-1]

""" funkcja zwraca poprawną drogę od początkowej pozycji aż do wyjścia"""

def path(input,initial):
    visited=[]
    visited.append([initial[0],initial[1]])
    path=[]
    path.append(initial)
    while get_last_step(input,initial) == None:
        temp= get_next_step(input,initial,visited)
        path.append([temp[0],temp[1]])
        visited.append(temp)
        initial=temp
    temp=get_last_step(input,initial)
    path.append(temp)
    return path

"""funkcja sprawdza czy droga spełnia wymagania na to żeby uznać ją za poprawną """

def check_if_correct(input,path,initial):

    has_8 = False
    for i in range (0,len(path)-1):
        if abs(path[i][0] - path[i+1][0]) >0 and abs(path[i][1] - path[i+1][1]) >0 :
            return False
        if abs(path[i][0] - path[i+1][0]) >1 or abs(path[i][1] - path[i+1][1]) >1 :
            return False

    for p in path:
        if p[0]>=n or p[0] >=m or p[0]<=0 or p[1]<=0 or p[1]>=n or p[1] >=m:
            return False
        if input[p[0]][p[1]] == 8:
            has_8 = True

        if input[p[0]][p[1]] == 1:
            return False
    if has_8 == False :
        return False
    if input[path[0][0]][path[0][1]] != 5:
        return False
    if input[path[-1][0]][path[-1][1]] != 8:
        return False

    return True


"""funkcja skraca drogę poprzez powielone współrzędne,
 jeśli współrzeðne się powielą tzn że możemy usunąć kroki które niepotrzebnie wykonujemy """
def cut_cycles(simple_path):

    while len(get_repeats(simple_path)) > 0:
        simple_path=shorten(simple_path, get_indexes(simple_path, get_repeats(simple_path)[0]))
    return simple_path

"""sąsiedztwo - funkcja wyznaczająca kolejnych kandydatóœ na rozwiązanie
    dlae danej drogi x_0, generujemy inne poprawne trasy. Losujemy indeksy współrzednych w x_0, jesli 
    w x_0  trasa od A do B została wykonana w k krokach, a wśród wygenerowanych dodatkowo dróg zobaczymy, że można od A do B
    przejść krócej to wycinamy krótszą trasę i zamieniamy w x_0"""
def neighbourhood_1 (simple):

    neighbours=[]
    for i in range (0,10):
        neighbours.append(path(input,initial))

    a = random.randint(0, len(simple) - 1)
    b = random.randint(0, len(simple) - 1)
    if a < b:
        min = abs(a - b-1)
        first = simple[a]
        last = simple[b]
        for n in neighbours:
            if first in n and last in n:

                idx_a = n.index(first)
                idx_b = n.index(last)

                a = simple.index(first)
                b = simple.index(last)
                if b <= a:
                    continue
                min = abs(a - b-1)
                diff = abs(idx_a - idx_b-1)

                if (diff < min):
                    sub_path = n[idx_a+1:idx_b + 1].copy()

                    if len(sub_path) > 1:
                        del simple[a + 1:b-1]
                        iter = 0

                        for i in range(a + 1, diff):
                            simple.insert(i, sub_path[iter])
                            iter += 1
    return cut_cycles(simple)

"""funkcja znajdująca  krótką trasę agenta w labiryncie - symulowane wyżarzanie"""
def zad1():

    initial_temperature=1000
    temperature = initial_temperature
    cooling = 0.93
    n = 1 #licznik najlepszych rozwiązań
    simple_path = path(input, initial) # generujemy początkową poprawną trasę
    best = len(simple_path)
    best_path = simple_path

    iteration=1
    temp_path=best_path.copy()
    t_end = time.time() + t
    while time.time() < t_end:

        #model w którym temperaturę ochładzamy co 5 iteracji
        while iteration % 5!= 0:

            #generujamy nowego kandydata na podstawię sądziedztwa z drogi temp_path
            current_path=neighbourhood_1(temp_path)

            #róznica rozwiązań najlepszego i kandydata
            E=abs(len(current_path)-len(best_path))

            if iteration == 1:
                EA = abs(len(current_path)-len(best_path))

            # nowy najlepszy kandydat
            if len(current_path) < len(best_path) and check_if_correct(input,current_path,initial) == True:
                best_path=current_path
                temp_path = current_path.copy()
                best=len(best_path)
                n += 1
                EA = (EA * (n - 1) + E) / n

            #gorsze rozwiązanie
            else:
                p = math.exp(-abs((E- EA)) / temperature)
                #jeśli p bedzie w odpowiednim zakresie to akceptuję gorsze rozwiązanie
                if p > random.uniform(0,1) :
                    temp_path=current_path.copy()
                else :
                    temp_path=path(input,initial)

            iteration+=1
        temperature*=cooling
        iteration+=1

    print(len(convert_coordinates_to_char(best_path)))
    print(convert_coordinates_to_char(best_path),file=sys.stderr)


zad1()


