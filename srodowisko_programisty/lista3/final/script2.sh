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






#====================
#STATYSTYKI 15
#====================
#    10 a
#      3 aa
#     1 aaa
#     1 aaaab
#      1 aaabb
#      2 aab
#      1 aabab
#     1 aabbb
#      6 ab
#      1 aba
#      1 abaab
#      1 ababb
#      2 abb
#      1 abbab
#      1 abbbb
#     10 b
#      1 bab
#      3 bb
#      1 bbb




#====================
#STATYSTYKI 18
#====================
#     11 a
#      3 aa
#      1 aaa
#      1 aaaab
#      1 aaabb
#      2 aab
#      1 aabab
#      1 aabbb
#      6 ab
#      1 aba
#      1 abaab
#     1 ababb
#      2 abb
#      1 abbab
#      1 abbbb
#     10 b
#      1 bab
#      3 bb
#      1 bbb
#      4 c
#      2 d


