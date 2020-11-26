#Wojciech Wróblewski
#zad6 lista1

# zwraca argument x który jest potęgą 8
function get_x(x,_type)
    return _type(1.0/8^x)
end

#oblicza funkcję f dla zadanego argumentu i
function func_f(x,_type)
    return sqrt(x^2+_type(1.0))-_type(1.0)
end

#oblicza funkcję g dla zadanego argumentu i typu
function func_g(x,_type)
    return x^2/(sqrt(x^2+_type(1.0))+_type(1.0))
end


# porównnanie funkcji 
for i = 1:15
    println("8 ^ -",i," ; ",func_f(get_x(i,Float64),Float64)," ; ",func_g(get_x(i,Float64),Float64))

end