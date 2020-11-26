#include<stdio.h>
#include<time.h>
#include<stdlib.h>

typedef struct ListElement {
    int data;
    struct ListElement * next;
   
} ListElement_type;


// metoda wyswietlajca queue
void print(struct ListElement *head){
struct ListElement* current = head->next;
 if(current == NULL){

 printf("queue is empty\n");
}
  // przechodzimy po liscie i wyswietlamy wezly
 while(current!=NULL){
     printf("%d ",current->data);
     current=current->next;
 }   
}


// dodaj do queue
void enqueue(struct ListElement *head, int data){
    struct ListElement *new=(struct ListElement*)malloc(sizeof(struct ListElement));
    struct ListElement *current=(struct ListElement*)malloc(sizeof(struct ListElement));
    current=head;
    if( head == NULL){
        new->data=data;
        new->next=NULL;
        head=new;
    }
    else{
        new->data=data;
        new->next=NULL;
        while(current->next !=NULL){
            current=current->next;
        }
        current->next=new;


    }
    

}
//metoda usuwajaca element z queue
void dequeue(struct ListElement *head){
   struct ListElement* startPtr =head;
    if(startPtr->next == NULL ){
        printf("nothing to dequeue\n");
    }else{

    struct ListElement* first = startPtr->next;
    struct ListElement* second = first->next;
    

    startPtr->next = second;
    free(first);
    }

}

int main(){

struct ListElement *head=(struct ListElement*)malloc(sizeof(struct ListElement));


    printf("\n\nDostepne operacje?\n");
    printf("1. Dodac element do kolejki.\n");
    printf("2. Usun element .\n");
    printf("3. Pokaz liste .\n");
    int operation;
    int data;
    scanf("%d",&operation);
    while(1){

        switch (operation)

        {
        case 1:
             printf("Podaj wartosc do dodania:");
             scanf("%d",&data);
             enqueue(head,data);
             print(head);
             printf("\n");

            break;
	case 2:
            dequeue(head);
            print(head);
            printf("\n");
            break;
        case 3:

            print(head);
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




