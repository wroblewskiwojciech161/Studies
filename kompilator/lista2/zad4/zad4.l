%{

/*Wojciech Wróblewski jftt lista2 zad4*/

#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<math.h>
#include<string.h>
#define SIZE 100


bool to_many_args = false;
bool invalid_operator = false;
bool invalid_number = false;
int stack[SIZE];
int pointer = 0;

void handle_error_message(char* error){
 
    if( strcmp("stack_err",error)==0)
      printf("\nstack_error- stack overflow.\n");

    else if(strcmp("less_arguments",error)==0)
      printf("\nless number of arguments than needed.\n");

    else if(strcmp("invalid_operator",error)==0)
      printf("\n invalid_operator,");

    else if(strcmp("less_operators",error)==0 )
      printf("\nless number of operators than needed.\n");

    else if( strcmp("division_err",error)==0)
      printf("\ndivision error !!!\n");
}

int to_the_power(int x, int y){

  int out = 1;
  if(y == 0) return 1;
  else{

    for(int i =0; i< y ;i++){
      out *= x;
    }
  return out;
  }

} 

void push_on_stack(int x) {
  
    if (pointer < SIZE) {
        stack[pointer] = x;
        pointer++;
    }
    else {
        handle_error_message("stack_err");
      
    } 
}

int pop_from_stack()  {

    if (pointer != 0) {
        pointer--;
        return stack[pointer ];
    }
    else {

        to_many_args = true;
        return 9999999;
    }
}

void print_result(){
  if(pointer > 0){
    printf( " = %d \n ", pop_from_stack() );
  }
}

void handle_result(){

  if (pointer > 1){
    handle_error_message("less_operators");
  }

  else if (invalid_operator == true) {
      invalid_operator = false;
  }
  else if (to_many_args == true) {
      handle_error_message("less_arguments");
      to_many_args = false;
  }
  else if (invalid_number == true) {
      handle_error_message("division_err");
      invalid_number = false;
  }
  else {
      print_result();
  }
  invalid_number = false;
  invalid_operator = false;
  to_many_args = false;
  pointer = 0;
}
 

%}

%%


-?[0-9]+    { int temp1 =  atoi(yytext); push_on_stack(temp1);}

\+          { int temp1 = pop_from_stack(); int temp2 = pop_from_stack(); push_on_stack(temp1 + temp2);}

\-          {int temp1 = pop_from_stack();int temp2 = pop_from_stack();push_on_stack(temp2 - temp1);}

\^          { int temp1 = pop_from_stack(); int temp2 = pop_from_stack();push_on_stack(to_the_power(temp2,temp1));}  

\*          {int temp1 = pop_from_stack();int temp2 = pop_from_stack();push_on_stack(temp1 * temp2);}

\%          {
              int temp1 = pop_from_stack();
              if (temp1 == 0)invalid_number = true;
              else
              {
                  int temp2 = pop_from_stack();
                  push_on_stack(temp2 % temp1);
              }   
            }

\/          {
              int temp1 = pop_from_stack();
              if (temp1 == 0)invalid_number = true;
              else
              {
                int temp2 = pop_from_stack();
                push_on_stack(temp2 / temp1);
              }
            }

\n        {
            handle_result();    
		      }

[^("+"|"-"|"*"|"^"|"/"|"%"0-9) \n]   { handle_error_message("invalid_operator"); printf("'%c'\n",yytext[0]); invalid_operator = true;};

[[:blank:]]     ;
     
                
%%

int yywrap() {

    return 1;
}

int main() {

    yylex();
    return 0;
}
