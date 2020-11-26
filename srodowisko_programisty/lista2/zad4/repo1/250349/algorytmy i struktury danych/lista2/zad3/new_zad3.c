#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#include<string.h>

/*zad 3 lista 2  algorymty i struktury danych

zawiera implementacje  dual_pivot_quicksort 

*/

//pomocnicza funkcja swap
void swap(int *a, int *b) 
{ 
    int temp = *a; 
    *a = *b; 
    *b = temp; 
} 
//zmienne globalne do liczenia porownan
int counter_key_compare=0;
int counter_key_swap=0;
//wyswietla tablie
void list_table(int tab[],int n){
    for(int i=0;i<n;i++){
        printf("%d ",tab[i]);
    }
}
//wyswietla inverse tab
void print_inverse(int tab[],int n){
    for( int i=n-1;i>=0;i--){
        printf("%d ",tab[i]);
    }
}
//kopiuje tablie
void copy_table(int tab1[],int tab2[],int n){
    for(int i=0; i<n;i++){
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
            //printf("compare : %d  %d \n ",tab[j],key);
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
            //printf("compare : %d  %d \n ",tab[j],key);
            //jesli poprzedni wiekszy to zamien
            tab[j+1]=tab[j];
            j=j-1;
            counter_key_compare++;
            counter_key_swap++;
            }
    }
    //zapamietana wartosc klucza przypisz nizej
   // printf("swap  %d  %d \n",key,tab[j+2]);
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
        //printf("compare : %d  %d \n ",L[i],R[j]);
        counter_key_compare++;

        //w zaleznosci od wybranego porzadku
        //asc
        if(order == '<'){
                if (L[i] < R[j]) 
                { 
                    counter_key_swap++;
                    tab[k] = L[i]; 
                    i++; 
                    //printf("swap  %d  %d \n",tab[k],L[i]);
                } 
                else
                { 
                    counter_key_swap++;
                    tab[k] = R[j]; 
                    j++; 
                    // printf("swap  %d  %d \n",tab[k],R[j]);
                } 
                k++; 
        }
        //dsc
        if(order =='>'){
                if (L[i] > R[j]) 
                { 
                    counter_key_swap++;
                    tab[k] = L[i]; 
                    i++; 
                    //printf("swap  %d  %d \n",tab[k],L[i]);
                } 
                else
                { 
                    counter_key_swap++;
                    tab[k] = R[j]; 
                    j++; 
                    //printf("swap  %d  %d \n",tab[k],R[j]);
                } 
                k++; 
        }
    } 
  
    // jesli zostana elementy lewej to je przepisz 
    while (i < length_1) 
    { 
        counter_key_swap++;
        tab[k] = L[i]; 
        i++; 
        k++; 
        //printf("swap  %d  %d \n",tab[k],L[i]);
    } 
  
    // jezeli zostana elementy prawej to przepisz 
    while (j < length_2) 
    { 
        counter_key_swap++;
        tab[k] = R[j]; 
        j++; 
        k++; 
        //printf("swap  %d  %d \n",tab[k],R[j]);
    } 
} 
  
//l lewy index tablicy do posortowania
// r prawy indeks tablicy do posortowania
void merge_sort(int tab[], int l, int r,char order) 
{ 
    //jesli jest wiecej niz jedej element to ...
    if (l < r) 
    { 
        //wyznacz indeks m w polowie tablicy
        int m = (l+r)/2;
  
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
                    counter_key_compare++;
                    if(order == '<')
                    {                         
                        if (tab[j] < pivot)  
                        {  
                            i++;  
                            swap(&tab[i], &tab[j]); 
                            counter_key_swap++;
                        }  
                    }
                    else
                    {         
                        if (tab[j] > pivot)  
                        {  
                            i++; 
                            swap(&tab[i], &tab[j]);  
                            counter_key_swap++;
                        }  
                    }       
                }  
                counter_key_swap++;
                //ustawianie pivot na właściwe miejsce
                swap(&tab[i + 1], &tab[upper]);

                int div= i + 1;  
                //rekurancja dla kolejnych podtablic bez juz ustawonego wczesniej elementu
                quick_sort(tab, lower, div - 1,order);  
                quick_sort(tab, div + 1, upper,order); 
            }    
}  

//---------------------------------------------------------------------------------dual pivot

//partycjonowanie
int make_part(int tab[], int low, int high, int* left) 
{ 
    counter_key_compare++;
    if (tab[low] > tab[high]) {
        counter_key_swap++;
        swap(&tab[low], &tab[high]); 
    }
    //inicjalizacja indeksow i przypisanie dla pivot lefti right
    int j = low + 1; 
    int l = high - 1;
    int k = low + 1;
    int left_pivot = tab[low];
    int right_pivot = tab[high]; 

    while (k <= l) { 
           
        if (tab[k] < left_pivot)
        { 
            counter_key_compare++;
            counter_key_swap++;
            swap(&tab[k], &tab[j]); 
            j++; 
        } 
  
        else if (tab[k] >= right_pivot)
         { 

                counter_key_compare++;
                while (tab[l] > right_pivot && k < l)
                {
                    counter_key_compare++;
                        l--;    
                } 
                counter_key_swap++;
                swap(&tab[k], &tab[l]); 
                l--; 
                counter_key_compare++;

                if (tab[k] < left_pivot)
                { 
                    counter_key_swap++;
                    swap(&tab[k], &tab[j]); 
                    j++; 
                } 
        } 
        k++; 
    } 
    j--; 
    l++; 
    counter_key_swap+=2;
    //pivoty ustawione na ich wlasciwe miejse 
    swap(&tab[low], &tab[j]); 
    swap(&tab[high], &tab[l]); 
  
     //przypisanie lewego indeksu
    *left = j;
            
    //zwrocenie prawego indeksu
    return l; 
} 
void dual_pivot_quicksort(int tab[], int low, int high) 
{ 
    if (low < high) { 
        //indeksu pivotow
        int left, right;  
        
        //dokonaj partycjonowania
        right = make_part(tab, low, high, &left); 
        //wykonaj rekurencyjnie dual_pivot z otrzymanymi indeksami lefu i right
        dual_pivot_quicksort(tab, low, left - 1); 
        dual_pivot_quicksort(tab, left + 1, right - 1); 
        dual_pivot_quicksort(tab, right + 1, high); 
    } 
} 
  
