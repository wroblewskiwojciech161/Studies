#! /bin/bash

#Wojciech Wróblewski zad3/lista3

# pobieram file path bez ostatniego slasha (funkcja sed) 

file_path=$(echo $2 | cut -d@ -f2 | cut -d/ -f2- | cut -d? -f1 | sed 's/.$//')

# jezeli folder root o danej nazwie istniał w katalogu to go usuwam
# wyrażenie ${file_path##/*/} zwraca nam nazwę folderu root z linku w przypadkach na liście było "a"

rm -r  ${file_path##/*/}
svn export -r $1 $2


#wyświetlmy statystyki
echo "===================="
echo "STATYSTYKI"
echo "===================="


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


for file in $(find ${file_path##/*/}/ -type f)
do
    tr -d '[:punct:]' < "$file" | tr '[A-Z] ' '[a-z]\n'  |  sed '/^$/d;s/[[:blank:]]//g'| sort -u 

done | sort | uniq -c 


#po uzyskaniu statystyk usuwam folder root
rm -r  ${file_path##/*/}




#====================
#STATYSTYKI
#====================
#      7 a
#      3 aa
#      1 aaa
#      1 aaaab
#      1 aaabb
#      2 aab
#      1 aabab
#      1 aabbb
#      5 ab
#      1 aba
#      1 abaab
#      1 ababb
#      2 abb
#      1 abbab
#      1 abbbb
#      7 b
#      1 bab
#      3 bb
#      1 bbb



#====================
#STATYSTYKI
#====================
#      7 a
#      3 aa
#      1 aaa
#      1 aaaab
#      1 aaabb
#      2 aab
#      1 aabab
#      1 aabbb
#      5 ab
#      1 aba
#      1 abaab
#      1 ababb
#      2 abb
#      1 abbab
#      1 abbbb
#      7 b
#      1 bab
#      3 bb
#      1 bbb
#      3 c
#      2 d
#      1 dd











