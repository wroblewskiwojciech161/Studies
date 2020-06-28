from cmath import exp
from math import pi
import timeit
from numpy.fft import fft as numpy_fft
from numpy.fft import ifft as numpy_ifft
import numpy as np
import timeit
from functools import wraps
from time import time
from functools import reduce
import random

"""Wojciech Wroblewski  lista4 zad5"""

"dekorator z zad1 do liczenia statystyk czasowych"
def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print('Elapsed time: {}'.format(end - start))
        return result

    return wrapper

class FastBigNum(object):
    def __init__(self, num):
        self.value = int(num)

    def __str__(self):
        return str(self.value)

    """tutaj definiujemy jaki rodzaj mnozenia wykonac 
    do dyspozycji  funkcje z zadania tj :
    -calculate_fft_numpy()
    -calculate_mult_dfft()
    -calculate_fft_numpy()
    -calculate_standard()
    """

    def __mul__(self, *other):
        temp = int(self.value)
        for o in other:
            temp = calculate_fft_numpy(temp, o.value)
        return FastBigNum(temp)


def is_power_of_two(n):
    """zwraca True jesli liczba jest potega 2"""
    if n <= 0:
        return False
    else:
        return n & (n - 1) == 0


def timer(function):
    def new_function():
        start_time = timeit.default_timer()
        function()
        elapsed = timeit.default_timer() - start_time
        print('Funkcja "{name}" zajela {time} sekund.'.format(name=function.__name__, time=elapsed))

    return new_function


def omega(k, n):
    return exp(-2j * k * pi / n)


def dft(x, n):
    return [sum(x[i] * omega(i * k, n) if i < len(x) else 0 for i in range(n)) for k in range(n)]


def idft(x, n):
    return [int(round(sum(x[i] * omega(-i * k, n) if i < len(x) else 0 for i in range(n)).real) / n) for k in range(n)]

    """zwraca inta na podstawie danej podstawy z tablicy """
def to_decimal(number, base):
    result = 0
    for index, character in enumerate(number):
        result += int(character) * base ** index
    return result


def check_which_2pow(number):
    """zwraca ktora potega 2 jest najblizej"""
    counter = len(str(number))
    k = 0
    while k != 2:
        if is_power_of_two(counter) == True:
            k += 1
        else:
            counter += 1
    return counter

    """zamiania int w tablice o odp dlugosci"""
def to_decimal_table(number, power):
    "zamiana liczby na tablice o zadanej dlugosci"
    output = []
    number = str(number)
    for i in range(0, len(number)):
        output.append(int(number[len(number) - i - 1]))
    while len(output) != power:
        output.append(0)
    return output


"""funkcja oblicza mnozenie 2 liczb metoda dyskretnej transfomrty fouriera"""


def calculate_mult_dfft(a, b):
    x = []
    y = []
    size = max(len(str(a)), len(str(b)))
    x = to_decimal_table(a, 2 * size)
    y = to_decimal_table(b, 2 * size)
    dft_x = dft(x, len(x))
    dft_y = dft(y, len(y))
    freq = []
    vector_0 = complex(0, 0)
    for i in range(0, max(len(dft_y), len(dft_x))):
        if i < min(len(dft_y), len(dft_x)):
            temp = complex(dft_x[i] * dft_y[i])
            freq.append(temp)
        else:
            freq.append(vector_0)

    return to_decimal(idft(freq, len(freq)), 10)


"""funkcja oblicza mnozenie 2 liczb na przy pomocy  fft i ifft z biblioteki numpy"""


def calculate_fft_numpy(a, b):
    x = to_decimal_table(a, 2 * check_which_2pow(max(a, b)))
    y = to_decimal_table(b, 2 * check_which_2pow(max(a, b)))

    dft_x = np.fft.fft(x)
    dft_y = np.fft.fft(y)

    freq = []
    out = []
    for i in range(0, len(dft_x)):
        temp = complex(dft_x[i] * dft_y[i])
        freq.append(temp)

    z = [int(round(elem.real)) for elem in numpy_ifft(freq)]

    return to_decimal(z, 10)


def fft_own(x):
    n = len(x)
    if n <= 1: return x
    even = fft_own(x[0::2])
    odd = fft_own(x[1::2])
    t = [exp(-2j * pi * k / n) * odd[k] for k in range(n // 2)]
    return [even[k] + t[k] for k in range(n // 2)] + \
           [even[k] - t[k] for k in range(n // 2)]


def ifft_own(x):

    for i in range(0, len(x)):
        x[i].conjugate()
    print("to:", len(x))
    x = fft_own(x)
    for i in range(0, len(x)):
        x[i].conjugate()
    for i in range(0, len(x)):
        x[i] = x[i].real
    return x


def calculate_fft_own(a, b):
    x = []
    y = []

    size = check_which_2pow(max(a, b))

    x = to_decimal_table(a, 2 * size)
    y = to_decimal_table(b, 2 * size)

    dft_x = fft_own(x)

    dft_y = fft_own(y)

    freq = []

    for i in range(0, len(dft_x)):
        temp = complex(dft_x[i] * dft_y[i])
        freq.append(temp)

    return to_decimal(idft(freq, len(freq)), 10)


"""funkcja oblicza standardowe mnozenie """
def calculate_standard(a, b):
    return int(a) * int(b)


def calculate_fft_numpy(a, b):
    x = to_decimal_table(a, 2 * check_which_2pow(max(a, b)))
    y = to_decimal_table(b, 2 * check_which_2pow(max(a, b)))

    dft_x = numpy_fft(x)
    dft_y = numpy_fft(y)

    freq = []
    for i in range(0, len(dft_x)):
        temp = complex(dft_x[i] * dft_y[i])
        freq.append(temp)

    z = [int(round(elem.real)) for elem in numpy_ifft(freq)]
    return to_decimal(z, 10)

    return output


A = int(''.join([random.choice("0123456789") for i in range(50)]))
B = int(''.join([random.choice("0123456789") for i in range(50)]))

print("random comparison \n")
print("python standard :",calculate_standard(A,B))
print("\n")
print("own fft :",calculate_fft_own(A,B))
print("\n")
print("numpy fft :",calculate_fft_numpy(A,B))
print("\n")
print("dft :",calculate_standard(A,B))

print("\n")
print("example from list")
A = '1312312231232131231231231231231231212331233231349'
B = '1212312311223123121312312321321231231112323123231'

a = FastBigNum(A)
b = FastBigNum(B)
print("A :",A)
print("B:",B)
print("A*B*A*B:",a*b*a*b)

