#include <stdio.h>
int main() {
    int n, reversedN = 0, remainder, originalN;
    printf("\n\nAutor: Wojciech Wróblewski, numer indeksu: 250349\n\n");
    printf("Podprogram wczytuje liczbę naturalną n i sprawdza, czy jest palindromem.\n\n");
    printf("Wprowadź liczbę całkowitą: \n");
    scanf("%d", &n);
    originalN = n;

    
    while (n != 0) {
        remainder = n % 10;
        reversedN = reversedN * 10 + remainder;
        n /= 10;
    }

    
    if (originalN == reversedN)
        printf("\n%d jest palindromem.", originalN);
    else
        printf("\n%d nie jest palindromem.", originalN);

    return 0;
}
