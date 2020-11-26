#Wojciech Wróblewski 250349
#zad1,zad2,zad3 lista3 obliczenia naukowe

module Methods
export mbisekcji, mstycznych, msiecznych

"""
============================================
metoda bijekcji
============================================
Wejście: (f,a,b,delta,epsilon)
--------------------------------------------
f               – funkcja anonimowa
a,b             – przedział początkowy [a,b]
delta, epsilon  – predefiniowane dokładności
============================================
Wyjście: (r,v,iterations,error),gdzie
--------------------------------------------
r          – przybliżone rozwiązanie
v          – f(r)
iterations - liczba iteracji
err        - kod błędu
(0 jeżeli nie ma błędu,1 jeżeli funkcja nie zmienia znaku w [a,b])
"""
function mbisekcji(f, a::Float64, b::Float64, delta::Float64, epsilon::Float64)
    u = f(a)
    v = f(b)
    error = 0
    iterations = 0
    e = b - a
    if sign(u) == sign(v)
        error = 1 
        return (NaN, NaN, iterations, error)
    end
    while e > epsilon
        iterations += 1
        e /= 2
        c = a + e
        w = f(c)
        if abs(e) < delta || abs(w) < epsilon
            return (c, w, iterations, error)
        end
        if sign(w) != sign(u) 
            b = c
            v = w
        else
            a = c
            u = w
        end
    end
end

"""
=========================================================
Metoda stycznych
=========================================================
Wejście: (f,derivitive_f,x_0,delta,epsilon,max_iterations)
---------------------------------------------------------
f               – funkcja znonimowa
derivitive_f    - pochodna funkcji f
x_0             – początkowa wartość przybliżenia 
delta, epsilon  – predefiniowane dokładności
max_iterations  – predefiniowana maksymalna liczba iteracji
=========================================================
Wyjście: (r,v,iterations,error)
---------------------------------------------------------
r               – przybliżone rozwiązanie
v               – f(r)
iterations      – liczba wykonanych iteracji
error           – kod błędu

 0 - jeżeli błędu nie było
 1 - jeżeli nie osiągnięto predefiniowanej precyzji
 2 - pochodna bliska zero
  
"""
function mstycznych(f, derivitive_f, x_0::Float64, delta::Float64, epsilon::Float64, max_iterations::Int)
    v = f(x_0)
    error = 0
    iterations = 0

    if abs(derivitive_f(x_0)) < epsilon
        error = 2
        return (x_0, v, iterations, error)
    end
    if abs(v) < epsilon
        return (x_0, v, iterations, error)
    end

  
    for iterations in 1:max_iterations
        x_1 = x_0 - v / derivitive_f(x_0)
        v = f(x_1)
        if abs(x_1 - x_0) < delta || abs(v) < epsilon
            return (x_1, v, iterations, error)
        end
        x_0 = x_1
    end
    error = 1
    return (NaN, NaN, iterations, error)
end

"""
================================================
Metoda siecznych
================================================
Wejście (f,x_0,x_1,delta,epsilon,max_iterations)
------------------------------------------------
f               – funkcja anonimowa
x_0, x_1        – początkowe przybliżenia 
delta, epsilon  – predefiniowane dokładności
max_iterations  – maksymalna liczba iteracji
================================================
Wyjście: (r,v,it,err)
------------------------------------------------
r               – przybliżone rozwiązanie
v               – f(r)
iterations      – number of iterations
error           – kod błędu
    0 – brak błędu
    1 – nie uzyskano predefiniowanej dokładności
"""
function msiecznych(f, x_0::Float64, x_1::Float64, delta::Float64, epsilon::Float64, max_iterations::Int)
    error = 0
    f_x0 = f(x_0)
    f_x1 = f(x_1)
    for iteration in 1:max_iterations
        if abs(f_x0) > abs(f_x1)
            x_0, x_1, = x_1, x_0
            f_x0, f_x1 = f_x1, f_x0
        end
        s = (x_1 - x_0)/(f_x1 - f_x0)
        x_1 = x_0
        f_x1 = f_x0
        x_0 = x_0 - (f_x0 * s)
        f_x0 = f(x_0)
        if abs(x_1 - x_0) < delta || abs(f_x0) < epsilon
            return (x_0, f_x0, iteration, error)
        end
    end
    error = 1 
    return (NaN, NaN, iteration, error)
end

end