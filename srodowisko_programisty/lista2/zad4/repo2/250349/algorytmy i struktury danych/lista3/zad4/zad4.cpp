

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


/*zad 4 lista 3 Wojciech Wroblewski AiSD*/
using namespace std; 
int comparisons=0;
int swaps=0;

int partition(int tab[], int left, int right, int x) ;
int select(int tab[], int left, int right, int k) ;
  
    
void swap(int *a, int *b) 
{ 
    int temp = *a; 
    *a = *b; 
    *b = temp; 
} 
  


void printArray(int arr[], int size) 
{ 
    int i; 
    for (i=0; i < size; i++) 
        cout << arr[i] << " "; 
    cout << endl; 
} 
//implementacja quick sort + select
void quicksort_with_select(int tab[], int left, int right) 
{ 
    if (left < right) 
    { 
        
        int n = right-left+1; 
        int med = select(tab, left, right, n/2); 
        int p = partition(tab, left, right, med); 
  
        quicksort_with_select(tab, left, p - 1); 
        quicksort_with_select(tab, p + 1, right); 
    } 
} 
  
//--------------------------------------------------------------------------------------SELECT
int partition(int tab[], int left, int right, int x) 
{ 
        int i; 
        for (i=left; i<right; i++) {

               
                comparisons++;
                if (tab[i] == x) 
                break; 
        }

        
        swaps++;
        swap(&tab[i], &tab[right]); 
    
    
        i = left; 
        for (int j = left; j <= right - 1; j++) 
        { 
                
                comparisons++;
                if (tab[j] <= x) 
                { 
                    ;
                    swaps++;
                    swap(&tab[i], &tab[j]); 
                    i++; 
                } 
        } 
        
        swaps++;
        swap(&tab[i], &tab[right]); 
        return i; 
} 
  

int get_median(int arr[], int n) 
{ 
   
    sort(arr,arr+n);
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
            i++; 
        }     
  
        int median_final = (i == 1)? median[i-1]: 
                                 select(median, 0, i-1, i/2); 
  
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
  
//implementacja algorytmu  dual pivot quicksort + select
void dual_pivot_with_select(int tab[], int left, int right)  
{  
    if (left < right)  
    {  
        int n = right-left+1; 
        int med1 = select(tab, left, right, n/3); 
        int med2 = select(tab, left, right, 2*n/3); 
        int p1 = partition(tab, left, right, med1);
        int p2 = partition(tab, left, right, med2);
        
        dual_pivot_with_select(tab, left, p1-1 );  
        dual_pivot_with_select(tab, p1+1 , p2-1 );  
        dual_pivot_with_select(tab, p2+1 , right); 
    }  
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
void copy_table(int tab1[],int tab2[],int n){
    for(int i=0; i<n;i++){
        tab1[i]=tab2[i];
    }

}

void zad3(int j,string filename){
     

    std::ofstream myfile;
    myfile.open(filename);
    myfile<<"n,time_quick_s,comp_quick_s,swaps_quick_s,time_dual_s,comp_dual_s,swaps_dual_s\n"<<endl;
        for(int i=100;i<=10000;i+=100){
                float time_rs=0;float comp_rs=0;float swaps_rs=0;
                float time_s=0;float comp_s=0;float swaps_s=0;
                int tab_s[i];int tab_rs[i];

               
                generate_table(tab_s,i,1000*i);
                copy_table(tab_rs,tab_s,i);

                for(int k=0;k<j;k++){
                    
                   
                    
                    int position = rand()%i;
                  
                    swaps =0;comparisons=0;
                    clock_t time_req=clock();
                    quicksort_with_select(tab_s,0,i-1);
                    time_req=clock()-time_req;
                    comp_s+=comparisons;
                    swaps_s+=swaps;
                    time_s+=(float)time_req/CLOCKS_PER_SEC;

                    swaps =0;comparisons=0;
                    time_req=clock();
                    dual_pivot_with_select(tab_rs,0,i-1);
                    time_req=clock()-time_req;
                    comp_rs+=comparisons;
                    swaps_rs+=swaps;
                    time_rs+=(float)time_req/CLOCKS_PER_SEC;





                }
               myfile<<i<<","<<time_s/j<<","<<comp_s/j<<","<<swaps_s/j<<","<<time_rs/j<<","<<comp_rs/j<<","<<swaps_rs/j<<" "<<endl;
        }
        myfile.close();
         
}

int main() 
{ 
    int arr[] = {123,24,-65,25,77,55,0}; 
    int tab[] = {1313,0,-5,4,3,2,8,9}; 
    int n = sizeof(arr)/sizeof(arr[0]); 
    int k=sizeof(tab)/sizeof(tab[0]);

    printArray(arr,n);cout<<endl;
    dual_pivot_with_select(arr, 0, n-1); 
    cout << "Posortowana tablica dual_pivot_select \n"; 
    printArray(arr, n); 


    cout<<endl;

    printArray(tab,k);cout<<endl;
    quicksort_with_select(tab, 0, k-1); 
    cout << "Posortowana tablica quick_select \n"; 
    printArray(tab, k); 


   // zad3(5,"data.txt");

    return 0; 
} 
