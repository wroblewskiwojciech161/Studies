#Wojciech Wróblewski
#zad3 lista1

# touple przechowujące zadane przedziały
bounds = [(Float64(0.5),Float64(1.0))
          (Float64(1.0),Float64(2.0))
          (Float64(2.0),Float64(4.0))]


#zwraca deltę na podstawie wartości dolnej granicy przedziału

function get_delta(a)
    return nextfloat(a) - a
end 

# zwraca t kolejnych bitstringów zaczynając od dolnej granicy przedziału a

function show_bitstrings_lowerbound(a,b, t)
    delta = get_delta(a)
    for k in 1:t
        x = Float64(a) + k * delta
        println(bitstring(x))
    end
end

# zwraca t kolejnych bitstringów zaczynając od górnej granicy przedziału b

function show_bitstrings_upperbound(a, b, t)
    delta = get_delta(a)
    for k in 1:t
        x = Float64(b) - k * delta
        println(bitstring(x))
    end
end


# liczba kolejnych (przesuniętych o delta od poprzednika)
# bitstringów do zaprezentowania dla danego przedziału
s = 3

for a in bounds
    println("") 
    println("Przedział ", a)
    println("=================================================")
    show_bitstrings_lowerbound(a[1],a[2],s)
    for i=1:3
        println(".")
    end
     show_bitstrings_upperbound(a[1],a[2],s)
    
end

println("")
println("Wartości delt ale zadanych różnych 3 przedziałów.")
println("=================================================")
for a in bounds
    println("delta dla przedziału [",a,"] to ", get_delta(a[1]))
    
end
