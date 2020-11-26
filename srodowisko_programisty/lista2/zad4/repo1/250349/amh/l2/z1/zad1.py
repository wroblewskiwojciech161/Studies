# -*- coding: utf-8 -*-

"""zad1 lista2 lab algorytmy metaheurystyczne Wojciech Wróblewski

 dane wejściowe t x_1 x_2 x_3 x_4  przekierwowywać z pliku txt """
import time
import random
import math

in_data = input().split()
t = int(in_data[0])
x_1=int(in_data[1])
x_2=int(in_data[2])
x_3=int(in_data[3])
x_4=int(in_data[4])



def salomon_function(X):
    norm=math.sqrt(pow(X[0],2)+pow(X[1],2)+pow(X[2],2)+pow(X[3],2) )
    return 1-math.cos(2*math.pi*norm)+0.1*norm
def objective_function(X):
    x = X[0]
    y = X[1]
    value = 3 * (1 - x) ** 2 * math.exp(-x ** 2 - (y + 1) *5* 2) - 10 * (x / 5 - x ** 3 - y ** 5) * math.exp(
        -x ** 2 - y ** 2) - 1 / 3 * math.exp(-(x + 1) ** 2 - y ** 2)
    return value

""" śądziedztwo rozwiązań, na podstawie rozwiazania best tworzy kolejny kandydujący wektor"""
def candidate(best,n):
    x=best[0]
    y=best[1]
    z=best[2]
    w=best[3]
    x+=float(random.uniform(-1,1)+0.01*random.randrange(-1,1)/n)
    y +=float( random.uniform(-1,1)+0.01*random.randrange(-1,1) /n)
    z += float(random.uniform(-1,1) + 0.01 * random.randrange(-1,1)/n)
    w += float(random.uniform(-1,1) + 0.01*random.randrange(-1,1) /n)

    return [x,y,z,w]


"""funkcja obliczajaca minimum funkcji metodą symulowanego wyżażania"""
def zad1():
    best = [x_1,x_2,x_3,x_4]
    initial_temperature = 1000
    temperature = initial_temperature
    cooling = 0.9
    top_results=[] # przechowuje najlepsze wyniki minimalizacji
    n = 1  # zlicza zaakceptowane rozwiązania

    t_end = time.time() + t
    while time.time() < t_end:

        #model w którym temperaturę wyżażania zmniejszamy po wykonaniu 100 prób
        for j in range (0,100):

            current_candidate= candidate(best,n)
            current_value=(salomon_function(current_candidate))
            best_value=salomon_function(best)

            E =abs(salomon_function(current_candidate)-salomon_function(best))
            if n == 1 and j==0:
                EA = E

            if current_value > best_value:

                p = math.exp(-abs((E-EA))/temperature)

                if p > random.uniform(0.5,1):
                    # akceptujemy gorsze rozwiązanie jeśli p jest w odpowiednim zakresie
                    interesting_value=True
                else :
                    # nie akceptujemy rozwiązania
                    interesting_value=False
            else:
                #lepsze rozwiązanie
                interesting_value = True
            if interesting_value == True:

                #mechanizm omijający powielenie tych samych elementow w talicy top_results
                if len(top_results)>2:
                    if salomon_function(top_results[len(top_results) - 1])==salomon_function(current_candidate):
                        continue
                #ustawiamy nowe  dobre rozwiązanie na podstawie którego będziemy szukać kolejnych
                best = current_candidate
                top_results.append(best)
                n+=1
                EA = (EA * (n - 1) + E) / n

        temperature*=cooling

    print(best[0]," ",best[1]," ",best[2]," ",best[3]," ",salomon_function(best))

zad1()
