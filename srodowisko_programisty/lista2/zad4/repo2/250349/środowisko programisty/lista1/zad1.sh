

#! /bin/bash

#Wojciech Wróblewski zad1/lista1

# ten skrypt wypisuje nazwy wszystkich plików regularnych w zadanym folderowaniu
# podaje nazwy bez ścieżek do plików
for i in $(find $1 -type f)
do


	echo $(basename $i)
done

# jeżeli chcemy nazwy wraz ze ścieżkami możemy użyć kodu poniżej
#find a -type f







