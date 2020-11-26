
#Wojciech Wróblewski 250349
#zad4 lista3 obliczenia naukowe

include("./methods_module.jl")
using .Methods

delta = 10^(-5) / 2
epsilon = 10^(-5) / 2
maxit = 60

function f(x)
     return sin(x) - (x/2)^2
end

function pf(x)
    return cos(x) - (x/2)
end

println( mbisekcji(f, 1.5, 2.0, delta, epsilon))
println( mstycznych(f, pf, 1.5, delta, epsilon, maxit))
println(msiecznych(f, 1.0, 2.0, delta, epsilon, maxit))