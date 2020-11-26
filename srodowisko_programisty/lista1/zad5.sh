#! /bin/bash

#Wojciech Wróblewski zad5/lista1


# przechodzę po plikach
for i in $(find $1 -type f)
do

	#w każdej lini należącej do zawartości pliku zamieniam a na A
	while read line
	do
		# do zamiany korzystam z komendy sed
		#flaga -i oznacza że nie bd printfować wyniku tylko pracować na pliku
		# w funkcji sed;
		# s- oznacza substitution
		# zamieniamy a na A  a/A
		# g - globalnie tz. jak tego nie damy to zamieni tylko pierwsze wystąpienie
		sed -i  's/A/a/g' $i

	done < $i
done


