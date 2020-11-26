
%{

/*Wojciech Wróblewski jftt lista2 zad3*/

#include <stdio.h>
#include <stdbool.h>
#include<string.h>

int yywrap();
int yylex();

bool PRINT_DOC_COMMENTS = false;

void get_documentation(bool decision) {

    PRINT_DOC_COMMENTS = decision;

}

%}


ESCAPE              \\|\n
MULTILINE_START     \/{ESCAPE}*\* 
MULTI_DOC_1_START   \/{ESCAPE}*\*{ESCAPE}*\*.* 
MULTI_DOC_2_START   \/{ESCAPE}*\*{ESCAPE}*!.* 
SINGLE_OPEN         \/{ESCAPE}*\/  
SINGLE_DOC_OPEN1    \/\/\/ 
SINGLE_DOC_OPEN2    \/\/!


%x INLINE
%x INLINE_DOC_1
%x INLINE_DOC_2
%x MULTILINE
%x MULTILINE_DOC_1
%x MULTILINE_DOC_2
%x STRING

%%
\"                              {BEGIN(STRING);  ECHO;}
<STRING>{   
    \\\n                        ECHO;
    \\\\                        ECHO;
    \\\"                        ECHO;
    \"                          {ECHO; BEGIN(INITIAL);}
}

{SINGLE_OPEN}                   {BEGIN(INLINE);}
<INLINE>{
    .                           ; 
    .*\\\n                      ;     
    [^\\]\n                     {fprintf(yyout, "\n"); BEGIN(INITIAL);}
}

{MULTILINE_START}               BEGIN(MULTILINE);
<MULTILINE>{

    .|\n                        ;
    \*{ESCAPE}*\/               BEGIN(INITIAL);
}

{SINGLE_DOC_OPEN1}              {BEGIN(INLINE_DOC_1); if(PRINT_DOC_COMMENTS) ECHO;}
<INLINE_DOC_1>{

    .                           {if(PRINT_DOC_COMMENTS) ECHO;}
    .*\\\n                      {if(PRINT_DOC_COMMENTS) ECHO;}
    .?\n                        {if(PRINT_DOC_COMMENTS) ECHO; BEGIN(INITIAL);}
}

{SINGLE_DOC_OPEN2}              {BEGIN(INLINE_DOC_2); if(PRINT_DOC_COMMENTS) ECHO;}
<INLINE_DOC_2>{

    .                           {if(PRINT_DOC_COMMENTS) ECHO;}
    .*\\\n                      {if(PRINT_DOC_COMMENTS) ECHO;}
    .?\n                        {if(PRINT_DOC_COMMENTS) ECHO; BEGIN(INITIAL);}
}

{MULTI_DOC_1_START}               {BEGIN(MULTILINE_DOC_1); if(PRINT_DOC_COMMENTS) ECHO;}
<MULTILINE_DOC_1>{

    .|\n                        {if(PRINT_DOC_COMMENTS) ECHO;}
    [ \t\n\r]*\*\**{ESCAPE}*\/  {if(PRINT_DOC_COMMENTS) ECHO; BEGIN(INITIAL);}
}

{MULTI_DOC_2_START}               {BEGIN(MULTILINE_DOC_2); if(PRINT_DOC_COMMENTS) ECHO;}
<MULTILINE_DOC_2>{

    .|\n                        {if(PRINT_DOC_COMMENTS) ECHO;}
    [ \t\n\r]*\*\**{ESCAPE}*\/  {if(PRINT_DOC_COMMENTS) ECHO; BEGIN(INITIAL);}
}

%%

int yywrap() {
    return 1;
}

int main(int argc,char* argv[]) {

    char* DOC_PASS_ARG = "-documentation";

    if(argc > 1)
    {
        if(strcmp(argv[1], DOC_PASS_ARG) == 0)
        {
            get_documentation(true);
        }
        else get_documentation(false);
    } 
    else
    {
        get_documentation(false);
    }

    yyout = fopen("output.cpp", "w");
    return yylex();
}