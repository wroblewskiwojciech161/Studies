#! /bin/bash

#Wojciech Wróblewski zad3/lista1

file_path=$(echo $2 | cut -d@ -f2 | cut -d/ -f2- | cut -d? -f1 | sed 's/.$//')
rm -r  ${file_path##/*/}
svn export -r $1 $2

echo "===================="
echo "STATYSTYKI"
echo "===================="

for file in $(find ${file_path##/*/}/ -type f)
do
    tr -d '[:punct:]' < "$file" | tr '[A-Z] ' '[a-z]\n'  |  sed '/^$/d;s/[[:blank:]]//g'| sort -u 

done | sort | uniq -c 



