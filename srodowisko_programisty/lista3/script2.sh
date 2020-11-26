#!/bin/bash

#Wojciech Wróblewski zad2/lista3

# pobieram file path bez ostatniego slasha (funkcja sed) 
file_path=$(echo $2 | cut -d@ -f2 | cut -d/ -f2- | cut -d? -f1 | sed 's/.$//')

# jezeli folder root o danej nazwie istniał w katalogu to go usuwam
# wyrażenie ${file_path##/*/} zwraca nam nazwę folderu root z linku w przypadkach na liście było "a"
rm -r  ${file_path##/*/}
svn export -r $1 $2

# wyswietlam statystyki
echo "===================="
echo "STATYSTYKI"
echo "===================="



#funkcja cat otworzy wszystkie pliki regularne , następnie :
# xargs wylistuje ich zawartość  czyli słowa w jednej lini
# dodając flagę -n1 wylistuje je linia po lini
# w rozwiązaniu traktuję że słowo pisane  z dużych czy małych liter to to samo słowo
# aby zachować case sensitivity należy usunąć  komendę  tr która zamienia
# wielkie litery na małe 
# pod koniec wystarczy posortować aby ustawić słowa takie same  koło siebie 
# i zastosować komendę uniq -c do policzenia


cat $(find ${file_path##/*/}/ -type f)  | xargs -n1  | tr '[A-Z] ' '[a-z]\n' | sort | uniq -c


#po uzyskaniu statystyk usuwam folder root
rm -r  ${file_path##/*/}



