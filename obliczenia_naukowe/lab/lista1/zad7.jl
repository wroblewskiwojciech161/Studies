#Wojciech Wróblewski
#zad7 lista1

#zwraca wartość funkcji f dla argumentu x 
function func_f(x)
    return Float64(sin(x) + cos(3x))
end

# zwraca wartość funkcji h zależnej od n
function func_h(n)
    return Float64(1/2^n)
end

# zwraca przybliżoną wartość pochodnej
function derivitive_aprox(x_0,h)
    return Float64(Float64(func_f(x_0 + h)-func_f(x_0))/Float64(h))
end

#zwraca dokładną wartość pochodnej
function derivitive(x_0)
    return Float64(cos(x_0) - Float64(3.0)*sin(Float64(3.0)*x_0))
end

#zwraca błąd
function error(x_0,h,derivitive_x0)
    return abs(derivitive_aprox(x_0,h)-derivitive_x0)
end

# dokładna wartość pochodnej w punkcie 1.0
derivitive_x0 = derivitive(1.0)
println("exact derivitive ",derivitive_x0)

x_0 = Float64(1.0)


for n = 1:54
   
    println(n," ; "," 2^",-n ," ; ",derivitive_aprox(x_0,func_h(n))," ; ",func_h(n)+1.0," ; ",error(x_0,func_h(n),derivitive_x0))
end
