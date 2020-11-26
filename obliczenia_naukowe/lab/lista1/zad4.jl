#Wojciech Wróblewski
#zad4 lista1

#funkcja wyznacza szukaną liczbe z przedziału (1,2)
function get_number()
 
    a = Float64(1.0)
    while nextfloat(a) * (Float64(1.0) / nextfloat(a)) == Float64(1.0)
        a = nextfloat(a)
    end
    
    return a
end


#funkcja wyznacza najmniejszą globalnie liczbę spełniającą równanie
function get_smallest_number()
 
    a = nextfloat(-Inf)
    while nextfloat(a) * (Float64(1.0) / nextfloat(a)) == Float64(1.0)
        a = nextfloat(a)
    end
    
    return a 
end


function value(x)
    return  x * (Float64(1.0) / x)
end



println("najmniejsza w przedziale z zadania : ",get_number())
println("najmniejsza globalnie : ",get_smallest_number())