#include <iostream>
#include <string.h>
#include <bits/stdc++.h>
#include<time.h>

using namespace std;


/*dodatkowa część zad3 lista2 AiSD
implementacja hybrydowego algorytmu sortowania  merge + insertion

algorytmy sortujące dowolnie zadeklarowany typ danych 
typ danych nalezy zadeklarować na poziomie kodu 
w funkcji main
*/

int counter_key_swap=0;
int counter_key_compare=0;

template <class T>
void swap(T* a, T* b){  
        T t = *a;  
        *a = *b;  
        *b = t;  
}  

namespace sort{

    template <class T> void merge(T tab[], int left, int mid, int right,char order) 
    { 
    
        int i, j, k; 
        int length_1 = mid - left + 1; 
        int length_2 =  right - mid; 
        T L[length_1], R[length_2]; 
    
        for (i = 0; i < length_1; i++) 
            L[i] = tab[left + i]; 

        for (j = 0; j < length_2; j++) 
            R[j] = tab[mid + 1+ j]; 
        i = 0; 
        j = 0; 
        k = left;

        while (i < length_1 && j < length_2) 
        { 
            cout<<"comp : "<<L[i]<<" and "<<R[j]<<endl;
            counter_key_compare++;
            if(order == '<'){
                    if (L[i] < R[j]) 
                    { 
                        cout<<"swap : "<<tab[k]<<" and "<<L[i]<<endl;
                        counter_key_swap++;                  
                        tab[k] = L[i]; 
                        i++;  
                    } 
                    else
                    { 
                        cout<<"swap : "<<tab[k]<<" and "<<R[j]<<endl;
                        counter_key_swap++;
                        tab[k] = R[j]; 
                        j++;  
                    } 
                    k++; 
            }
            if(order =='>'){
                    if (L[i] > R[j]) 
                    { 
                        cout<<"swap : "<<tab[k]<<" and "<<L[i]<<endl;
                        counter_key_swap++;
                        tab[k] = L[i]; 
                        i++; 
                    
                    } 
                    else
                    { 
                        cout<<"swap : "<<tab[k]<<" and "<<R[j]<<endl;
                        counter_key_swap++;
                        tab[k] = R[j]; 
                        j++;                    
                    } 
                    k++; 
            }
        } 
        while (i < length_1) 
        { 
            cout<<"swap : "<<tab[k]<<" and "<<L[i]<<endl;
            counter_key_swap++;
            tab[k] = L[i]; 
            i++; 
            k++; 
            
        } 
        while (j < length_2) 
        { 
            cout<<"swap : "<<tab[k]<<" and "<<R[j]<<endl;
            counter_key_swap++;
            tab[k] = R[j]; 
            j++; 
            k++; 
        } 
    } 
    
