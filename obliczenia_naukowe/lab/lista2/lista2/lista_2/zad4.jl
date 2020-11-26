#Wojciech Wróblewski 
#lista2 zad4

using Polynomials
using Polynomials.PolyCompat

# wspolczynniki wielomianu
coefficients=Float64[1, -210.0, 20615.0,-1256850.0,53327946.0,-1672280820.0,
                         40171771630.0, -756111184500.0,11310276995381.0,
                          -135585182899530.0, 1307535010540395.0,-10142299865511450.0,
                          63030812099294896.0,-311333643161390640.0,1206647803780373360.0,
                        -3599979517947607200.0,8037811822645051776.0,-12870931245150988800.0,
                        13803759753640704000.0,-8752948036761600000.0,2432902008176640000.0                        
]
   
# wspolczynniki wielomianu po modyfikacji
coefficients2=Float64[1,  -210.0 - (2)^(-23), 20615.0,-1256850.0,53327946.0,-1672280820.0,
                         40171771630.0, -756111184500.0,11310276995381.0,
                          -135585182899530.0, 1307535010540395.0,-10142299865511450.0,
                          63030812099294896.0,-311333643161390640.0,1206647803780373360.0,
                        -3599979517947607200.0,8037811822645051776.0,-12870931245150988800.0,
                        13803759753640704000.0,-8752948036761600000.0,2432902008176640000.0
]

#generowanie wielomianu ze współczynników
function get_P(coefficients)
    coefficients = reverse(coefficients)
    return  Poly(coefficients)
end
#generowanie wielomianu z pierwiastków
function get_p()
    return poly(Float64[1.0:20.0;])
end


function get_data(coefficients)
    p =get_p()
    P =get_P(coefficients)
    #generowanie pierwiastków wielomianu funkcją biblioteczną
    c_roots = roots(P)
    println("k & zk & |P(zk)| & p(zk)| & |zk - k| ")
    for k in 1:20
        z = c_roots[k]
        println("$k & $z & $(abs(polyval(P, z))) & $(abs(polyval(p, z))) & $(abs(z - k)) ") 
  end
end

print("dane dla wielomianu wilkinsona")
println("\n")
get_data(coefficients)
println("\n")
println("\n")
print("dane do wielomianu wilkinsona po modyfikacji")
println("\n")
get_data(coefficients2)
