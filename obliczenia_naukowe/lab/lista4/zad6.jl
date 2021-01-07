# Wojciech Wróblewski
# lista4 zadanie 6, obliczenia naukowe

include("./zad1234.jl")
using .Lista4

function func_abs(x)
    return abs(x)
end

function func_homo(x)
    return Float64(1.0) / (Float64(1.0) + x^Float64(2.0))
end
 
rysujNnfx(func_abs, -1.0, 1.0, 5)
rysujNnfx(func_abs, -1.0, 1.0, 10)
rysujNnfx(func_abs, -1.0, 1.0, 15)
rysujNnfx(func_homo, -5.0, 5.0, 5)
rysujNnfx(func_homo, -5.0, 5.0, 10)
rysujNnfx(func_homo, -5.0, 5.0, 15)
