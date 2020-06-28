import java.lang.reflect.Array;
import java.sql.Driver;
import java.util.ArrayList;
import java.util.*;

/* zad3 lista 1 algorytmy metaheurystyczne */
public class zad3 {


    public static void main(String[] args)

    {
        System.setProperty("java.util.Arrays.useLegacyMergeSort", "true");
        Scanner scan = new Scanner(System.in);
        String line = scan.nextLine();
        double time =0, startTime, curTime;
        int sizeX =0, sizeY =0;
     
        try{
            time = Double.parseDouble(line.split(" ")[0]);
            sizeX = Integer.parseInt(line.split(" ")[1]);
            sizeY = Integer.parseInt(line.split(" ")[2]);
        } catch(NumberFormatException ex){
            System.exit(0);
        }
        //Stworzenie planszy
        int[][] grid = new int[sizeX][sizeY];
        //Wczytanie planszy
        for(int i=0; i < sizeX; i++){
            if(!scan.hasNextLine())
                break;
            line = scan.nextLine();
            for(int j =0; j<sizeY; j++){
                grid[i][j] = Character.getNumericValue(line.charAt(j));
            }
        }
        scan.close();



       
        int tab[]= new int[2];
        tab=findStart(grid, sizeX, sizeY).clone();
        
        /*znajdz  sciezke  poczatkowa */
        int[][] path = new int [sizeX*5][2];
        path=findPath(grid, sizeX, sizeY, findStart(grid, sizeX, sizeY)).clone();

        int k =0;
        while(path[k][0]!=0  && path[k][1]!=0){
                k++;
        }
        int[][] base = new int [k+1][2];
        for(int i=0;i<k;i++){
            base[i][0]=path[i][0];
            base[i][1]=path[i][1];
        }
       
         /*tablic krokow dla sciezki poczatkowej*/
         char[] directions = converFromCoordinatesToChars(base).clone();


         /* for(int b =0 ;b < directions.length; b++){
  
              System.out.print(directions[b]+ " ");
          }
          System.out.println(directions.length +" \n");*/
  
          /*tablica tabu z zakazanymi wspolrzedymi swap dla  2 zamiany */
          int[][] tabuArray= new int[path.length][path.length];
          /*okreslenie wielkosci tablicy sasiedztwa */
          int neighbourLength=8;
          /*sasiedztwo*/
          int[][] neighbour = new int[neighbourLength][3];
  
  
          int firstPathLength=directions.length;
          int best =directions.length;
          char[] temp =directions.clone();
          double end =System.currentTimeMillis()+time*1000;
          
  
          while(System.currentTimeMillis()<end){
              //stworz sasiedztwo na podstawie poczatkowej sciezki
              char[] var =directions.clone();
              char[] current =directions.clone();
              neighbour=generateNeighbour(neighbourLength, grid, directions, sizeX, sizeY).clone();
              //sortowanie malejace
              sortbyColumn(neighbour,2);
              int p=0;
              //przechodzac odpowiednio po sasiedztwie sprawdzamy czy wartosc fnkcji celu
              //jest mniejsza od najmniejszej do tej pory
              while(p<neighbourLength){
                      if(neighbour[p][2]<best){
  
                          if(checkIfTabuSwap(neighbour[p][0], neighbour[p][1], tabuArray)==false){
                              swapDirections(neighbour[p][0], neighbour[p][1], current);
  
                        
                              int[][] help = convertFromCharToCoordinates(findStart(grid, sizeX, sizeY), current).clone();
                              
                              if(checkIfPathLeadsToDoor(help, grid, sizeX, sizeY).length>1 && checkIfPathLeadsToDoor(help, grid, sizeX, sizeY).length - 1 < best){
  
                                  best=checkIfPathLeadsToDoor(convertFromCharToCoordinates(findStart(grid, sizeX, sizeY), current), grid, sizeX, sizeY).length - 1;  
                                  char[] helper = converFromCoordinatesToChars(checkIfPathLeadsToDoor(convertFromCharToCoordinates(findStart(grid, sizeX, sizeY), current), grid, sizeX, sizeY)).clone();
                                  
                                   bestPath=helper.clone();
                                  //przypisz nowa najlepsza
                                  directions=helper.clone();
                              }
                              else{
                                  directions=current.clone();
  
                              }
                          }
                          
                      }
                      else{
                          //w przeciwnym wypadku wrzucamy ruch na liste tabu//
                          addToTabuArray(neighbour[p][0], neighbour[p][1], tabuArray);
                         // System.out.println("dodalem do tabu");
                      
                      }
                      
                      p++;
                     
                     
              }
              decrementKadencja(tabuArray, sizeX, sizeY);
             
              
              
             
  
          }  
        System.out.println(best);

        if(best==firstPathLength){

            directions = converFromCoordinatesToChars(base).clone();
            for(int i=0;i<directions.length;i++){
                System.err.print(directions[i]+" ");
            }

        }
        else{
            
            for(int i=0;i<bestPath.length;i++){
                System.err.print(bestPath[i]+" ");
            }

        }
       
    }


    public static char bestPath[];
  
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

