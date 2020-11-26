#Wojciech Wróblewski
#lista2 zad1

# wektory po modyfikacji

x=  [2.718281828,-3.141592654,1.414213562,0.577215664,0.301029995]
y=  [1486.2497,878366.9879,-22.37492,4773714.647,0.000185049]

#liczy iloczyn skalarny z podpunktu a

function dot_product_forward(x,y,_type)
   
  result =_type(0)
    
  for i in 1:length(x)
    result += _type(x[i]) * _type(y[i])
  end
    
  return result
end

#liczy iloczyn skalarny z podpunktu c

function dot_product_reverse(x,y,_type)
   
  result =_type(0)
    
  for i in length(x):-1:1
    result += _type(x[i]) * _type(y[i])
  end
    
  return result
end
            
#liczy iloczyn skalarny z podpunktu c

function dot_product_c(x,y,_type)
    pos = zeros(_type, 0)
    neg = zeros(_type, 0)
    
    for i in 1:length(x)
        temp = _type(x[i]) * _type(y[i])
        if temp > 0
            push!(pos,temp) 
        else 
            push!(neg,temp)
        end
    end
        
    pos = sort(pos, rev = true)
    neg = sort(neg)
    
    return sum(pos) + sum(neg)
       
end

#liczy iloczyn skalarny z podpunktu d

function dot_product_d(x,y,_type)
    pos = zeros(_type, 0)
    neg = zeros(_type, 0)
    
    for i in 1:length(x)
        temp = _type(x[i]) * _type(y[i])
        if temp > 0
            push!(pos,temp) 
        else 
            push!(neg,temp)
        end
    end
        
    pos = sort(pos)
    neg = sort(neg, rev = true)
    
    return sum(pos) + sum(neg)
       
end
    
    

println("====================================")
println("type Float64")
println("====================================")
println("a  ",dot_product_forward(x,y,Float64))
println("b  ",dot_product_reverse(x,y,Float64))
println("c  ",dot_product_c(x,y,Float64))
println("d  ",dot_product_d(x,y,Float64))
println("====================================")
println("type Float32")
println("====================================")
println("a  ",dot_product_forward(x,y,Float32))
println("b  ",dot_product_reverse(x,y,Float32))
println("c  ",dot_product_c(x,y,Float32))
println("d  ",dot_product_d(x,y,Float32))
