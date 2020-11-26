#include<stdio.h>
#include<time.h>
#include<stdlib.h>

/* zadanie 1, lista 2, algorytmy i stuktury danych */

 
void swap(int *a, int *b){  
        int t = *a;  
        *a = *b;  
        *b = t;  
}  
//zmienne globalne do liczenia porownan
int counter_key_compare=0;
int counter_key_swap=0;
//wyswietla tablie
void list_table(int tab[],int n)
{
    for(int i=0;i<n;i++)
    {
        printf("%d ",tab[i]);
    }
}
//wyswietla inverse tab
void print_inverse(int tab[],int n)
{
    for( int i=n-1;i>=0;i--)
    {
        printf("%d ",tab[i]);
    }
}
//kopiuje tablie
void copy_table(int tab1[],int tab2[],int n)
{
    for(int i=0; i<n;i++)
    {
        tab1[i]=tab2[i];
    }

}
//------------------------------------------------------------------------------INSERTIONSORT
void insertion_sort(int tab[],int n,char order)
{
  //iterujemy po tablicy od 2 elementu
  for(int i=1;i<n;i++)
  {
  int key=tab[i];
  int j=i-1;
    //j in range (0,i-1) podczas iteracji
        if (order == '<')
        {

                while(j>=0 && tab[j]>key)
                {
                printf("compare : %d  %d \n ",tab[j],key);
                printf("swap : %d  %d \n ",tab[j+1],tab[j]);
                //jesli poprzedni wiekszy to zamien
                tab[j+1]=tab[j];
                j=j-1;
                counter_key_compare++;
                counter_key_swap++;
                }          


        }
        if( order =='>')
        {

                while(j>=0 && tab[j]<key){
                printf("compare : %d  %d \n ",tab[j],key);
		printf("swap : %d  %d \n ",tab[j+1],tab[j]);
                //jesli poprzedni wiekszy to zamien
                tab[j+1]=tab[j];
                j=j-1;
                counter_key_compare++;
		counter_key_swap++;
                }
        }
    //zapamietana wartosc klucza przypisz nizej
    printf("swap  %d  %d \n",key,tab[j+2]);
    counter_key_swap++;
    tab[j+1]=key;
  }
}

//------------------------------------------------------------------------------MERGE SORT

void merge(int tab[], int left, int mid, int right,char order) 
{ 
    //inicjalizacja indeksow
    int i, j, k; 
    // okreslenie wielkosci podtablic
    int length_1 = mid - left + 1; 
    int length_2 =  right - mid; 
  
    //tablice pomocnicze
    int L[length_1], R[length_2]; 
  
    // skopiuj dane do tablic pomocniczych L oraz R
    for (i = 0; i < length_1; i++) 
        L[i] = tab[left + i]; 

    for (j = 0; j < length_2; j++) 
        R[j] = tab[mid + 1+ j]; 
  
    // poczatkowy indeks pierwszej L tablicy
    i = 0; 
    // poczatkowy indeks drugiej R tablicy 
    j = 0; 
    k = left;

    //porownuj i wstawiaj mniejszy do tablicy wynikowej
    while (i < length_1 && j < length_2) 
    { 
        //wyswietlam zgodnie z poleceniem poownania 
        printf("compare : %d  %d \n ",L[i],R[j]);
        counter_key_compare++;
        //w zaleznosci od wybranego porzadku
        //asc
        if(order == '<'){
                if (L[i] < R[j]) 
                { 
                    printf("swap  %d  %d \n",tab[k],L[i]);
                    counter_key_swap++;                  
                    tab[k] = L[i]; 
                    i++; 
                    
                } 
                else
                { 
                    printf("swap  %d  %d \n",tab[k],R[j]);
                    counter_key_swap++;
                    tab[k] = R[j]; 
                    j++; 
                    
                } 
                k++; 
        }
        //dsc
        if(order =='>'){
                if (L[i] > R[j]) 
                { 
                    printf("swap  %d  %d \n",tab[k],L[i]);
                    counter_key_swap++;
                    tab[k] = L[i]; 
                    i++; 
                    
                } 
                else
                { 
                    printf("swap  %d  %d \n",tab[k],R[j]);
                    counter_key_swap++;
                    tab[k] = R[j]; 
                    j++; 
                    
                } 
                k++; 
        }
    } 
  
    // jesli zostana elementy w lewej podtablicy to je przepisz 
    while (i < length_1) 
    { 
        printf("swap  %d  %d \n",tab[k],L[i]);
        counter_key_swap++;
        tab[k] = L[i]; 
        i++; 
        k++; 
        
    } 
  
    // jezeli zostana elementy prawej to przepisz 
    while (j < length_2) 
    { 
        printf("swap  %d  %d \n",tab[k],R[j]);
        counter_key_swap++;
        tab[k] = R[j]; 
        j++; 
        k++; 
        
    } 
} 
  