    template <class T> void merge_sort(T tab[], int l, int r,char order) 
    { 
        if (l < r) 
        { 
            int m = (l+r)/2;
            merge_sort(tab, l, m,order); 
            merge_sort(tab, m+1, r,order); 
    
            merge(tab, l, m, r,order); 
        } 
    } 
    //---------------------------------------------------------------------------------
    template <class T> void insertion_sort(T tab[], int left, int right,char order) 
    {   
        
            for (int i = left + 1; i <= right; i++) 
            { 
                T key = tab[i]; 
                int j = i - 1; 
                if(order=='<'){
                        while (tab[j] > key && j >= left) 
                        {        
                            cout<<"comp : "<<tab[j]<<" and "<<key<<endl;
                            cout<<"swap : "<<tab[j+1]<<" and "<<tab[j]<<endl;     
                            counter_key_swap++;        
                            counter_key_compare++;              
                            tab[j+1] = tab[j]; 
                            j--;                    
                        } 
                }
                if(order=='>'){
                        while (tab[j] < key && j >= left) 
                        { 
                            cout<<"comp : "<<tab[j]<<" and "<<key<<endl;
                            cout<<"swap : "<<tab[j+1]<<" and "<<tab[j]<<endl;   
                            counter_key_swap++;
                            counter_key_compare++;
                            tab[j+1] = tab[j]; 
                            j--;                     
                        } 
                }
                cout<<"swap : "<<tab[j+1]<<" and "<<key<<endl;   
                counter_key_swap++;
                tab[j+1] = key; 
            } 
    } 
    //------------------------------------------------------------------------------
    template <class T> void  quick_sort (T tab[], int lower, int upper,char order)  
    {  
        if (lower < upper)  {
                    //wyznaczenie pivota
                    T pivot = tab[upper];  
                    int i = (lower - 1);  
                
                    for (int j = lower; j <= upper - 1; j++)  
                    {  
                        cout<<"comp : "<<tab[j]<<" and "<<pivot<<endl;   
                        counter_key_compare++;
                        if(order == '<')
                        {                         
                            if (tab[j] < pivot)  
                            {  
                                i++;  
                                cout<<"swap : "<<tab[i]<<" and "<<tab[j]<<endl;   
                                swap(&tab[i], &tab[j]); 
                                counter_key_swap++;
                            }  
                        }
                        else
                        {         
                            if (tab[j] > pivot)  
                            {  
                                i++; 
                                cout<<"swap : "<<tab[i]<<" and "<<tab[j]<<endl;   
                                swap(&tab[i], &tab[j]);  
                                counter_key_swap++;
                            }  
                        }       
                    }  
                    counter_key_swap++;
                    //ustawianie pivot na właściwe miejsce
                    cout<<"swap : "<<tab[i+1]<<" and "<<tab[upper]<<endl;   
                    swap(&tab[i + 1], &tab[upper]);

                    int div= i + 1;  
                    //rekurancja dla kolejnych podtablic bez juz ustawonego wczesniej elementu
                    quick_sort(tab, lower, div - 1,order);  
                    quick_sort(tab, div + 1, upper,order); 
                }    
    }  
    //----------------------------------------------------------------------------------
    template <class T> int make_part(T tab[], int low, int high, int* left) 
    { 
        counter_key_compare++;
        if (tab[low] > tab[high]) {
            counter_key_swap++;
            cout<<"swap : "<<tab[low]<<" and "<<tab[high]<<endl;   
            swap(&tab[low], &tab[high]); 
        }
        //inicjalizacja indeksow i przypisanie dla pivot lefti right
        int j = low + 1; 
        int l = high - 1;
        int k = low + 1;
        T left_pivot = tab[low];
        T right_pivot = tab[high]; 

        while (k <= l) { 
            
            if (tab[k] < left_pivot) { 
                cout<<"comp : "<<tab[k]<<" and "<<left_pivot<<endl;   
                cout<<"swap : "<<tab[k]<<" and "<<tab[j]<<endl;   
                counter_key_compare++;
                counter_key_swap++;
                swap(&tab[k], &tab[j]); 
                j++; 
            } 
    
            else if (tab[k] >= right_pivot) { 

                cout<<"comp : "<<tab[k]<<" and "<<right_pivot<<endl;   
                counter_key_compare++;
                while (tab[l] > right_pivot && k < l){
                    counter_key_compare++;
                        l--;    
                } 


                counter_key_swap++;
                cout<<"swap : "<<tab[k]<<" and "<<tab[l]<<endl;   
                swap(&tab[k], &tab[l]); 
                l--; 
                counter_key_compare++;
                cout<<"comp : "<<tab[k]<<" and "<<left_pivot<<endl;   
                if (tab[k] < left_pivot) { 
                    counter_key_swap++; 
                    cout<<"swap : "<<tab[k]<<" and "<<tab[j]<<endl;   
                    swap(&tab[k], &tab[j]); 
                    j++; 
                } 
            } 
            k++; 
        } 
        j--; 
        l++; 
        counter_key_swap+=2;
    
        cout<<"swap : "<<tab[low]<<" and "<<tab[j]<<endl;   
        cout<<"swap : "<<tab[high]<<" and "<<tab[l]<<endl;   
        swap(&tab[low], &tab[j]); 
        swap(&tab[high], &tab[l]); 
    
        *left = j;
        
        return l; 
    } 
    template <class T> void dual_pivot_quicksort(T tab[], int low, int high) 
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
    //----------------------------------------------------------------------
    /*interwał sortowania ustawiony na 3 tylko na potrzeby ręcznego deklarowania 
     małych tablic żeby zobaczyć zasadę działania
     normalnie intervał ustawia się na potęgi dwójki 32,64*/
    int interval=3;
    
