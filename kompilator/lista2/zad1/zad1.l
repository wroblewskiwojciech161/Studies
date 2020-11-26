
%{ 

/*Wojciech Wróblewski jftt lista2 zad1*/

#include<stdio.h> 
#include<string.h> 

int word_counter = 0,line_counter=0;

%} 

%% 

^[ \t]*\n*          ;
[ \t]+$             ;
[ \t]+              { fprintf(yyout, " "); }
[^ \t\n]+           { ECHO; word_counter++; };
\n                  { fprintf(yyout, "\n"); line_counter++; }

%% 
  
int yywrap(void){
    return 1;
} 

int main() 
{    

    extern FILE *yyout; 
  
    yyout = fopen("output.txt", "w"); 
    yylex(); 

    fprintf(yyout, "Liczba wyrazow : %d \t", word_counter);
    fprintf(yyout, "Liczba lini : %d ", line_counter);

    return 0; 
} 



