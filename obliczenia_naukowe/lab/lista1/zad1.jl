#Wojciech Wróblewski
#zad1 lista1

# badane typy
types = [Float16, Float32, Float64]

# funkcja wyznacza epsilon maszynowy
function get_machine_epsilon(_type)
        
    eps = _type(1.0)
    while _type(1.0) + eps / 2 > _type(1.0)
        eps /= 2
    end
    
    return eps
end

   
#funkcja wyznacza eta
function get_eta(_type)
                        
    eta = _type(1.0)
    while eta / _type(2.0) > _type(0.0) 
        eta /= _type(2.0)
    end
                            
    return eta
end


#funkcja oblicza MAX
function get_max(_type)
                                
    max = prevfloat(_type(1.0))
    while !isinf(max * 2)
        max *= 2
    end
                                    
    return max
end


    
for e in types
    println("========================================")                                     
    println(e)
    println("========================================")                               
    println("MAX ",floatmax(e))
    println("MAX computed ",get_max(e))
    println("")
    println("MACHINE EPSILON ",eps(e))
    println("MACHINE EPSILON computed ",get_machine_epsilon(e))
    println("")
    println("ETA ",nextfloat(e(0.0)))
    println("ETA computed ",get_eta(e))
    println("")                                                  
                                                                                                       
end                                               
              