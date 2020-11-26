#Wojciech Wróblewski 250349
#zad6 lista3 obliczenia naukowe

include("./methods_module.jl")
using .Methods

delta = 10^(-5)
epsilon = 10^(-5)
#maksymalna liczba iteracji
MAX = 60

function f1(x)
    return exp(1 - x) - 1
end

function f2(x)
    return x * exp(-x) 
end

function pf1(x)
     return -exp(1 - x)
end

function pf2(x)
      return -exp(-x) * (x - 1)
end

mbisekcji_parameters = [
    (f1, 0.5, 2.0, delta, epsilon), (f1, 0.5, 3.0, delta, epsilon),
    (f1, 0.0, 2.5, delta, epsilon),(f1, -2.0, 2.0, delta, epsilon),
    (f1, -5.0, 10.0, delta, epsilon),(f1, -10.0, 10.0, delta, epsilon),
    (f2, -0.3, 0.2, delta, epsilon), (f2, -1.0, 1.0, delta, epsilon),
    (f2, -0.5, 0.5, delta, epsilon),(f2, -2.5, 2.0, delta, epsilon),
    (f2, -8.0, 7.0, delta, epsilon),(f2, -20.0, 20.0, delta, epsilon)
]
mstycznych_parameters = [
   
    (f1, pf1,1.5, delta, epsilon, MAX),(f1, pf1, 2.0, delta, epsilon, MAX),
    (f1, pf1, 5.0, delta, epsilon, MAX),(f1, pf1, 8.0, delta, epsilon, MAX),
    (f1, pf1, 10.0, delta, epsilon, MAX), (f1, pf1, 15.0, delta, epsilon, MAX),
    (f1, pf1, 50.0, delta, epsilon, MAX), (f1, pf1, 500.0, delta, epsilon, MAX),
    (f1, pf1, 5000.0, delta, epsilon, MAX), (f2, pf2,1.0, delta, epsilon, MAX),
    (f2, pf2,2.0, delta, epsilon, MAX), (f2, pf2,5.0, delta, epsilon, MAX), 
    (f2, pf2,8.0, delta, epsilon, MAX), (f2, pf2,10.0, delta, epsilon, MAX),
    (f2, pf2,15.0, delta, epsilon, MAX), (f2, pf2,50.0, delta, epsilon, MAX),
    (f2, pf2, 500.0, delta, epsilon, MAX), (f2, pf2, 5000.0, delta, epsilon, MAX),
]
msiecznych_parameters = [
    (f1, -3.0,2.0, delta, epsilon, MAX), (f1, 0.0, 2.0, delta, epsilon, MAX),
    (f1,0.97,1.27, delta, epsilon, MAX),(f1,0.97,8.0, delta, epsilon, MAX),
    (f1,0.0,9.0, delta, epsilon, MAX),(f2, -0.1, 0.2, delta, epsilon, MAX),
    (f2, -2.0, 2.0, delta, epsilon, MAX), (f2, -8.0, 5.0, delta, epsilon, MAX),
    (f2, -0.1,0.23, delta, epsilon, MAX), (f2, -0.1, 5.0, delta, epsilon, MAX)
]

println("========================================================")
println("metoda bisekcji")
println("========================================================")
for i in 1:length(mbisekcji_parameters)
    p = mbisekcji_parameters[i]
    println(p[1],"  ",mbisekcji(p[1],p[2],p[3],p[4],p[5]),"  ",p)
end
println("========================================================")
println("metoda stycznych")
println("========================================================")
for i in 1:length(mstycznych_parameters)
    p = mstycznych_parameters[i]
    println(p[1],"  ",mstycznych(p[1],p[2],p[3],p[4],p[5],p[6]),"  ",p)
end
println("========================================================")
println("metoda siecznych")
println("========================================================")
for i in 1:length(msiecznych_parameters)
    p = msiecznych_parameters[i]
    println(p[1],"  ",msiecznych(p[1],p[2],p[3],p[4],p[5],p[6]),"  ",p)
end