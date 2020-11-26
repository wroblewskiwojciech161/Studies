#! /bin/bash

#Wojciech Wróblewski zad2/lista1

#funkcja cat otworzy wszystkie pliki regularne , następnie :
# xargs wylistuje ich zawartość  czyli słowa w jednej lini
# dodając flagę -n1 wylistuje je linia po lini
# w rozwiązaniu traktuję że słowo pisane  z dużych czy małych liter to to samo słowo
# aby zachować case sensitivity należy usunąć  komendę  tr która zamienia
# wielkie litery na małe 
# pod koniec wystarczy posortować aby ustawić słowa takie same  koło siebie 
# i zastosować komendę uniq -c do policzenia

cat $(find $1/ -type f)  | xargs -n1 | tr '[A-Z] ' '[a-z]\n' | sort | uniq -c 


