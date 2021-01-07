#include <string>
#include <cmath>
#include <iostream>

long long int ring_mod(long long int a, int p)
{
    return (a % p + p) % p;
}
long long int pow(int k, int n, int p)
{
    long long int w = 1;
    long long int a = (long long int)k;
    n = ring_mod(n, p);

    while (n > 0)
    {
        if (n % 2 == 1)
            w = ring_mod(w * a, p);

        a = ring_mod(a * a, p);
        n /= 2;
    }
    return w;
}

long long int gcdExtended(int a, int b, int *x, int *y)
{

    if (a == 0)
    {
        *x = 0, *y = 1;
        return b;
    }

    int x1, y1;
    int gcd = gcdExtended(b % a, a, &x1, &y1);
    *x = y1 - (b / a) * x1;
    *y = x1;

    return gcd;
}

long long int modularInverse(int a, int m)
{
    int x, y;
    int g = gcdExtended(a, m, &x, &y);
    if (g != 1)
        return -1;
    else
    {
        long long int out = (x % m + m) % m;
        return out;
    }
}

std::string addToDisplay(std::string output, std::string data)
{
    return output + data + " ";
}
