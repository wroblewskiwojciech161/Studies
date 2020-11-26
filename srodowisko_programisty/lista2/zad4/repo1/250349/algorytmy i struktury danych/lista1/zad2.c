#include<stdio.h>
#include<time.h>
#include<stdlib.h>

typedef struct ListElement {
    int data;
    struct ListElement * next;
} ListElement_type;


//metoda wyswietlajaca liste
void print(struct ListElement *head){
struct ListElement* current = head->next;
    if(current == NULL ){
        printf("Lista jest pusta\n");
    }else{
    while (current != NULL)
    {
       printf("%d  ",current->data);
       current=current->next;
    }

    printf("\n");
    
    }
}

//metoda wyswietlajaca dane do zadania z porownania czasu
void compareTime(struct ListElement *head){


struct ListElement *startPtr=head;
int temp=0;

clock_t time_req;

    time_req=clock();
    for(int k=0;k<10000;k++){
       int number = rand()%1000;
       temp=0;

      while(temp != number){

        startPtr=startPtr->next;    
        temp++;
      }
    number=0;
    startPtr=head;
    }
  
    time_req=clock()-time_req;
    printf("czas do  losowego elementu : %f\n", (double)(time_req/1000)/CLOCKS_PER_SEC);


   struct ListElement *startPtr2=head;
int temp2=0;

clock_t time_req2;

    time_req2=clock();
    for(int k=0;k<10000;k++){
       int number2 = 778;
       temp2=0;

      while(temp2 != number2){

        startPtr2=startPtr2->next;    
        temp2++;
      }
    number2=0;
    startPtr2=head;
    }
  
    time_req2=clock()-time_req2;
    printf("czas do  stalego elementu : %f\n", (double)(time_req2/1000)/CLOCKS_PER_SEC);


}
//metoda pokazujaca funkcje merge dla 2 list 
void merge(struct ListElement *head1,struct ListElement *head2){
    struct ListElement* current = head1;
    
    while(current->next!= NULL){
        current=current->next;
    }
    current->next=head2->next;

    print(head1);
}
//metoda dodajaca element
void add(struct ListElement *head, int data){
    struct ListElement *new=(struct ListElement*)malloc(sizeof(struct ListElement));
    if(head == NULL ){
        head->data=data;
        head->next=NULL;
    }
    else{
     new ->data = data;
     new ->next=NULL;
     struct ListElement* current = head;
    
     while(current->next!= NULL){
        current=current->next;
     }
    //wczesniejszy ostatni od teraz
    //wskazuje na nowy ktory jest nowym ostatnim
     current->next= new;
    }

}
// metoda usuwa element z listy o zadanym indeksie
void delByValue(struct  ListElement *head, int data){

     struct ListElement* startPtr =head;
     struct ListElement*  first;
     struct ListElement*  second;
  
   
    if(startPtr == NULL  ){
        printf("nothing to dequeue");
    }else{
        int temp=0;
        while(temp != data){

                startPtr=startPtr->next;
                temp++;
         }
 
    
        first = startPtr->next;
        second = first->next;
        startPtr->next = second;
        free(first);
        }
}

int main(){

struct ListElement *head=(struct ListElement*)malloc(sizeof(struct ListElement));
struct ListElement *head1=(struct ListElement*)malloc(sizeof(struct ListElement));
struct ListElement *head2=(struct ListElement*)malloc(sizeof(struct ListElement));
struct ListElement *head3=(struct ListElement*)malloc(sizeof(struct ListElement));



    printf("\n\nDrogi uzytkowniku! Co chcesz zrobic?\n");
    printf("1. Dodac element na poczatek listy.\n");
    printf("2. Usun element o indeksie :.\n");
    printf("3. zaprezentuj metode merge dla 2 list :.\n");
    printf("4. porownaj czasy :.\n");
    int operation;
    int data;
    scanf("%d",&operation);
    while(1){

        switch (operation)

        {
        case 1:
             printf("Podaj wartosc do dodania:");
             scanf("%d",&data);
             add(head,data);
             print(head);

            break;
        case 2:
            printf("Podaj index do usuniecia:");
            scanf("%d",&data);
            delByValue(head,data);
            print(head);
            break;
        case 3:

            for(int i=0 ; i<20 ; i++){
                add(head1,rand()%100);
                add(head2,rand()%100);
            }
            printf("pierwsza lista :\n");
            print(head1);
            printf("druga lista :\n");
            print(head2);
            printf("pierwsza lista + 2 lista :\n");
            merge(head1,head2);
            break;
	case 4:

            for(int i=0 ; i<1000 ; i++){
                add(head3,rand()%1000);
            }
            compareTime(head3);
            break;


        default:
            break;
        }
        printf("wybierz operacje:");
        scanf("%d",&operation);

    
    }




    return 0;
}