// [l,r] zakres w sensie indeksowania podtablicy do posortowania
void merge_sort(int tab[], int l, int r,char order) 
{ 
    //jesli jest wiecej niz jedej element to ...
    if (l < r) 
    { 
        //wyznacz indeks m w polowie tablicy
        int m =(l+r)/2;
  
        // rekurancja - posortuj 2 podtablice i scal
        merge_sort(tab, l, m,order); 
        merge_sort(tab, m+1, r,order); 
  
        merge(tab, l, m, r,order); 
    } 
} 

//--------------------------------------------------------------------------------------QUICKSORT
void  quick_sort (int tab[], int lower, int upper,char order)  
{  
    if (lower < upper)  {
                //wyznaczenie pivota
                int pivot = tab[upper];  
                int i = (lower - 1);  
            
                for (int j = lower; j <= upper - 1; j++)  
                {  
                    printf("compare  %d  %d \n",tab[j],pivot);
                    counter_key_compare++;
                    if(order == '<')
                    {                         
                        if (tab[j] < pivot)  
                        { 
                            printf("swap  %d  %d \n",tab[i],tab[j]);
                            i++;  
                            swap(&tab[i], &tab[j]); 
                            counter_key_swap++;
                        }  
                    }
                    else
                    {         
                        if (tab[j] > pivot)  
                        {  
                            printf("swap  %d  %d \n",tab[i],tab[j]);
                            i++; 
                            swap(&tab[i], &tab[j]);  
                            counter_key_swap++;
                        }  
                    }       
                }  
                printf("swap  %d  %d \n",tab[i+1],tab[upper]);
                counter_key_swap++;
                //ustawianie pivot na właściwe miejsce
                swap(&tab[i + 1], &tab[upper]);

                int div= i + 1;  
                //rekurancja dla kolejnych podtablic bez juz ustawonego wczesniej elementu
                quick_sort(tab, lower, div - 1,order);  
                quick_sort(tab, div + 1, upper,order); 
            }    
}  
 
int main(int argc, char **argv)
{
    // pobieram z lini komend  litery ktore charakteryzuja dane sortowanie
    char sort =argv[2][0];// m,i,q
    //pobieram porzadek sortowania
    char order = argv[4][0];
  

    printf("Create array. Set size of array :\n");
    int n;
    scanf("%d",&n);
    int tab[n];
    printf("add elements:\n");
    for(int i=0;i<n;i++){
        scanf("%d",&tab[i]);
    }

    printf("\ntable ---------------------------\n");
    list_table(tab,n);printf("\n");
    printf("-----------------------------------\n");
    
    clock_t time_req;
    switch (sort)
    {
        case 'i':
            printf("Porownania----insertion_sort-----\n");
            time_req=clock();
            insertion_sort(tab,n,order);
            time_req=clock()-time_req;
            printf("Sorted --------------------------\n");
            list_table(tab,n);
            

            break;
        case 'm':

            printf("Porownania----merge_sort--------\n");
            time_req=clock();
            merge_sort(tab,0,n-1,order);
            time_req=clock()-time_req;


            printf("Sorted --------------------------\n");
            list_table(tab,n);
            
            break;
        case 'q':

            printf("Porownania--------quick_sort-----\n");
            time_req=clock();
            quick_sort(tab,0,n-1,order);
            time_req=clock()-time_req;

            printf("Sorted --------------------------\n");
             list_table(tab,n);
           
                break;
        default:
            printf("error.");
            break;
    }
            printf("\n");
            printf("Porownania : %d: \n",counter_key_compare);
            printf("Przestawienia kluczy : %d: \n",counter_key_swap);
            printf("Czas dzialania algorytmu :%lf\n",(double)time_req/CLOCKS_PER_SEC);
            printf("\n");printf("\n");
   

    return 0;
}
