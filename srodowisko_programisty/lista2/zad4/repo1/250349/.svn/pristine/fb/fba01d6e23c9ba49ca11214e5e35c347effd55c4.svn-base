
Wojciech Wróblewski readme do programow
===========================================

kompilacja standardowa
w przypadku plików c :
gcc zad.c -o zad

kompilacja standardowa
w przypadku plików cpp :
g++ zad.c -o zad

===========================================
zad1 lista 3
===========================================


program uruchamiamy 
./zad1 --type x --comp "y"

w miesce x wpisujemy odpowiednio
radix
quick
insertion
merge

w miejsce y wpisujemy odpowednio

 <=
 >=

np: ./zad1 --type radix --comp "<="


Implementacja algorytmow taka sama jak z ostatniej listy .
Dane generowane do wykresow i analizy statystycznej.
poprzez 

./zad1 --stat dane.txt k

gdzie k to liczba potworzen do sredniej dla denego pomiaru
 
===========================================
zad2 lista 3
===========================================

program uruchamiamy dla permutacji
./zad3 -p 10 4
dla losowej tablicy
./zad2 -r 10 4

gdzie 10 to wielkosc tablicy a 4 to charakterystyka
Program wykonuje zadania z polecenia
-drukuje przestawienia, porównania, pivoty
-max liczbę swapów i porównań
- jako output tablica z zeznaczoną k- tą statystyką

dla czytelności 
opcja -p jest wtkonywana algorytmem randomized select
opcja -r algorytmem select



dane statystyczne znajduję się w pliku data_stat.pdf
Dane zwierają czas działania,porównania ,swapy, max porównania
 i min porównania dla danego algorytmu (dane dla kilku prób).
skróty s - select , rs - randomized select

dla każdej wielkości tablicy n  wynik był powtarzany 5 razy i uśredniany

można zauważyć że przy select
odchylenie standardowe pomiędzy max i min  liczbą porówań jest znacząco mniejsze
niż przy random select.

dane możemy wygenerować np
./zad2 -s 10 4 dane.txt
gdzie parametry 10 4 nie mają znaczenia bo 
przy generowaniu danych korzystamy z funkcji która
ma juz zaimplementowane wartości dla jakich przeprowadzany jest test  



===========================================
zad3 lista 3
===========================================

program uruchamiamy 
./zad3
podajemy rozmiar i kolejne lementy tablicy
funkcja zwraca 0 gdy nie istnieje i 1 gdy istanieje

dla statystyk wykorzystywana jest funkcja zad3

Wyznaczenie stałej doświadczalnie na podstawie Master Theorem 
polega na analizie problemu bin search.
Wiemy, że  T(n)=T(n/2) + O(c)
więc stałą jestśmy w stanie wyznaczyć
porównując prolblem z problemem dwukrotnie mniejszym

wyniki przedstawione śą w pdf  ->  data_stat

===========================================
zad4 lista3
===========================================

programy tą testowane przez tablice 
zaimplementowane w poziomie kodu.

Dane statystyczne data_stat.pdf zawierają 
porównanie zwykłych quicksort i dual_pivot quick sort z 
odpowiednikami, które bazują na algorytmie select.







