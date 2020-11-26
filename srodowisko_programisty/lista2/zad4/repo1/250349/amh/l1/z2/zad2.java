
import java.util.*;
/*algorytmy metaheurystyczne zad2 lista 1 */



public class zad2 {
    public static int kadencja=7;
    public static int best;
     //przechowuje input
     public static int size;
     public static int input[][];

    public static void copyArray(int a[],int b[]){
        for (int i=0; i<a.length; i++)
            b[i] = a[i];
    }
   
    
    
    public static void decrementKadencja(int tabu[][],int size){
        for(int i=0;i<size;i++){
            for(int j=0;j<size;j++){
                if(tabu[i][j]>0){
                    tabu[i][j]--;
                }
            }
        }
    }
    // sortowanie tablicy ze wzgledu na kolumne
    public static void sortbyColumn(int arr[][], int col)
    {
        
        Arrays.sort(arr, new Comparator<int[]>() {

            @Override
           
            public int compare(final int[] entry1,
                               final int[] entry2) {

               
                if (entry1[col] > entry2[col])
                    return 1;
                else
                    return -1;
            }
        });  
    }

    public static void printTableTwoDiemsion(int tab[][],int x,int y){
        for(int i=0;i<x;i++){
            for(int j=0;j<y;j++){
                System.out.print(tab[i][j] + ",  ");
            }
            System.out.println("\n");
        }
    }
    public static void printTableOneDimension(int tab[],int sideLength){
        for(int i=0;i<sideLength;i++){
            System.err.print(tab[i] + "  ");
        }
        System.err.print(tab[0] + "  ");
       
    }
    //tasuje permutaccje
    public static void shuffle(int a[],int n){
        // shuffle
        for (int i = 0; i < n; i++) {
            int r = (int) (Math.random() * (i+1));     
            int swap = a[r];
            a[r] = a[i];
            a[i] = swap;
        }
    }
    public static int[] generatePermutation(int n){
        int[] permutation= new int[n];
        for(int i=1;i<=n;i++){
            permutation[i-1]=i;
        }
        shuffle(permutation,n);
       return permutation;
    }
    public static void swap(int index1,int index2,int tab[] ){
        int temp =tab[index1];
        tab[index1]=tab[index2];
        tab[index2]=temp;
    }
    public static void swapByValue(int val1,int val2,int tab[] ){
        int index1=0;int index2=0;
        for(int i=0;i<tab.length;i++){
            if(tab[i]==val1)index1=i;
            if(tab[i]==val2)index2=i;
        }
        int temp =tab[index1];
        tab[index1]=tab[index2];
        tab[index2]=temp;
    }

    public static boolean checkIfInArray(int value,int tab[]){
        for(int i=0;i<tab.length;i++){
            if(tab[i]==value)return true;
        }
        return false;
    }
    public static int getRandomIntegerInRange(int low,int upper){
            int x = (int)(Math.random()*((upper-low)+1))+low;
            return  x;

    }
    public static boolean checkIfInRandomList(ArrayList <int[]> list, int x, int y){
       for(int i=0;i<list.size();i++){
        if(list.get(i)[0]==x && list.get(i)[1]==y){
            return true;
        }
       }
       return false;
    }

    //generowanie sasiedztwa  jako tablicy zawierajacej  wspolrzedne swapu oraz  wartosc funkcji celu dla danego swapa
    public static int[][] generateNeighbour(int input[][],int length,int size,int[] initial){
      
        int[] temp= new int[size];
        ArrayList <int[]> choices = new ArrayList<>();
        int []pair=new int[2];


        //tablica sasiedztwa
        int[][] neighbour = new int[length][3];
        for( int i=0;i<length;i++){
            copyArray(initial,temp);
            
            neighbour[i][0]=getRandomIntegerInRange(1,size);
            neighbour[i][1]=getRandomIntegerInRange(1,size);
            //losujemy tak dlugo by tablica nie zawierala powtorzonych swapow
            while(checkIfInRandomList(choices, neighbour[i][0], neighbour[i][1])){
            neighbour[i][0]=getRandomIntegerInRange(1,size);
            neighbour[i][1]=getRandomIntegerInRange(1,size);
            }
            pair[0]=neighbour[i][0];
            pair[1]=neighbour[i][1];
            choices.add(pair);
            swapByValue( neighbour[i][0], neighbour[i][1],temp);
            neighbour[i][2]=getCost(input,temp)-getCost(input,initial);

        }

        return neighbour;
    }


    
    public static int getDistance(int city1,int city2,int tab[][]){
       return tab[city1-1][city2-1];
    }

