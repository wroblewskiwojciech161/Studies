#include<stdio.h>
#include<time.h>
#include<stdlib.h>

typedef struct ListElement {
    int data;
    struct ListElement * next;
    struct ListElement * prev;
} ListElement_type;


//metoda wyswietlajaca liste cykliczna
void print(struct ListElement *head){
struct ListElement* current = head->next;
    if(head->next ==head->prev && head->prev ==NULL   ){
        printf("lista pusta");
    }
    else {

         printf("%d  ", head->data);
        while (current != head) {
        printf("%d  ", current->data);
        current=current->next;
        }

    }
}
// porownanie czasow
void compareTime(struct ListElement *head){


struct ListElement *startPtr=head;
int temp=0;

clock_t time_req;
    time_req=clock();
    for(int k=0;k<1000;k++){
       temp=0;

      while(temp != 756){

        startPtr=startPtr->next;    
        temp++;
      }

    }
    time_req=clock()-time_req;
    printf("czas do tego samego elementu : %f\n", (double)(time_req/1000)/CLOCKS_PER_SEC);

    struct ListElement *startPtr2=head;
    clock_t time_req2;
   
    time_req2=clock();
    for(int k=0;k<1000;k++){
       temp=0;
      int data = rand()%1000;
      while(temp != data){

        startPtr2=startPtr2->next;    
        temp++;
      }

    }
    time_req2=clock()-time_req2;
    printf("czas do losowego elementu : %f\n", (double)(time_req2/1000)/CLOCKS_PER_SEC);

 
}
//dodawanie elementow do listy
void add(struct ListElement *head, int data){
    struct ListElement *new=(struct ListElement*)malloc(sizeof(struct ListElement));
    
    if( head->next==NULL & head->prev==NULL ){

        head->data=data;
        head->prev=head;
        head->next=head;
    }
    else{
     new->next=NULL;
     new->prev=NULL;
     new ->data = data;
     //new ->next=NULL;
     struct ListElement* current = head;
    
     while(current->next!= head){
        current=current->next;

     }
    //wczesniejszy ostatni od teraz
    //wskazuje na nowy ktory jest nowym ostatnim
     new->prev=current;
     current->next= new;
     new->next=head;
     head->prev=new;
    }


}
//metoda prezentujaca funkcje merge
void merge(struct ListElement *head1,struct ListElement *head2){
   struct ListElement *last1;
   struct ListElement *last2;
   struct ListElement *temp=head1;
   struct ListElement *temp2=head2;
   
   
    last1=head1->prev;
    last2=head2->prev;

  
   while(temp->next != head1){
     
       temp=temp->next;
   }
   while(temp2->next != head2){

       temp2=temp2->next;
   }
 
   temp->next->prev=head2;
   temp->next=head2;
   
   temp2->next->prev=head1;
   temp2->next=head1;
   

   
  
   print(temp2->next);


}
//usuwanie elementow po indeksie z listy
void delByIndex(struct  ListElement *head, int data){

     struct ListElement* startPtr =head;
     struct ListElement*  first;
     struct ListElement*  second;
  
   
    if(startPtr->prev == NULL  ){
        printf("nothing to dequeue");
    }
    else{
   int temp=0;
    while(temp != data){
        //first->prev=startPtr->prev;
        first=startPtr;

       // startPtr->prev=startPtr;
        startPtr=startPtr->next;
        //second->prev=startPtr;
        second=startPtr->next;
 
        temp++;
        }
        //printf("first->data  %d", first->data);
        //printf("start->data  %d", startPtr->data);
        //printf("second->data  %d", second->data);

        first->next=second;
        second->prev=first;
        free(startPtr);
     //   head=first->next;

        }
}
// wyswietlanie liczby jednej przed i jednej po liczbie o zadanym indeksie
void printNearByIndex(struct ListElement *head,int index){
struct ListElement* current = head;
    if(head->next ==head->prev && head->prev ==NULL   ){
        printf("lista pusta");
    }
    else {
    int k=0;
    
     while(k!=index){
            current=current->next;
            k++;
        }
    printf("%d \n", current->data);

    printf("one back : %d ", current->prev->data);
    printf("one forward : %d ", current->next->data);
    
    }
    
}

int main(){

struct ListElement *head=(struct ListElement*)malloc(sizeof(struct ListElement));
struct ListElement *head1=(struct ListElement*)malloc(sizeof(struct ListElement));
struct ListElement *head2=(struct ListElement*)malloc(sizeof(struct ListElement));
struct ListElement *head3=(struct ListElement*)malloc(sizeof(struct ListElement));


 head->next=NULL;
 head->prev=NULL;

 head1->next=NULL;
 head1->prev=NULL;
    printf("\n\n Co chcesz zrobic?\n");
    printf("1. Dodac element na poczatek listy.\n");
    printf("2. Usun element o indeksie :.\n");
    printf("3. zaprezentuj metode merge dla 2 list :.\n");
    printf("4. porownaj czasy :.\n");
    printf("5. Pokaz liste :.\n");
    printf("6. Pokaz 1 element do przodu oraz do tylu od elementu o indeksie :.\n");

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
              printf("\n");

            break;
        case 2:
            printf("Podaj index do usuniecia:");
            scanf("%d",&data);
            delByIndex(head,data);
            print(head);
             printf("\n");
            break;
 	case 3:

            for(int i=0 ; i<20 ; i++){
                add(head1,rand()%100);
                add(head2,rand()%100);
            }
            printf("pierwsza lista :\n");
            print(head1);printf("\n");
            printf("druga lista :\n");
            print(head2);printf("\n");
            printf("pierwsza lista + 2 lista :\n");
            merge(head1,head2);printf("\n");
             printf("\n");
            break;
        case 4:

            for(int i=0 ; i<1000 ; i++){
                add(head3,rand()%1000);
            }
            compareTime(head3);
             printf("\n");
            break;
        case 5:
            print(head);
            printf("\n");
            break;
        case 6:
            printf("Podaj index do wyszukania:");
            scanf("%d",&data);
            printNearByIndex(head,data);
            printf("\n");

            break;

 	default:
            break;
        }
        printf("wybierz operacje:\n");
        scanf("%d",&operation);

    
    }




    return 0;
}












