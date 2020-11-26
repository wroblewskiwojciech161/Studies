
#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#include<string.h>
#include <sys/sysinfo.h>
#include <sys/resource.h>
#include <errno.h>

/*Wojciech Wróblewski  lista3 AiSD  zad1*/


void swap(int *a, int *b){  
        int t = *a;  
        *a = *b;  
        *b = t;  
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
  //j w zakresie (0,i-1) podczas iteracji
    if (order == '<')
    {

            while(j>=0 && tab[j]>key)
            {
    
            //jesli poprzedni wiekszy to zamien
            tab[j+1]=tab[j];
            j=j-1;
            counter_key_swap ++;
            counter_key_compare++;
            }          


    }
    if( order =='>')
    {

            while(j>=0 && tab[j]<key){
            //jesli poprzedni wiekszy to zamien
            tab[j+1]=tab[j];
            j=j-1;
            counter_key_compare++;
	    counter_key_swap ++;
            }
    }
    //zapamietana wartosc klucza przypisz nizej
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
                } 
                else
                { 
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
                    counter_key_swap++;
                    tab[k] = L[i]; 
                    i++; 
                } 
                else
                { 
                    counter_key_swap++;
                    tab[k] = R[j]; 
                    j++; 
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
    } 
  
    // jezeli zostana elementy prawej to przepisz 
    while (j < length_2) 
    { 
        counter_key_swap++;
        tab[k] = R[j]; 
        j++; 
        k++; 
       
    } 
} 
  
//l lewy index tablicy do posortowania
// pracy indeks tablicy do posortowania
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

//------------------------------------------------------------------------RadiX sort

int get_max(int arr[], int n) 
{ 
    int mx = arr[0]; 
    for (int i = 1; i < n; i++) {
        counter_key_compare++;
        if (arr[i] > mx) {
            counter_key_swap++;
            mx = arr[i]; 
        }
            
    }


    return mx; 
} 
int get_min(int arr[], int n) {
  int c, min, index;
 
  min = arr[0];
  index = 0;
 
  for (c = 1; c < n; c++) {
    if (arr[c] < min) {
       index = c;
       min = arr[c];
    }
  }
 
  return arr[index];
}

void radix_count(int tab[], int n, int exponent) 
{ 
    // wynikowa tablica 
    int output[n]; 

    int i;
    // tablica przechowujaca powtorzenia danej cyfry od 0 - 9 w danym rzedzie wielkosci
    int count[20] = {0}; 
  
  

   // prechodzac do tablicy odczutujemy poczatkowo cyfry jednosci, dziesiactek ... 
    //i zapisujemy w count  powtorzenia danych cyfr 
    for (i = 0; i < n; i++){
         //korzystam ze zmiennej counter key compare w tym wypadku nie do liczenia
         //porownan lecz operacji wykonanymi podczas radix sort (poza swap)
         // zeby nie tworzyc kolejnej zmiennej globalnej
         counter_key_compare ++;
          count[ (tab[i]/exponent)%10 + 9]++; 
    } 
      
  
   
    for (i = 1; i < 20 ; i++){
         counter_key_compare ++;
        count[i] += count[i - 1]; 
    } 
        
    // ukladamy dane w tabeli pomocniczej tak
    // aby byly posortowane odpowiedno do danego rzedu wielkosci
    for (i = n - 1; i >= 0; i--) 
    { 
        counter_key_swap++;
        counter_key_compare++;
        output[count[ (tab[i]/exponent)%10 +9] - 1] = tab[i]; 
        count[ (tab[i]/exponent)%10 +9]--; 
    } 
    // majac posortowane dane co do danego rzedu 
    // nadpisujemy je w tabeli wejsciowej
    for (i = 0; i < n; i++){
         counter_key_swap++;
         tab[i] = output[i]; 
    } 
       

} 
  
