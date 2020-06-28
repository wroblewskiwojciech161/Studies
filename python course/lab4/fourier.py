from cmath import exp
from math import pi

import timeit
from numpy.fft import fft,ifft
from numpy import array
import numpy as np


import timeit
from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print ('Elapsed time: {}'.format(end-start))
        return result
    return wrapper



def is_power_of_two(n):
    """Return True if n is a power of two."""
    if n <= 0:
        return False
    else:
        return n & (n - 1) == 0
def timer(function):
  def new_function():
    start_time = timeit.default_timer()
    function()
    elapsed = timeit.default_timer() - start_time
    print('Function "{name}" has taken {time} seconds to complete.'.format(name=function.__name__, time=elapsed))
  return new_function

def omega(k,n):
    return exp(-2j*k*pi/n)

def dft(x,n):
    return [sum(x[i]*omega(i*k,n) if i<len(x) else 0 for i in range(n)) for k in range(n)]

def idft(x,n):
    return [int(round(sum(x[i]*omega(-i*k,n) if i<len(x) else 0 for i in range(n)).real)/n) for k in range(n)]

def to_decimal(number, base):
    result = 0
    for index, character in enumerate(number):
        result += int(character) * base ** index
    return result

def check_which_2pow(number):
    counter=len(str(number))
    k=0
    while k!=2:
        if is_power_of_two(counter)==True:
            k+=1
        else:
            counter += 1
    return counter

def to_decimal_table(number,power):
    output=[]
    number=str(number)
    for i in range (0,len(number)):
        output.append(int(number[len(number)-i-1]))
    while len(output)!=power:
        output.append(0)
    return output


def calculate_fft_own(a,b):
    return output
@timing
def calculate_mult_dfft(a,b):
    x=[]
    y=[]
    #size = max(check_which_2pow(a), check_which_2pow(b))
    size=max(len(str(a)),len(str(b)))

   # print(size)
    #size=check_which_2pow(size)
    x = to_decimal_table(a,2*size)
    y = to_decimal_table(b,2*size)

   # print(x)
  #  print(y)
    dft_x=dft(x,len(x))
  #  print(len(dft_x))

    dft_y=dft(y,len(y))
  #  print(len(dft_y))
    freq = []
    vector_0 = complex(0, 0)
    for i in range(0, max(len(dft_y),len(dft_x))):
        if i < min(len(dft_y),len(dft_x)):
             temp = complex(dft_x[i] * dft_y[i])
             freq.append(temp)
        else:
             freq.append(vector_0)



    return to_decimal(idft(freq,len(freq)),10)


def calculate_fft_num(a,b):

    output=[]
    x=np.str(a)
    y = np.str(b)
    dft_x = fft(x)
    dft_y =fft(y)
    vector_0=complex(0,0)
    freq = []
    for i in range(0, max(len(dft_x), len(dft_y))):
        if (i < min(len(dft_x), len(dft_y))):
            temp = complex(dft_x[i] * dft_y[i])
            freq.append(temp)
        else:
            freq.append(vector_0)


    output = np.fft.ifft(freq)
    output = to_decimal(output, 10)

    return output

def fft_own(x):
    N = len(x)
    if N <= 1: return x
    even = fft_own(x[0::2])
    odd = fft_own(x[1::2])
    T = [exp(-2j * pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + \
           [even[k] - T[k] for k in range(N // 2)]

def ifft_own(x):
    output=[]
    for i in range(0, len(x)):
        x[i].conjugate()
    x=fft_own(x)
    for i in range(0, len(x)):
        x[i].conjugate()

    for i in range(0, len(x)):
        x[i]= x[i].real/len(x)
    return x
@timing
def calculate_fft_own(a,b):
    x = []
    y = []
    # size = max(check_which_2pow(a), check_which_2pow(b))
    size = max(len(str(a)), len(str(b)))

    size=check_which_2pow(max(a,b))

    # print(size)
    # size=check_which_2pow(size)

    x = to_decimal_table(a, 2*size)
    y = to_decimal_table(b, 2*size)

    # print(x)
    #  print(y)
    dft_x = fft_own(x)
    #  print(len(dft_x))

    dft_y = fft_own(y)
    #  print(len(dft_y))
    freq = []
    vector_0 = complex(0, 0)
    for i in range(0, len(dft_x)):
            temp = complex(dft_x[i] * dft_y[i])
            freq.append(temp)

    freq_t=fft_own(freq)

    freq_t.reverse()
    for i in range(0, len(freq_t)):
        freq_t[i]= round(freq_t[i].real/len(freq_t))
    return to_decimal(freq_t,10)
    #return to_decimal(ifft_own(freq), 10)
@timing
def calculate_standard(a,b):
    return a * b
@timing
def calculate_fft_numpy(a,b):
    size=check_which_2pow(max(a,b))

    # print(size)
    # size=check_which_2pow(size)

    x = to_decimal_table(a, 2*check_which_2pow(max(a,b)))
    y = to_decimal_table(b, 2*check_which_2pow(max(a,b)))

    dft_x=np.fft.fft(x)
    dft_y = np.fft.fft(y)


    freq =[]
    out=[]
    for i in range(0, len(dft_x)):
        temp = complex(dft_x[i] * dft_y[i])
        freq.append(temp)

    #output=np.fft.ifft(freq)
    #output=output.real
    output=idft(freq,len(freq))
    #output = ifft_own(freq)
    output=to_decimal(output,10)


    return output






#print(check_which_2pow(555555555555555555555555555555555555))
#print(check_which_2pow(1232343454565677687898706767475345435435345353))
a=148127498127489148127498127489
b=323131321312
c=31231232131
print("standard system    ",calculate_standard(a,b))
print("discrete fourier   ",calculate_mult_dfft(a,b))
print("own fast fourier   ",calculate_fft_own(a,b))
print("numpy fast fourier ",calculate_fft_numpy(a,b))

