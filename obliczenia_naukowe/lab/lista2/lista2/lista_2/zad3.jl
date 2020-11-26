# Wojciech Wróblewski
# lista2 zad3

using LinearAlgebra

#funkcja hilb() ze strony Profesora Zielińskiego
function hilb(n::Int)
# Function generates the Hilbert matrix  A of size n,
#  A (i, j) = 1 / (i + j - 1)
# Inputs:
#	n: size of matrix A, n>=1
#
#
# Usage: hilb(10)
#
# Pawel Zielinski
        if n < 1
         error("size n should be >= 1")
        end
        return [1 / (i + j - 1) for i in 1:n, j in 1:n]
end


#funkcja matcond() ze strony Profesora Zielińskiego
function matcond(n::Int, c::Float64)
# Function generates a random square matrix A of size n with
# a given condition number c.
# Inputs:
#	n: size of matrix A, n>1
#	c: condition of matrix A, c>= 1.0
#
# Usage: matcond(10, 100.0)
#
# Pawel Zielinski
        if n < 2
         error("size n should be > 1")
        end
        if c< 1.0
         error("condition number  c of a matrix  should be >= 1.0")
        end
        (U,S,V)=svd(rand(n,n))
        return U*diagm(0 =>[LinRange(1.0,c,n);])*V'
end


#błąd względny metody gaussa
function gaussian_err(A,b,n,x)
    return norm(A \ b - x)/norm(x)
end

#bład względny
function inv_err(A,b,n,x)
    return norm(inv(A) * b - x)/norm(x)
end

#funkcja zwraca dane dotyczące macierzy hilberta
function get_hilbert_matrix_data()
        
    for n in 1:1:25
        calculate(hilb(n), n)
    end
end

#funkcja zwraca dane dotyczące macierzy losowej
function get_rand_matrix_data()
    
    n_storage = [5,10,20]
    c_storage = [1.0, 10.0, 10.0^3, 10.0^7, 10.0^12, 10.0^16]
    
    for n in n_storage
        for c in c_storage
            calculate(matcond(n,c), n)
        end
    end
end

#dla zadanej macierzy funkcja zwraca wartości jak n,rząd macierzy
# wskaźnik uwarunkowania, błędy względne metod 
function calculate(A, n)
    x = ones(Float64, n)
    b = A * x
    println("n: ",n)
    println("rank(A): ",rank(A))
    println("cond(A): ",cond(A))
    println("g_err: ",gaussian_err(A,b,n,x))
    println("inv_err: ",inv_err(A,b,n,x))
    println("---------------------------------")
end

println("===============================")
println("RANDOM MATRIX")
println("===============================")
get_rand_matrix_data()
println("")
println("")
println("===============================")
println("HILBERT'S MATRIX")
println("===============================")
get_hilbert_matrix_data()
