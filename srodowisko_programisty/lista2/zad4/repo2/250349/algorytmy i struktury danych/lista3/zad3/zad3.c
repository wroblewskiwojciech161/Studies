#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#include<string.h>
#include <sys/sysinfo.h>
#include <sys/resource.h>
#include <errno.h>

/*Wojciech Wróblewski  lista3 AiSD  zad3*/
int counter_key_compare;


void generate_table(int tab[],int n)
{

    for( int i=0;i<n;i++)
    {
        tab[i]=rand()%100;
    }   

}
void list_table(int tab[],int n){
    for(int i=0;i<n;i++){
        printf("%d ",tab[i]);
    }
}

//implementacja binary search
int binarySearch(int tab[], int l, int r, int x) 
{   
    
   if (r >= l) 
   { 
        int mid = l + (r - l)/2; 
  
       
        counter_key_compare++;
        if (tab[mid] == x)  return 1; 
  
       
        counter_key_compare++;
        if (tab[mid] > x) return binarySearch(tab, l, mid-1, x); 
  
       
        return binarySearch(tab, mid+1, r, x); 
   } 
  
   
   return 0; 
} 
void insertion_sort(int tab[],int n,char order)
{
  //iterujemy po tablicy od 2 elementu
  for(int i=1;i<n;i++)
  {
  int key=tab[i];
  int j=i-1;
  //j w zakresie (0,i-1) podczas iteracji
    if (order == '<')
    {

            while(j>=0 && tab[j]>key)
            {
           
            //jesli poprzedni wiekszy to zamien
            tab[j+1]=tab[j];
            j=j-1;
            }          


    }
    if( order =='>')
    {

            while(j>=0 && tab[j]<key){
            //jesli poprzedni wiekszy to zamien
            tab[j+1]=tab[j];
            j=j-1;
            }
    }
    tab[j+1]=key;
  }
}
void copy_table(int tab1[],int tab2[],int n){
    for(int i=0; i<n;i++){
        tab1[i]=tab2[i];
    }

}
void zad3(int j, char *filename){

    FILE *fp;
    fp=fopen(filename,"w+");

    fprintf(fp,"n;time;compares problem n;compares problem n / 2\n");
    for(int i=1000;i<=100000;i+=1000){ 
            
                float time_sum=0;
                float compares_sum=0;float compares_half=0;
                int tab[i];int tab2[i/2];
                 generate_table(tab,i);
                 copy_table(tab2,tab,i/2);
                insertion_sort(tab2,i/2,'<');
                insertion_sort(tab,i,'<');


                for(int k=0;k<j;k++){
                       
                    int x =rand()%100;
                    //binary search dla problem i
                    counter_key_compare=0;
                    clock_t time_req=clock();
                    binarySearch(tab,0,i-1,x);
                    time_req=clock()-time_req;
                    compares_sum+=counter_key_compare;
                    time_sum+=(float)time_req/CLOCKS_PER_SEC;

                    //binary search dla problemu polowe mniejszego
                    counter_key_compare=0;
                    time_req=clock();
                    binarySearch(tab2,0,i/2-1,x);
                    time_req=clock()-time_req;
                    compares_half+=counter_key_compare;
                    time_sum+=(float)time_req/CLOCKS_PER_SEC;

                }
                fprintf(fp,"%d;%f;%f;%f\n",i,time_sum/j,compares_sum/j,compares_half/j);
              

        }
        fclose(fp);
}


int main(){
    printf("set length of array.\n");
    int n;
    int value;
    scanf("%d",&n);
    printf("Add values to table.\n");
    int tab[n];
    for(int i=0;i<n;i++){
        scanf("%d",&tab[i]);
    }
    printf("insert searching value. \n");
    scanf("%d",&value);

    insertion_sort(tab,n,'<');
    list_table(tab,n);
    printf("\n");
    printf("%d\n",binarySearch(tab,0,n-1,value));

   // zad3(5,"dane2.txt");
     

    return 0;
}