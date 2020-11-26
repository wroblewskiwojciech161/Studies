
#include<climits> 
#include <iostream>
#include <stdlib.h> 
#include <time.h> 
#include <algorithm>
#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#include<string.h>
#include <errno.h>
#include<fstream>
#include<unistd.h>
#include<string>

/*Wojciech Wróblewski  lista3 AiSD  zad2*/
using namespace std; 

int swaps=0;
int comparisons=0;
void swap(int *a, int *b) 
{ 
    int temp = *a; 
    *a = *b; 
    *b = temp; 
} 
int get_max(int arr[], int n) 
{ 
    int mx = arr[0]; 
    for (int i = 1; i < n; i++) {

        if (arr[i] > mx) {
        
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
//--------------------------------------------------------------------------------------QUICKSORT
void  quick_sort (int tab[], int lower, int upper,char order)  
{  
    if (lower < upper)  {
                //wyznaczenie pivota
                int pivot = tab[upper];  
                int i = (lower - 1);  
            
                for (int j = lower; j <= upper - 1; j++)  
                {  
                    
                    if(order == '<')
                    {             
                        comparisons++;
                        cerr<<"compare "<<tab[j]<<" "<<pivot<<endl;            
                        if (tab[j] < pivot)  
                        {  
                            i++;  
                            cerr<<"swap "<<tab[i]<<" "<<tab[j]<<endl;
                            swap(&tab[i], &tab[j]); 
                            swaps++;
                        }  
                    }
                    else
                    {   
                        comparisons++;
                        cerr<<"compare "<<tab[j]<<" "<<pivot<<endl;
                        if (tab[j] > pivot)  
                        {  
                            i++; 
                            cerr<<"compare "<<tab[i]<<" "<<tab[j]<<endl;
                            swap(&tab[i], &tab[j]);  
                            swaps++;
                        }  
                    }       
                }  
                cerr<<"swap "<<tab[i+1]<<" "<<tab[upper]<<endl;
                swaps++;
                //ustawianie pivot na właściwe miejsce
                swap(&tab[i + 1], &tab[upper]);

                int div= i + 1;  
                //rekurancja dla kolejnych podtablic bez juz ustawonego wczesniej elementu
                quick_sort(tab, lower, div - 1,order);  
                quick_sort(tab, div + 1, upper,order); 
            }    
}  
//--------------------------------------------------------------------------------------SELECT
int partition(int tab[], int left, int right, int x) 
{ 
        int i; 
        for (i=left; i<right; i++) {

                cerr<<"compare "<<tab[i]<<" "<<x<<endl;
                comparisons++;
                if (tab[i] == x) 
                break; 
        }

        cerr<<"swaps "<<tab[i]<<" "<<tab[right]<<endl;
        swaps++;
        swap(&tab[i], &tab[right]); 
    
    
        i = left; 
        for (int j = left; j <= right - 1; j++) 
        { 
                cerr<<"compare "<<tab[j]<<" "<<x<<endl;
                comparisons++;
                if (tab[j] <= x) 
                { 
                    cerr<<"swap "<<tab[i]<<" "<<tab[j]<<endl;
                    swaps++;
                    swap(&tab[i], &tab[j]); 
                    i++; 
                } 
        } 
        cerr<<"compare "<<tab[i]<<" "<<tab[right]<<endl;
        swaps++;
        swap(&tab[i], &tab[right]); 
        return i; 
} 
  

int get_median(int arr[], int n) 
{ 
    //tutaj akurat sortowanie quicksortem z poprzednich zadań
    quick_sort(arr,0,n-1,'<') ; 
    //zwracamy medianę
    return arr[n/2];   
} 
  
//implementacja algorytmu select
int select(int tab[], int left, int right, int k) 
{ 
    if (k > 0 && k <= right - left + 1) 
    { 
        int n = right-left+1; 
  
        //dzielimy tablice na podgrupy 5 elementowe i wyznaczamy medianę
        // medianę zapisujemy w tablicy median
        int i, median[(n+4)/5]; 
        for (i=0; i<n/5; i++) {
            median[i] = get_median(tab+left+i*5, 5); 
        }
        // ostatnia grupa może mieć mniej niż 5 elementów
        if (i*5 < n) 
        { 
            median[i] = get_median(tab+left+i*5, n%5);  
            cerr<<"sub-median "<<median[i]<<endl;
            i++; 
        }     
  
        int median_final = (i == 1)? median[i-1]: 
                                 select(median, 0, i-1, i/2); 
        cerr<<"median  "<<median_final<<endl;
  
        int position = partition(tab, left, right, median_final); 
  
        if (position-left == k-1)
        {
           
             return tab[position]; 
        }
           
        if (position-left > k-1)
        {
           
            return select(tab, left, position-1, k); 
        }  
  
        return select(tab, position+1, right, k-position+left-1); 
    } 
  
    return INT_MAX; 
} 
  


  
 //--------------------------------------------------------------------RANDOMIZED SELECT
int random_partition(int tab[], int left, int right)
{
        srand(time(NULL));
        int pivotIdx = left + rand() % (right-left+1);
        int pivot = tab[pivotIdx];
        cerr<<"pivot  "<<tab[pivotIdx]<<endl;

        swaps++;
        cerr<<"swap "<<tab[pivotIdx]<<" "<<tab[right]<<endl;
        swap(tab[pivotIdx], tab[right]); 
        pivotIdx = right;
        int i = left -1;
    
        for(int j=left; j<=right-1; j++)
        {
                cerr<<"compare "<<tab[j]<<" "<<pivot<<endl;
                comparisons++;
                if(tab[j] <= pivot)
                {
                    i = i+1;
                    cerr<<"swap "<<tab[i]<<" "<<tab[j]<<endl;
                    swaps++;
                    swap(tab[i], tab[j]);
                }
        }
        cerr<<"swap "<<tab[i+1]<<" "<<tab[pivotIdx]<<endl;
        swaps++;
        swap(tab[i+1], tab[pivotIdx]);
        return i+1;
}
// implementacja lagorytmu randomized select
int random_selection(int tab[], int left, int right, int k)
{
    if (k > 0 && k <= right - left + 1) { 
        
        if(left == right)

            return tab[left];
    
        if(k ==0) return -1;

        if(left < right)
        {
        
            int mid = random_partition(tab, left, right);
            int i = mid - left + 1;

        
            if(i == k){
                return tab[mid];
            }
        
            if(k < i)
            {
                return random_selection(tab, left, mid-1, k);
            }
           
            else
            {
                return random_selection(tab, mid+1, right, k-i);
            }
           
        }
    }
     return -1;
        
 
}
int value_in_table(int tab[],int n,int value){
     for(int j=0;j<n;j++){
         if(tab[j]==value)return 1;
     }
     return 0;
}
void generate_table(int tab[],int n,int range)
{

   srand((unsigned)time(0)); 
     
    for(int i=0; i<n; i++){
         int value=(rand()%range)+1; 
         while(value_in_table(tab,i,value)==1){
             value=(rand()%range)+1; 
         }
         tab[i]=value;
    }
       

}
void generate_permutation(int tab[],int n){
    for(int i=0;i<n;i++){
        tab[i]=i+1;
    }
    srand(time(NULL));
    random_shuffle(tab,tab+n);
    
}
void list_table(int tab[],int n){
    for(int i=0;i<n;i++){
        printf("%d ",tab[i]);
    }
}
void print_array(int tab[],int size,int value){
    for(int i=0;i<size;i++){
        if(tab[i]==value){
             cout<<"["<<tab[i]<<"]"<<" ";
        }
        else
             cout<<tab[i]<<" ";
    }
    cout<<endl;
}
void copy_table(int tab1[],int tab2[],int n){
    for(int i=0; i<n;i++){
        tab1[i]=tab2[i];
    }

}

void zad2(int j, char *filename){
     

    std::ofstream myfile;
    myfile.open(filename);
    myfile<<"n,time_s,comp_s,swaps_s,s_c_max,s_c_min,time_rs,comp_rs,swaps_rs,rs_c_max,rs_c_min"<<endl;
        for(int i=100;i<=10000;i+=100){
                float time_rs=0;float comp_rs=0;float swaps_rs=0;
                float time_s=0;float comp_s=0;float swaps_s=0;
                int tab_s[i];int tab_rs[i];

                int tab_select_compares_store[j];
                int tab_r_select_compares_store[j];
                //wygeneruj tablice liczb losowych o podanej dl
                //zrob kopie dla danych sortowan
                generate_table(tab_s,i,1000*i);
                copy_table(tab_rs,tab_s,i);

                for(int k=0;k<j;k++){
                    
                   
                    
                    int position = rand()%i;
                  
                    swaps =0;comparisons=0;
                    clock_t time_req=clock();
                    select(tab_s,0,i-1,position);
                    time_req=clock()-time_req;
                    comp_s+=comparisons;
                    swaps_s+=swaps;
                    tab_select_compares_store[k]=comparisons;
                    time_s+=(float)time_req/CLOCKS_PER_SEC;

                    swaps =0;comparisons=0;
                    time_req=clock();
                    random_selection(tab_s,0,i-1,position);
                    time_req=clock()-time_req;
                    comp_rs+=comparisons;
                    swaps_rs+=swaps;
                    tab_r_select_compares_store[k]=comparisons;
                    time_rs+=(float)time_req/CLOCKS_PER_SEC;





                }
               myfile<<i<<","<<time_s/j<<","<<comp_s/j<<","<<swaps_s/j<<" "<<get_max(tab_select_compares_store,j)<<","<<get_min(tab_select_compares_store,j)<<","<<time_rs/j<<","<<comp_rs/j<<","<<swaps_rs/j<<" "<<get_max(tab_r_select_compares_store,j)<<","<<get_min(tab_r_select_compares_store,j)<<endl;
        }
        myfile.close();
         
}

int main(int argc, char **argv) 
{ 
    int pid = getpid();
   
    int n=atoi(argv[2]);
    int k=atoi(argv[3]);
    int tab[n];
    
    if(argv[1][1] == 'p'){
        swaps=0;comparisons=0;
        generate_permutation(tab,n);
        int arr[n];
        copy_table(arr,tab,n);
        int value=random_selection(tab,0,n-1,k);
        cout<<"total swaps "<<swaps<<" total compares "<<comparisons<<endl;
        cout<<endl;
        print_array(arr,n,value);

    }
    else if(argv[1][1] == 'r'){
    
        swaps=0;comparisons=0; 
        generate_table(tab,n,1000*n);
        int arr[n],arr2[n];
        copy_table(arr2,tab,n);
        copy_table(arr,tab,n);
        
        int value=select(tab,0,n-1,k);
        cout<<"total swaps "<<swaps<<" total compares "<<comparisons<<endl;
        cout<<endl;
        print_array(arr,n,value);
        cout<<endl;
    }
    else{
    
        char *filename=argv[4];
        zad2(5,filename);
       
    }
    return 0;
} 








 

