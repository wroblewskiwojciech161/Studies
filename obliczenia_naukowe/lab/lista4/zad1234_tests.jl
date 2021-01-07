#Wojciech Wróblewski
#testy funkcji do listy 4 kursu obliczenia naukowe 

include("./zad1234.jl")
using .Lista4
#data sets
x0 = [1.0, 3.0, 2.0, 6.0]
f0 = [-3.0, 4.0, 1.0, 4.0]
w0=[-3.0, 3.5, -0.5, -0.05]
#------------------------
x1 = [3.0, 1.0, 5.0, 6.0]
f1 = [1.0, -3.0, 2.0, 4.0]
w1 = [1.0, 2.0, -0.375,0.175]
#------------------------
x2 = [-1.0, 1.0, 2.0, 3.0, 4.0]
f2 = [2.0, 1.0, 2.0, -7.0, 5.0]
w2 = [2.0, -0.5, 0.5, -1.375, 1.308333333]
#------------------------
x3 = [-3.0, 7.0, -1.0, 2.0, 1.0]
f3 = [5.0, -1.0, 0.0, -3.0, 2.0]
w3 = [5.0, -0.6, 0.2375, -0.0125, 0.09375]
#------------------------
x7 = [2.0, 4.0, -5.0, 1.0]
f7 = [1.0, -1.0, 2.0, 1.0]
w7 = [59.0, -35.0, 1.0, 1.0]
#------------------------
w4 = ilorazyRoznicowe(x2,f2)
w8 = ilorazyRoznicowe(x1,f1)
w5 = [-43.0, 33.0, 41.0, -32.0, 5.0]
w6 = [-28.0, 44.0, -23.0, 4.0]

function expect(nazwa,idx,test,value)
    delta = 0.00001
    check = true
    for i in 1:length(test)
        if test[i] > value[i]+delta || test[i] < value[i]-delta
            check = false
        end
    end
    if  check 
        print("[test] ",nazwa," [numer] ",idx," [wynik] ",)
        printstyled("PASS\n";color =:green)
        println("============================================")
    else
        print("[test] ",nazwa," [numer] ",idx," [wynik] ",)
        printstyled("FAIL\n";color =:red)
        println(test)
        println("============================================")
    end
end

println("==================TESTING=====================")
expect("ilorazy różnicowe",0,ilorazyRoznicowe(x0, f0), w0)
expect("ilorazy różnicowe",1,ilorazyRoznicowe(x1, f1), w1)
expect("ilorazy różnicowe",2,ilorazyRoznicowe(x2, f2), w2)
expect("ilorazy różnicowe",3,ilorazyRoznicowe(x3, f3), w3)
expect("war netwon",1,warNewton(x2, w4, 2.0),2.0)
expect("war newton",2,warNewton(x2, w4, 10.0), 6210.4)
expect("war newton",2,warNewton(x1, w8, 10.0), 46.5)
expect("naturalna",1,naturalna(x2, f2), w5)
expect("naturalna",2,naturalna(x0, f0), w6)
expect("naturalna",3,naturalna(x7, f7), w7)






