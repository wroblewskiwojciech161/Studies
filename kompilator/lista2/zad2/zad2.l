
%{ 

/*Wojciech Wróblewski jftt lista2 zad2*/

#include<stdio.h> 
#include<string.h> 


%} 

%x COMMENT
%x STRING_CASE1
%x STRING_CASE2
%x DOCUMENTATION_1
%x DOCUMENTATION_2

DOC1    \"\"\"   
DOC2    \'\'\'              

%%


\"                            { ECHO;BEGIN(STRING_CASE1); }
<STRING_CASE1>{  

    \\\\                       ECHO;
    \\\n                       ECHO;
    \\\"                       ECHO;
    \"                         {ECHO; BEGIN(INITIAL);}
    .                          ECHO;
}

\'                            {ECHO;BEGIN(STRING_CASE2);  }
<STRING_CASE2>{   

    \\\\                       ECHO;
    \\\n                       ECHO;
    \\\'                       ECHO;
    \'                         {ECHO; BEGIN(INITIAL);}
    .                          ECHO;
}

#                             {BEGIN(COMMENT);}
<COMMENT>{
    .                          ;
    \n                         { ECHO;BEGIN(INITIAL); };
}

{DOC1}                         { ECHO; BEGIN(DOCUMENTATION_1); }
<DOCUMENTATION_1>{

    \\\\                       ECHO;
    \\\n                       ECHO;
    \\\'                       ECHO;
    .|\n                       ECHO;
    {DOC1}                     { ECHO; BEGIN(INITIAL); }
}


{DOC2}                         {ECHO; BEGIN(DOCUMENTATION_2); }
<DOCUMENTATION_2>{

    \\\\                       ECHO;
    \\\n                       ECHO;
    \\\'                       ECHO;
    .|\n                       ECHO;
    {DOC2}                     { ECHO; BEGIN(INITIAL); }
}


%%
int yywrap() {
    return 1;
}

int main() 
{    

    yyout = fopen("output.py", "w");
    return yylex();
} 