    /*metoda tworzy sasiedztwo w postacie tablicy  zawierajacej  wartosc funkcji celu dla dengo swapu  2 - zamiana*/ 
    public static int[][] generateNeighbour(int neighbourLength,int[][] grid,char[] directions,int sizeX,int sizeY){
        int[][] output= new int[neighbourLength][3];
        char [] temp = new char[directions.length];
        int[][] cor = new int[directions.length+1][2];
        int[] swaps= new int[2];

        for(int i=0;i< neighbourLength;i++){
            temp=directions.clone();

                temp=directions.clone();
                swaps=getRandomPair(directions.length-1);
                swapDirections(swaps[0], swaps[1], temp);
                cor=convertFromCharToCoordinates(findStart(grid, sizeX, sizeY), temp);
                temp=converFromCoordinatesToChars(checkIfPathLeadsToDoor(cor, grid, sizeX, sizeY));
                
                output[i][0]=swaps[0];
                output[i][1]=swaps[1];
                output[i][2]=temp.length;
                
        
        }


        return output;

     }
    public static void decrementKadencja(int[][] tabu,int n,int m){
        for( int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(tabu[i][j]>0){
                    tabu[i][j]--;
                }
                
            }
        }
    }
    public static void addToTabuArray(int x,int y,int tabu[][]){
       tabu[x][y]=5;
    }

    public static boolean checkIfTabuSwap(int x,int y,int tabu[][]){
        if(tabu[x][y]>0){
            return true;
        }
        return  false;
    }

    public static int[] getRandomPair(int upper){
        int low=0;
        int[] output= new int[2];
        int x=0;int y=0;
        while(x == y) {
            x = (int) (Math.random() * ((upper - low) + 1)) + low;
            y = (int) (Math.random() * ((upper - low) + 1)) + low;
        }
        output[0]=x;
        output[1]=y;
        return  output;

    }
    public static boolean has_1(int[][] input,int[][] grid){
        int count = 0;

        for(int i = 0; i < input.length; i++)

        {

            int[] a = input[i];
            if(grid[a[0]][a[1]] == 1)

            {

                return true;

            }

        }
        return false;
    }

    public static boolean has_8(int[][] input,int[][] grid){
        int count = 0;

        for(int i = 0; i < input.length; i++)

        {

            int[] a = input[i];
            if(grid[a[0]][a[1]] == 8)

            {

                count++;

            }

        }
        if (count > 0){
            return true;
        }
        else{
            return false;
        }
    }

    public static int[][] checkIfPathLeadsToDoor(int[][] temp,int [][]grid,int n,int m){
        int[][] nothing ={{0,0}};
        for(int i=0;i<temp.length;i++){
            if(temp[i][0]>=n-1 || temp[i][1]>=m|| temp[i][1] < 0 || temp[i][0]<0){
                break;
            }
            if(grid[temp[i][0]][temp[i][1]]==8){
                int[][] output = new int[i+1][2];
                for(int j=0;j<=i;j++){
                    output[j][0]=temp[j][0];
                    output[j][1]=temp[j][1];
                        
                }
                if(has_8(output,grid) == true && has_1(output,grid) == false){
                    return output;
                } 
                else{
                    return nothing;
                }      

                
            }
            
        }
        return nothing;
    }

    public static void swapDirections(int i,int j,char[] dir){
        char temp;
        temp=dir[i];
        dir[i]=dir[j];
        dir[j]=temp;
  
    }

    public static char[] converFromCoordinatesToChars(int[][] cor){
        char [] directions = new char[cor.length-1];
        for( int i=0;i<directions.length;i++){
            if(cor[i+1][0]-cor[i][0]>0){
                directions[i]='D';
            }
            else if(cor[i+1][0]-cor[i][0]<0){
                directions[i]='U';
            }
            else if(cor[i+1][1]-cor[i][1]>0){
                directions[i]='R';
            }
            else if(cor[i+1][1]-cor[i][1]<0){
                directions[i]='L';
            }
        }
        return directions;
    }
    public static int[][] convertFromCharToCoordinates(int initialCoordinates[],char[] directions){
        int[][] output = new int[directions.length+1][2];
        output[0][0]= initialCoordinates[0];
        output[0][1]=initialCoordinates[1];
        for( int i=1;i<=directions.length;i++){
            if(directions[i-1] == 'U'){
                initialCoordinates[0]--;
                output[i][0]=initialCoordinates[0];
                output[i][1]=initialCoordinates[1];

            }
            else if(directions[i-1] == 'D'){
                initialCoordinates[0]++;
                output[i][0]=initialCoordinates[0];
                output[i][1]=initialCoordinates[1];
            }
            else if(directions[i-1] == 'L'){
                initialCoordinates[1]--;
                output[i][0]=initialCoordinates[0];
                output[i][1]=initialCoordinates[1];
            }
            else if(directions[i-1] == 'R'){
                initialCoordinates[1]++;
                output[i][0]=initialCoordinates[0];
                output[i][1]=initialCoordinates[1];
            }

        }


        return output;
    }
    
   
    
     public static int[] findStart(int[][]grid,int sizeX, int sizeY){

        int[] cordinates = new int[2];
        for( int i=0;i<sizeX;i++){
            for(int j=0;j<sizeY;j++){
                if(grid[i][j]==5){
                    cordinates[0]=i;
                    cordinates[1]=j;
                }
            }
        }
        return cordinates;
    }


    public static  int[][] findPath(int[][] grid, int sizeX, int sizeY,int startCoordinates[] ){
        // ArrayList <int[]> path = new ArrayList<int[]>();
         int path[][]= new int[sizeY*sizeX][2];
         int[] temp= new int [2];
         int iterator=0;
       
 
       if(startCoordinates[0]!=1) {
           while (grid[startCoordinates[0]][startCoordinates[1] - 1] != 1) {
 
           
               path[iterator][0] = startCoordinates[0];
               path[iterator][1] = startCoordinates[1];
               iterator++;
 
               if (meetEnd(grid, startCoordinates[0], startCoordinates[1])[0] != -1) {
                 //  System.out.println("mamy 8 w poblizu");
                   path[iterator][0] = meetEnd(grid, startCoordinates[0], startCoordinates[1])[0];
                   path[iterator][1] = meetEnd(grid, startCoordinates[0], startCoordinates[1])[1];
                   return path;
               }
 
               startCoordinates[1]--;
 
           }
       }
 
         while(grid[startCoordinates[0]-1][startCoordinates[1]] != 1){
          
             path[iterator][0]=startCoordinates[0];
             path[iterator][1]=startCoordinates[1];
             iterator++;
 
             if(meetEnd(grid,startCoordinates[0],startCoordinates[1])[0]!=-1){
              
                 path[iterator][0]=meetEnd(grid,startCoordinates[0],startCoordinates[1])[0];
                 path[iterator][1]=meetEnd(grid,startCoordinates[0],startCoordinates[1])[1];
                 return path;
             }
             startCoordinates[0]--;
 
         }
         while(grid[startCoordinates[0]][startCoordinates[1]+1] != 1){
          
             path[iterator][0]=startCoordinates[0];
             path[iterator][1]=startCoordinates[1];
             iterator++;
 
             if(meetEnd(grid,startCoordinates[0],startCoordinates[1])[0]!=-1){
                
                 path[iterator][0]=meetEnd(grid,startCoordinates[0],startCoordinates[1])[0];
                 path[iterator][1]=meetEnd(grid,startCoordinates[0],startCoordinates[1])[1];
                 return path;
             }
             startCoordinates[1]++;
 
 
         }
         while(grid[startCoordinates[0]+1][startCoordinates[1]]!=1){
         
             path[iterator][0]=startCoordinates[0];
             path[iterator][1]=startCoordinates[1];
             iterator++;
 
             if(meetEnd(grid,startCoordinates[0],startCoordinates[1])[0]!=-1){
               
                 path[iterator][0]=meetEnd(grid,startCoordinates[0],startCoordinates[1])[0];
                 path[iterator][1]=meetEnd(grid,startCoordinates[0],startCoordinates[1])[1];
                 return path;
             }
             startCoordinates[0]++;
 
         }
         while(grid[startCoordinates[0]][startCoordinates[1]-1]!=1){
        
             path[iterator][0]=startCoordinates[0];
             path[iterator][1]=startCoordinates[1];
             iterator++;
 
             if(meetEnd(grid,startCoordinates[0],startCoordinates[1])[0]!=-1){
             
                 path[iterator][0]=25;
                 path[iterator][1]=startCoordinates[1];
                 return path;
             }
             startCoordinates[1]--;
 
         }
         while(grid[startCoordinates[0]-1][startCoordinates[1]]!=1){
       
               path[iterator][0]=startCoordinates[0];
               path[iterator][1]=startCoordinates[1];
               iterator++;
   
               if(meetEnd(grid,startCoordinates[0],startCoordinates[1])[0]!=-1){
                  // System.out.println("mamy 8 w poblizu");
                   path[iterator][0]=meetEnd(grid,startCoordinates[0],startCoordinates[1])[0];
                   path[iterator][1]=meetEnd(grid,startCoordinates[0],startCoordinates[1])[1];
                   return path;
               }
               startCoordinates[0]--;
           }
   
         return path;
       }
    public static boolean checkIfContainWall(int[][] grid, int[][] cor){
        for(int i=0;i<cor.length;i++){
            if(grid[cor[i][0]][cor[i][1]]==1)return true;
        }
        return false;
    }
    
    public static int[] meetEnd(int[][] grid,int x, int y){
        int[] out= new int[2];
        if(grid[x+1][y]==8){
            out[0]=x+1;
            out[1]=y;
        }
        else if(grid[x-1][y]==8){
            out[0]=x-1;
            out[1]=y;

        }
        else if(grid[x][y+1]==8){
            out[0]=x;
            out[1]=y+1;
            
        }
        else if(grid[x][y-1]==8){
            out[0]=x;
            out[1]=y-1;
        }
        else{
            out[0]=-1;
            out[1]=-1;

        }
        return out;



    }

}
