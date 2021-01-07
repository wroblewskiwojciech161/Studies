%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
extern int yylex();
extern int yyparse();
extern FILE* yyin;
void yyerror(const char* s);
int euklides(int x);
int intpow(int x, int y);
int mod(int a);
%}

/* Bison declarations. */
%define api.value.type {long long}
%token NUM
%token '\n' QUIT comment '(' ')'
%left '+' '-'
%left '*' '/'
%right '^'

%% /* The grammar follows. */
input:
	%empty
| input line
;

line:
  '\n'
| exp '\n'          {	if ($1 < 0) $1 = mod($1);
			else $1 = $1 % 1234577;
			printf("\nWynik:\t%llu\n", $1); }
| comment
;
//ONP

exp: 
  NUM               { if ($1 >= 0) $$ = $1 % 1234577;
			else if ($1 < 0) $$ = mod($1);
			printf("%llu ", $$);}

| '-' NUM	    { $$ = mod($2); printf("%llu ", $$);	}
| exp '+' exp       { $$ = ($1 + $3) % 1234577; printf("+ ");	}
| exp '-' exp       { $$ = $1 - $3; printf("- ");   	}
| exp '*' exp       { $$ = ($1 * $3) % 1234577; printf("* ");	}

| exp '/' exp       { if ($3 > 0) $$ = $1 * euklides($3);
			else if ($3 == 0) printf("Błąd: Dzielenie przez 0.\n");
			else $$ = $1 * euklides(mod($3)); 
			printf("/ ");}	

| exp '^' exp	    { $$ = intpow($1, $3); printf("^ ");}  
| exp '^' '-' exp   { $$ = intpow(euklides($1), abs($4)); printf("^ ");}
| '(' exp ')'	    { $$ = $2;		}
| '-' '(' exp ')'   { $$ = -$3;		}
;

%%
void main() {
	yyin = stdin;
	do { 
		yyparse();
	} while(!feof(yyin));
}
void yyerror(const char* s) {
	fprintf(stderr, "Błąd: %s\n", s);
	exit(1);
}
// http://rosettacode.org/wiki/Modular_inverse#C
int euklides(int a)
{
	int b = 1234577;
	int b0 = b, t, q;
	int x0 = 0, x1 = 1;
	if (b == 1) return 1;
	while (a > 1) {
		q = a / b;
		t = b, b = a % b, a = t;
		t = x0, x0 = x1 - q * x0, x1 = t;
	}
	if (x1 < 0) x1 += b0;
	return x1;
}
//---------------------------------------------
int intpow(int x, int y) {
	long long result = 1;
	if (y > 0) {
		while (y > 0) {
			result = (result * x) % 1234577;
			y--;
		}
	}
	else if (y < 0) {
		x = euklides(x);
		y = abs(y);
		while(y > 0) {
			result = (result * x) % 1234577;
			y--;
		}
	}
	return result;
}
int mod(int x) {
	if (x > 0) x = -x;
	while (x < 0) {
		x = 1234577 + x;
	}
	return x;
}
