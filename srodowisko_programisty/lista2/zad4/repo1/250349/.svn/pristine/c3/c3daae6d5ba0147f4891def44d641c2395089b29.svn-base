
#! /bin/bash

#Wojciech Wróblewski zad4/lista1


# dla lepszego wyglądu outputu definiuję kolory 
RED='\033[0;31m'
NC='\033[0m' 

# przechodzę po plikach w danym poddrzewie katalogów
for i in $(find $1 -type f)
do

	#następnie wczytuję zawartość pliku  linia po lini 
	while IFS= read -r line
	do

		#przechodzę słowo po słowie w danej lini/wierszu
		for t in $line
		do
		# wypisuję  nazwę pliku + linię/wiersz + słowo
		echo -e "${RED}<PLIK>${NC}$(basename $i) ${RED}<WIERSZ>${NC}$line ${RED}<WYRAZ>${NC}$t"

		#przekazanie do funkcji sort usuwa duplikaty jeżeli takie samo słowo wystąpiło kilka razy w danej lini
		done | sort -u

	done < $i

done

