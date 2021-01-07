#Wojciech Wróblewski 250349
#zadania 1,2,3,4 lista 4, obliczenia naukowe

module Lista4
using Plots
export ilorazyRoznicowe, warNewton, naturalna, rysujNnfx

#------------------------------------------------------------------------------
#wejście :
#x - wektor długości n + 1 zawierający węzły
#f - wektor długości n + 1 zawierający wartości interpolowanej funkcji w węzłach 
#------------------------------------------------------------------------------
#wyjście:
#fx -  wektor zawierający ilorazy różnicowe
#------------------------------------------------------------------------------

function ilorazyRoznicowe(x::Vector{Float64}, f::Vector{Float64})
   
    fx = Vector{Float64}(undef, length(x))

    i = 1
    while i <= length(x)
        fx[i] = f[i]
        i = i + 1
    end

    i = 2
    while i <= length(x)
        j= length(x)
        while j >= i
            fx[j] = (fx[j] - fx[j - 1]) / (x[j] - x[j - i + 1])
            j = j - 1
        end
        i = i + 1
    end

    return fx
end

#------------------------------------------------------------------------------
#wejście :
#x -  wektor długości n + 1 zawierający węzły
#fx - wektor długości n + 1 zawierający ilorazy różnicowe
#t -  punkt, w którym należy obliczyć wartość wielomianu
#------------------------------------------------------------------------------
#wyjście:
#nt – wartość wielomianu w punkcie t.
#------------------------------------------------------------------------------

function warNewton(x::Vector{Float64}, fx::Vector{Float64}, t::Float64)
     
    nt = fx[length(x)]

    i = length(x) - 1
    while i >= 1
        nt = fx[i] + (t-x[i]) * nt
        i = i - 1
    end
    return nt
end

#------------------------------------------------------------------------------
#wejście :
#x -  wektor długości n + 1 zawierający węzły
#fx - wektor długości n + 1 zawierający ilorazy różnicowe
#------------------------------------------------------------------------------
#wyjście:
#a – wektor długości n + 1 zawierający obliczone współczynniki postaci naturalnej
#------------------------------------------------------------------------------

function naturalna(x::Vector{Float64}, fx::Vector{Float64})

    len = length(x)
    a = Vector{Float64}(undef, len)
    a[len] = fx[len]

    i = len - 1
    while i >= 1
        a[i] = fx[i] - a[i + 1] * x[i]

        j = i + 1
        while j <= len - 1
            a[j] = a[j] - a[j + 1] * x[i]
            j = j + 1
        end
   
        i = i - 1
    end 

    return a
end

#------------------------------------------------------------------------------
#wejście :
#f – funkcja f(x) zadana jako anonimowa funkcja
#a,b – przedział interpolacji
#n – stopień wielomianu interpolacyjnego
#------------------------------------------------------------------------------
#wyjście:
#– funkcja rysuje wielomian interpolacyjny i interpolowaną funkcję w przedziale [a, b].
#------------------------------------------------------------------------------

function rysujNnfx(f, a :: Float64, b :: Float64, n :: Int)
   
    MAX_NODES = n + 1
    EXPAND_CONST = 25
    LIMIT = MAX_NODES * EXPAND_CONST
    ZERO = Float64(0.0)
    
    x = Vector{Float64}(undef, MAX_NODES)
    y = Vector{Float64}(undef, MAX_NODES)
    fx = Vector{Float64}(undef, MAX_NODES)
    y_val = Vector{Float64}(undef,LIMIT)
    x_val = Vector{Float64}(undef,LIMIT)
    y_val_interpolated = Vector{Float64}(undef,LIMIT)

    kh = ZERO
    h = (b-a)/(MAX_NODES-1)

    i = 1
    while i <= MAX_NODES
        x[i] = a + kh
        y[i] = f(x[i])
        kh += h
        i=i+1
    end

    fx = ilorazyRoznicowe(x, y)
    h = (b - a)/(LIMIT-1)
    kh = ZERO

    i = 1
    while i <= LIMIT
        x_val[i] = a + kh
        y_val_interpolated[i] = warNewton(x, fx, x_val[i])
        y_val[i] = f(x_val[i])
        kh += h
        i=i+1
    end
 
    filename = string("plot", f, "", n, ".png")
    plot_title = "Interpolacja dla wielomianu stopnia $n"
    plot([x_val,x_val],[y_val,y_val_interpolated],title=plot_title, xlabel="x", ylabel="f(x)",line=(0.5, 3), label=[ "przebieg rzeczywisty" "przebieg interpolacji"])
    savefig(filename)
    
    end
end