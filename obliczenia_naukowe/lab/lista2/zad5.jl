#Wojciech Wróblewski
#lista2 zad5

# obliczanie wyrażenia
#limit -> liczba iteracji
# p,r -> początkowe współczynniki
function formula(_type, p, r, limit)
    p =_type(p) 
    r =_type(r) 
    for i in 1:limit
        p = p + _type(r * p * (_type(1.0) - p))
    end
    return p
end

# obliczanie wyrażenia dla zadanej liczby iteracji 
# z uwzględnieniem obcięcia po  iteracji o zadanym numerze (cut_position)
#limit -> liczba iteracji
# p,r -> początkowe współczynniki
function formula_with_cut(_type, p, r, limit , cut_position)
    p = formula(_type,p,r,cut_position)
    p = trunc(p, digits=3)
    return formula(_type, p, r, limit - cut_position)

end
println("==================")
println("FLOAT 32")
println("==================")
println(formula(Float32, 0.01,3.0,40))
println("==================")
println("FLOAT 32 with cut")
println("==================")
println(formula_with_cut(Float32, 0.01,3.0,40,10))
println("\n")


println("==================")
println("FLOAT 32")
println("==================")
println(formula(Float32, 0.01,3.0,40))
println("==================")
println("FLOAT 64 ")
println("==================")
println(formula(Float64, 0.01,3.0,40))
println("\n\n")