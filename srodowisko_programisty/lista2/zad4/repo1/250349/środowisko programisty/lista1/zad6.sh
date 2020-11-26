

#! /bin/bash


#Wojciech Wróblewski zad6/lista1

# definiuję kolory do outputu
RED='\033[0;31m'
NC='\033[0m'

# przechodzę po plikach
for i in $(find $1 -type f)
do
	# wczytuję linię po linie z zawartości każdego pliku
	while IFS= read -r line
	do
		# wczytuje słowo po słowie z lini
		for t in $line
		do
			# wyświetlam  nazwa pliku + linia/wiersz + słowo
			echo -e "${RED}<plik>${NC}$(basename $i)   ${RED}<linia>${NC}$line   ${RED}<wyraz>${NC}$t"

		# chcemy odszukać słowa które wystąpiły więcej niż raz w jakiejś lini wobec tego
		#sortujemy i zliczamy wystąpienia, liczba zapisze się w 1 kolumnie outputu
		#jednak musimy jakoś dostać się do tych które wystąpiły 2 lub więcej razy.
		#czyli musimy wypisać te które w pierwszej kolumnie mają  liczbę równą lub większą 2
		#korzystamy tutaj z funkcji  awk
		#która wypisze tylko te wiersze które w  pierwszej kolumnie bd miały liczbą  większą lub równą 2
		done | sort | uniq -c  | sort -k 1n  | awk '{ if($1 >= 2) { $1=""; print }}'

	done < $i

done

