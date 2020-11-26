#! /bin/bash

#Wojciech Wróblewski zad3/lista1

#przechodzę w pętli po wszystkich plikach regularnych
# na początku usuwam punktatory (opcjonalnie na wszelki wypadek jakby były)
# znowu traktuję że słowo z dużych i małych liter to to samo 
# żeby zachować case  sensitivity należy usunąć komendę tr
# funkcja sed usuwa białe znaki , w przeciwnym wypadku ich liczba pojawiłaby się 
# w statystykach (wykonanych przez ten skrypt)
# usuwamy duplikaty w pliku funkcją sort -u
#
# na samym końcu jak mamy wylistowane słowa z wszystkich plików
#(wiedząć żę w plikach nie  było duplikatów) zliczam je najpierw
# sortując aby były koło siebie
# i dodając uniq - c 

for file in $(find $1 -type f)
do
    tr -d '[:punct:]' < "$file" | tr '[A-Z] ' '[a-z]\n'  |  sed '/^$/d;s/[[:blank:]]//g'| sort -u 

done | sort | uniq -c 