    // oblicza funkcje kosztu dla danej permutacji
    public static int getCost(int[][]input,int[] permutation){
        int cost =0;
        for(int i=0;i<permutation.length-1;i++){
           
            cost+=getDistance(permutation[i],permutation[i+1],input);
        }
        cost+=getDistance(permutation[permutation.length-1],permutation[0],input);
        return cost;
    }
    public static int[][] getSwapIndexes(int permutationSize){
        int index=0;
        int output[][]= new int[permutationSize*(permutationSize-1)/2][2];
        for(int i=0;i<permutationSize-1;i++){
            for(int j=i+1;j<permutationSize;j+=1){
               
                output[index][0]=i;
                output[index][1]=j;
                index++;
            }
        }

        return output;
    }
    // metoda dodaje swapu na liste tabu
    public static void addToTabuSwap(int city1,int city2,int tabu[][]){
        tabu[city1-1][city2-1]=kadencja;
    }
    
    public static boolean checkIfTabuSwap(int city1,int city2,int tabu[][]){
        if(tabu[city1-1][city2-1]>0){
            return true;
        }
        return  false;
    }
    public static int costDifference(int[] initial,int[] permutation){
        return getCost(input,initial)-getCost(input,permutation);
    }


    
   public static void main(String[] args) {
    System.setProperty("java.util.Arrays.useLegacyMergeSort", "true");

        Scanner scan = new Scanner(System.in);
        String line = scan.nextLine();
        double time =0;
        int size =0;
        try{
            time = Double.parseDouble(line.split(" ")[0]);
            size = Integer.parseInt(line.split(" ")[1]);
        } catch(NumberFormatException ex){
            System.exit(0);
        }
        int[][] input = new int[size][size];
        for(int i=0; i < size; i++){
            if(!scan.hasNextLine())
                break;
            line = scan.nextLine();
            String[] tab = line.split(" ");
            for(int j =0; j<size; j++){
                input[i][j] = Integer.parseInt(tab[j]);
            }
        }   
        scan.close(); 
       
       
         

        int neihbourLength=(int)(size*0.8);
        int[][] neighbour =new int[neihbourLength][3];

        //tablica tabu na poczatek wypelniona zerami dla kazdej z permutacji
        int tabu[][] = new int[size][size];
        for(int i=0;i<size ;i++){
            for(int j=0;j<size;j++){
                tabu[i][j]=0;

            }
        }
        
        //pierwsza losowa permutacja
        int[] initialPermutation=generatePermutation(size);
        int[] bestPermutation= new int[size];
        best=getCost(input,initialPermutation);
        int current;
      
       

       double end =System.currentTimeMillis()+time*1000;
       while(System.currentTimeMillis()<end){
           //ustalamy tymczasowy 
           current=getCost(input,initialPermutation);
           //tworzymy sasiedztwo
           neighbour=generateNeighbour(input,neihbourLength,size,initialPermutation);
           //sortujemy rosnaco 
           sortbyColumn(neighbour,2);
       
           int k=0;
           /*przechodzimy po sasiedztwie az do wybrania najbardziej oczekiwanej pod wzgledem 
           funkcji kosztu permutacji */
           while(k!=neighbour.length){


                /* jesli po swapie permutacja jest kandydatem na nowe minimum 
                korzystamy z  niej mimo to ze jest na liscie tabu */
               if(neighbour[k][2]+current< best){
                   swapByValue(neighbour[k][0],neighbour[k][1],initialPermutation);
                    best = neighbour[k][2]+current;
                    copyArray(initialPermutation,bestPermutation);
                    current=current+ neighbour[k][2];
              

                break;
               }
               /*wybierz taki swap taki co powoduje najmniej strat  jesli nie znajduje sie na liscie tabu */
                if(checkIfTabuSwap(neighbour[k][0],neighbour[k][1],tabu)==false){
                   swapByValue(neighbour[k][0],neighbour[k][1],initialPermutation);
                   current=current+neighbour[k][2];
                   addToTabuSwap(neighbour[k][0],neighbour[k][1],tabu);
                   break;
               }
            k++;
           }
            decrementKadencja(tabu,size);
           

        }
        
       System.out.println(best);
       printTableOneDimension(bestPermutation,bestPermutation.length);
       
    }

}