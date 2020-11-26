#Wojciech Wróblewski
#lista2 zad6

iterations = 40
parameters = [(-2.0, 1.0), (-2.0, 2.0), (-2.0, 1.99999999999999), (-1.0, 1.0), (-1.0, -1.0), (-1.0, 0.75), (-1.0, 0.25)]

# oblicza iteracyjnie zadaną formułę (liczba iteracji -> iterations)
function recursion_formula(iterations,c, x)
    if iterations == 0
         return Float64(x)
    else
      x = Float64(recursion_formula(iterations-1, c, x))
        return Float64(x^2) + Float64(c)
    end
end


function get_data(parameters,iterations)
    for i in 1:length(parameters)

        array=zeros(40)
        for k in 1:iterations
            array[k]=recursion_formula(k,Float64(parameters[i][1]),Float64(parameters[i][2]))
        end
        println(parameters[i])
        println(array)
        println("\n")
    end
end

get_data(parameters,iterations)


