%option noyywrap
%{

#include "calculator.tab.hpp"

int yylex();
%}

%%
^#(.|\\\n)*\n   ;
\\\n            ;
[ \t]+	        ;
[0-9]+          { yylval = atoi(yytext); return NUMBER; }
"+"             { return ADD;                           }
"-"             { return SUB;                           }
"*"             { return MULT;                          }
"%"             { return MODULO;                        }
"^"             { return POWER;                         }
"/"             { return DIVIDE;                        }
"("             { return LBRACKET;                      }
")"             { return RBRACKET;                      }
\n              { return QUIT;                          }
EOF             { return 0;                             }
.               { return ERROR;                         }
%%

