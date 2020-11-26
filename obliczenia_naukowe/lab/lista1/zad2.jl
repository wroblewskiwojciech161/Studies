#Wojciech Wróblewski
#zad2 lista1

# badane typy
array = [Float16, Float32, Float64]

#dla zadanego typu funkcja zwraca wyrażenie Kahana
function get_eps(type)
     type(3.0) * (type(4.0) / type(3.0) - type(1.0)) - type(1.0)
end


for e in array
    println(e)
    println("eps method ",eps(e))
    println("kahan method ",get_eps(e))
    println("")
end
