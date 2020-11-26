
#Wojciech Wróblewski
#testy do zad1,zad2,zad3

include("./methods_module.jl")
using .Methods

max_iterations = 100000
delta =  10^(-5)
epsilon =  10^(-5)

function f(x)
    return x^3 - 5
end
  
function pf(x)
     return 3*(x^2)
 end

function get_error_type(method,error)
    if method == "mbisekcji"
        if error == 1
            return "Funkcja nie zmienia znaku w przedziale [a,b]."
        end
    end
    if method == "mstycznych"
        if error == 1
            return "Nie osiągnięto wymaganej dokładności w maxint iteracji."
        end
        if error == 2
            return "Pochodna bliska 0."
        end
    end
    if method == "mstycznych"
        if error == 1
            return "Nie osiągnięto wymaganej dokładności w maxint iteracji."
        end

    end    
end
function test(method,data_set)

    for i in 1:length(data_set)
        if method == "mbisekcji"
            result = mbisekcji(data_set[i][1],data_set[i][2],data_set[i][3],data_set[i][4],data_set[i][5])
        elseif method == "mstycznych" 
            result = mstycznych(data_set[i][1],data_set[i][2],data_set[i][3],data_set[i][4],data_set[i][5],data_set[i][6])
        elseif method == "msiecznych" 
            result = msiecznych(data_set[i][1],data_set[i][2],data_set[i][3],data_set[i][4],data_set[i][5],data_set[i][6])
        else
            return "niepoprawna deklaracja metody"
        end
       
        if last(result) == 0  
            println("numer testu ",i)
            println("parametry testu: ",data_set[i])
            println("wynik testu: ",result)
            println("błąd :", "NIE\n")
          
        else  
            println("numer testu ",i)
            println("parametry testu: ",data_set[i])
            println("wynik testu: ",result)
            println("błąd :", "TAK")
            println("typ błędu: ",get_error_type(method,last(result)),"\n")
          
        end    
    end
end
  


set1 = [
    (f,-3.0, 2.5,delta,epsilon),
    (f,1.5, 2.5,delta,epsilon),
    (f,1.0, 2.5, delta,epsilon), 
    (f,-4.0, 18.0, delta,epsilon) 
]

set2 = [
    (f, pf, -4.0,delta,epsilon, max_iterations),
    (f, pf, 2.5, delta,epsilon, max_iterations),
    (f, pf, 3.0, delta,epsilon, max_iterations),
    (f, pf, 0.0,delta,epsilon, max_iterations)
]

set3 = [
    (f, -4.0, 2.5, delta,epsilon,max_iterations),
    (f, 1.0, 2.0, delta,epsilon,max_iterations),
    (f, -25.0, 19.0,delta,epsilon,max_iterations),
    (f, 1.5, 4.0,delta,epsilon,max_iterations)
]

println("================================================================")
println("          Testy dla metody bisekcji.")
println("================================================================")
test("mbisekcji",set1)
println("================================================================")
println("          Testy dla metody stycznych.")
println("================================================================")
test("mstycznych",set2)
println("================================================================")
println("          Testy dla metody siecznych.")
println("================================================================")
test("msiecznych",set3)






