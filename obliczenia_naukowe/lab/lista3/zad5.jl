#Wojciech Wróblewski 250349
#zad5 lista3 obliczenia naukowe

include("./methods_module.jl")
using .Methods

delta = 10^(-4)
epsilon = 10^(-4)
a1, b1 = 0.5, 1.0
a2, b2 = 1.0, 2.0

function f(x) 
    return 3 * x
end

function g(x)
    return exp(x)
end

function h(x) 
    return f(x) - g(x)
end


println(mbisekcji(h, a1, b1, delta, epsilon))
println(mbisekcji(h, a2, b2, delta, epsilon))