// radix_sort
void radix_sort(int tab[], int n) 
{ 
  
    int maximum = get_max(tab,n);
    int minimum = get_min(tab,n);

    if(abs(maximum)>abs(minimum))
    {
        maximum=maximum;
    }
    else if(maximum == 0 && minimum ==0)
    {
        maximum=1;
    }
    else
    {
        maximum =abs(minimum);
    }
   
    for (int exp = 1; maximum/exp > 0; exp *= 10) {
        radix_count(tab, n, exp); 
    }
        
} 

void generate_table(int tab[],int n,int range)
{

    for( int i=0;i<n;i++)
    {
        tab[i]=rand()%range;
    }   
 

}
void zad1(int j, char *filename,int range){
     

    FILE *fp;
    fp=fopen(filename,"ab");
    fprintf(fp,"n;q_time;q_c;q_s;q__c/n;q_s/n,m_time;m_c;m_s;m__c/n;m_s/n,i_time;i_c;i_s;i__c/n;i_s/n;r_time;r_c;r_s;r_c/n;r_s/n\n");
    for(int i=50;i<=100000;i+=50){ 
                float quicksort_c_sum=0;float quicksort_s_sum=0;
                float insertion_c_sum=0;float insertion_s_sum=0;
                float merge_c_sum=0;float merge_s_sum=0;
                float radix_c_sum=0;float radix_s_sum=0;
                float quicksort_t_sum=0;float insertion_t_sum=0;float merge_t_sum=0;
                float radix_t_sum=0;

                for(int k=0;k<j;k++){
                    
                    //wygeneruj tablice liczb losowych o podanej dl
                    //zrob kopie dla danych sortowan
                    int tab_q[i],tab_i[i],tab_m[i],tab_r[i];
                    generate_table(tab_q,i,range);
                    copy_table(tab_m,tab_q,i);
                    copy_table(tab_i,tab_q,i);
                    copy_table(tab_r,tab_q,i);


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

                     //radix
                    counter_key_compare=0;
                    counter_key_swap=0;
                    time_req=clock();
                    radix_sort(tab_r,i);
                    time_req=clock()-time_req;
                    radix_c_sum+=counter_key_compare;
                    radix_s_sum+=counter_key_swap;
                    radix_t_sum+=(float)time_req/CLOCKS_PER_SEC;
                    
                
                }
               fprintf(fp,"%d;%f;%f;%f;%f;%f;%f;%f;%f;%f;%f;%f;%f;%f;%f;%f;%f;%f;%f;%f;%f\n",i,quicksort_t_sum/j,quicksort_c_sum/j,quicksort_s_sum/j,quicksort_c_sum/(j*i),quicksort_s_sum/(j*i),merge_t_sum/j,merge_c_sum/j,merge_s_sum/j,merge_c_sum/(j*i),merge_s_sum/(j*i),insertion_t_sum/j,insertion_c_sum/j,insertion_s_sum/j,insertion_c_sum/(j*i),insertion_s_sum/(j*i),radix_t_sum/j,radix_c_sum/j,radix_s_sum/j,radix_c_sum/(j*i),radix_s_sum/(j*i));
               
        }
        fclose(fp);
         
}
int main(int argc, char **argv)
{
    struct rusage r_usage;
  int ret = getrusage(RUSAGE_SELF,&r_usage);
    clock_t time_req;

    if(argv[1][2] != 's'){

        //pobieram odpowiednie char zeby dobrac odpowiednie sortowanie
        char sort =argv[2][0];// m,i,q
        //pobranie znaku porzadku
        char order = argv[4][0];

        printf("Create array. Set size of array :\n");
        int n;
        scanf("%d",&n);
        int tab[n];
        printf("add elements:\n");
        for(int i=0;i<n;i++){
            scanf("%d",&tab[i]);
        }

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
                 case 'r':

                    printf("Porownania--------radix_sort-----\n");
                    time_req=clock();
                    radix_sort(tab,n);
                    time_req=clock()-time_req;
                    printf("Sorted --------------------------\n");
                    if(order=='>'){
                        print_inverse(tab,n);
                    }else{
                         list_table(tab,n);
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
        int k=atoi(argv[3]);
        
        zad1(k,filename,100);
    }
    return 0;
}