    int min(int num1,int num2){
        if(num1>num2)
            return num2;
        else 
            return num1;

    }
    template <class T> void hybrid_sort(T tab[], int n,char order) 
    { 
        for (int i = 0; i < n; i+=interval) 
            insertion_sort(tab, i, min((i+interval-1), (n-1)),order); 
    

        for (int size = interval; size < n; size = 2*size) 
        { 
        
            for (int left = 0; left < n; left += 2*size) 
            { 
                
                int mid = left + size - 1; 
                int right = min((left + 2*size - 1), (n-1)); 
                merge(tab, left, mid, right,order); 
            } 
        } 
    } 
    template <class T> void print_inverse(T tab[],int n){
        for( int i=n-1;i>=0;i--){
            cout<<tab[i]<<" ";
            
        }cout<<endl;
    }
    template <class T> void list_table(T tab[],int n){
        for(int i=0;i<n;i++){
            cout<<tab[i]<<" ";
        }cout<<endl;
    }



}
int main(int argc, char **argv)
{
    
    clock_t time_req;

    if(argv[1][2] != 's'){

        char sort =argv[2][0];// m,i,q
        char order = argv[4][0];
        

        cout<<("Create array. Set size of array :\n");
        int n;
        cin>>n;
        
        /*zdefiniowany tutaj typ danej tabeli mozna zmienic w zaleznosci od 
        typu danych jaki chcemy sortować   string,float,...*/
         float tab[n];


        cout<<("add elements:\n");
        for(int i=0;i<n;i++){
            cin>>tab[i];
        }


            switch (sort)
            {
                case 'i':
                    cout<<"Porownania----insertion_sort-----\n";
                    time_req=clock();
                    sort::insertion_sort(tab,0,n-1,order);
                    time_req=clock()-time_req;
                    cout<<"Sorted --------------------------\n";
                    sort::list_table(tab,n);
                    cout<<"Czas dzialania algorytmu : "<<(double)time_req/CLOCKS_PER_SEC;
                    

                    break;
                case 'm':

                    cout<<"Porownania----merge_sort--------\n";
                    time_req=clock();
                    sort::merge_sort(tab,0,n-1,order);
                    time_req=clock()-time_req;
                    cout<<"Sorted --------------------------\n";   
                    sort::list_table(tab,n);
                    cout<<"Czas dzialania algorytmu : "<<(double)time_req/CLOCKS_PER_SEC;
                   
                    break;
                case 'q':

                    cout<<"Porownania--------quick_sort-----\n";
                    time_req=clock();
                    sort::quick_sort(tab,0,n-1,order);
                    time_req=clock()-time_req;
                    cout<<"Sorted --------------------------\n";
                    sort::list_table(tab,n);
                    cout<<"Czas dzialania algorytmu : "<<(double)time_req/CLOCKS_PER_SEC;
                   
                    break;

                case 'd':

                    cout<<"Porownania---double pivot quick_sort-----\n";
                    time_req=clock();
                    sort::dual_pivot_quicksort(tab,0,n-1);
                    time_req=clock()-time_req;

                    cout<<"Sorted ----------------------------------\n";
                    if(order == '<'){
                         sort::list_table(tab,n);
                    }else{
                         sort::print_inverse(tab,n);
                    }
                    cout<<"Czas dzialania algorytmu : "<<(double)time_req/CLOCKS_PER_SEC;
                    
                    break;

                   case 'h':

                    cout<<"Porownania---hybrid_sort-----\n";
                    time_req=clock();
                    sort::hybrid_sort(tab,n,order);
                    time_req=clock()-time_req;
                    cout<<"Sorted ----------------------------------\n";
                    sort::list_table(tab,n);
                    cout<<"Czas dzialania algorytmu : "<<(double)time_req/CLOCKS_PER_SEC;
                    
                    break;
                default:
                    cout<<"error.";
                    break;
            }
            cout<<endl;
            cout<<"Porownania : " << counter_key_compare << endl;
            cout<<"Przestawienia kluczy : " << counter_key_swap << endl; 
            
    }
    else{

       cout<<("wrong syntax");

    }


    return 0;
}