//----------------------------------------------------------------------------

void generate_table(int tab[],int n)
{
    for( int i=0;i<n;i++){
        tab[i]=rand()%1000;
    }   
 

}

//metoda wykonujaca zad3
void zad3(int j, char *filename){

FILE *fp;
fp=fopen(filename,"w+");

 //printf("n;time;number of compares;number of swaps\n");
  fprintf(fp,"n;q_time;q_c;q_s;q__c/n;q_s/n,m_time;m_c;m_s;m__c/n;m_s/n,i_time;i_c;i_s;i__c/n;i_s/n;q_dual_time;q_dual_c;q_dual_s;q_dual__c/n;q_dual_s/n\n");
  for(int i=100;i<=10000;i+=100){ 
            //wyzerowanie
            float quicksort_c_sum=0;float quicksort_s_sum=0;
            float insertion_c_sum=0;float insertion_s_sum=0;
            float merge_c_sum=0;float merge_s_sum=0;
            float dual_quicksort_c_sum=0;float dual_quicksort_s_sum=0;
            float dual_quicksort_t_sum=0;float quicksort_t_sum=0;float insertion_t_sum,merge_t_sum=0;

            for(int k=0;k<j;k++){
                int tab_q[i],tab_i[i],tab_m[i],tab_dual_q[i];
                generate_table(tab_q,i);
                copy_table(tab_m,tab_q,i);
                copy_table(tab_i,tab_q,i);
                copy_table(tab_dual_q,tab_q,i);


                //quick
                counter_key_compare=0;
                counter_key_swap=0;
                clock_t time_req=clock();
                quick_sort(tab_q,0,i-1,'<');
                time_req=clock()-time_req;
                quicksort_c_sum+=counter_key_compare;
                quicksort_s_sum+=counter_key_swap;
                quicksort_t_sum+=(float)time_req/CLOCKS_PER_SEC;

                //merge
                counter_key_compare=0;
                counter_key_swap=0;
                time_req=clock();
                merge_sort(tab_m,0,i-1,'<');
                time_req=clock()-time_req;
                merge_c_sum+=counter_key_compare;
                merge_s_sum+=counter_key_swap;
                merge_t_sum+=(float)time_req/CLOCKS_PER_SEC;

                //insertion
                counter_key_compare=0;
                counter_key_swap=0;
                time_req=clock();
                insertion_sort(tab_i,i,'<');
                time_req=clock()-time_req;
                insertion_c_sum+=counter_key_compare;
                insertion_s_sum+=counter_key_swap;
                insertion_t_sum+=(float)time_req/CLOCKS_PER_SEC;

                //quick dual pivot
                counter_key_compare=0;
                counter_key_swap=0;
                time_req=clock();
                dual_pivot_quicksort(tab_dual_q,0,i-1);
                time_req=clock()-time_req;
                dual_quicksort_c_sum+=counter_key_compare;
                dual_quicksort_s_sum+=counter_key_swap;
                dual_quicksort_t_sum+=(float)time_req/CLOCKS_PER_SEC;
              
            }
            fprintf(fp,"%d;%f;%f;%f;%f;%f;%f;%f;%f;%f;%f;%f;%f;%f;%f;%f;%f;%f;%f;%f;%f\n",i,quicksort_t_sum/j,quicksort_c_sum/j,quicksort_s_sum/j,quicksort_c_sum/(j*i),quicksort_s_sum/(j*i),merge_t_sum/j,merge_c_sum/j,merge_s_sum/j,merge_c_sum/(j*i),merge_s_sum/(j*i),insertion_t_sum/j,insertion_c_sum/j,insertion_s_sum/j,insertion_c_sum/(j*i),insertion_s_sum/(j*i),dual_quicksort_t_sum/j,dual_quicksort_c_sum/j,dual_quicksort_s_sum/j,dual_quicksort_c_sum/(j*i),dual_quicksort_s_sum/(j*i));
            
    }
    fclose(fp);
}
int main(int argc, char **argv)
{
    
        clock_t time_req;

        if(argv[1][2] != 's'){

        char sort =argv[2][0];// m,i,q
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
        printf("--------------------------------\n");

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

                case 'd':

                    printf("Porownania---double pivot quick_sort-----\n");
                    time_req=clock();
                    dual_pivot_quicksort(tab,0,n-1);
                    time_req=clock()-time_req;

                    printf("Sorted ----------------------------------\n");
                    if(order == '<'){
                        list_table(tab,n);
                    }else{
                        print_inverse(tab,n);
                    }
                    
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
    }
    else{

        char *filename=argv[2];
       // printf("%s",filename);
        int k=atoi(argv[3]);
       // printf("%d",k);
        zad3(k,filename);

    }

    return 0;
}
