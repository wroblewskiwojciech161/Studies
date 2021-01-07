#Wojciech Wróblewski
# lista4 zadania 5, obliczenia naukowe

include("./zad1234.jl")
using .Lista4

function func_exp(x)
    return exp(x)
end

function func_sin(x)
    return (x^Float64(2.0))*sin(x)
end

rysujNnfx(func_exp, 0.0, 1.0, 5)
rysujNnfx(func_exp, 0.0, 1.0, 10)
rysujNnfx(func_exp, 0.0, 1.0, 15)
rysujNnfx(func_sin, -1.0, 1.0, 5)
rysujNnfx(func_sin, -1.0, 1.0, 10)
rysujNnfx(func_sin, -1.0, 1.0, 15)
